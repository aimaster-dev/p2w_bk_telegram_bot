''' 财务 '''
import datetime, time, json
from flask import request, render_template, current_app
from .cms_base import CmsTableViewBase, CmsFormViewBase
from models.pay_table import CollectionOrderTable, MerchantTable, BankCardTable, BankTable, MerchantBillStatementTable, BankCardBillTable, WithdrawTable, MerchantTunnleTable, TunnelTable, RechargeMoneyTable, AgentadminBillLogTable
from constants import BANK_CODE, PAY_METHOD, WITHDRAW_STATUS, CallbackState, ROlE_ALL, BankCardType, BILL_STATEMEN_TYPES, BankBillTypes
from common_utils.utils_funcs import PagingCLS
from models.behalfPay import behalfPayOrderTable
from common_utils.lqredis import SiteRedis
from models.cms_user import CmsUserTable
from common_utils.utils_funcs import update_language



class MerchantTunnleTotalView(CmsFormViewBase):
    add_url_rules = [['/merchantTunnleTotal', 'merchantTunnleTotal']]
    title = '商户通道报表'
    MCLS = CollectionOrderTable
    template = 'cms/finance/merchantTunnleTotal.html'

    def view_get(self):
        merchant = request.args.get('merchant')
        tunnel_code = request.args.get('tunnel_code')
        orderDate = request.args.get('orderDate')
        datas = []
        search_res = {}
        fff = {'is_review': True}
        if merchant and merchant.strip():
            fff['$or'] = [{'merchant_id': merchant.strip()}, {'merchant_name': merchant.strip()}]
            search_res['merchant'] = merchant
        if tunnel_code and tunnel_code.strip():
            search_res['tunnel_code'] = tunnel_code
        if orderDate and orderDate.strip():
            start_time, end_time = PagingCLS.by_silce(orderDate)
        else:
            crrdate = datetime.datetime.now()
            start_time, end_time = datetime.datetime(crrdate.year, crrdate.month, crrdate.day, 0, 0, 0), datetime.datetime(crrdate.year, crrdate.month, crrdate.day, 23, 59, 59)
            orderDate = start_time.strftime('%Y-%m-%d %H:%M:%S') + '|' + end_time.strftime('%Y-%m-%d %H:%M:%S')

        if self.current_admin_dict.get('role_code') == ROlE_ALL.AGENTADMIN:
            fff['agentadmin_uuid'] = self.current_admin_dict.get('uuid')
        elif self.current_admin_dict.get('role_code') == ROlE_ALL.SYSTEMUSER:
            fff['agentadmin_uuid'] = self.current_admin_dict.get('agentadmin_uuid')

        # 代收申请单数
        total_dssqds = 0
        # 代收成功单数
        total_dscgds = 0
        # 代收成功金额
        total_dscgje = 0
        # 代收成功手续费
        total_dscgsxf = 0
        search_res['orderDate'] = orderDate
        mdatas = MerchantTable.find_many(fff)
        for mdata in mdatas:
            for metht in PAY_METHOD.name_arr:
                _dd = {
                    'tunnel_name': PAY_METHOD.name_dict.get(metht),
                    'mdata': mdata,
                }
                if tunnel_code and tunnel_code.strip() and metht != tunnel_code.strip():
                    continue
                df_fv = 0
                tunnel_data = TunnelTable.find_one({'code': metht}) or {}
                if tunnel_data:
                    mtunnlet_data = MerchantTunnleTable.find_one({'merchant_uuid': mdata.get('uuid'), 'tunnle_id': tunnel_data.get('uuid')}) or {}
                    df_fv = mtunnlet_data.get('rate') or 0
                _dd['df_fv'] = round(df_fv * 100, 3)

                fff1 = {'order_time': {'$gte': start_time, '$lte': end_time}, 'merchant_id': mdata.get('merchant_id'), 'pay_method': metht, 'agentadmin_uuid': mdata.get('agentadmin_uuid')}
                # 代收总订单数
                order_counts = CollectionOrderTable.count(fff1) or 0
                if order_counts == 0:
                    continue
                total_dssqds += order_counts

                fff2 = {'callback_time': {'$gte': start_time, '$lte': end_time}, 'merchant_id': mdata.get('merchant_id'), 'pay_method': metht, 'agentadmin_uuid': mdata.get('agentadmin_uuid')}
                fff2.update({
                    'pay_statu': True,
                    'callback_statu': CallbackState.SUCCESS,
                })
                # 代收成功单数
                success_order_counts = CollectionOrderTable.count(fff2) or 0
                total_dscgds += success_order_counts

                # 代收成功率
                if order_counts:
                    ds_success_rate = round(success_order_counts / order_counts * 100, 2)
                else:
                    ds_success_rate = 0

                # 代收成功金额
                df_repay_amount_amount_ll = CollectionOrderTable.collection().aggregate([
                    {"$match": fff2},
                    {"$group": {"_id": None, "actual_amount": {"$sum": '$actual_amount'}}},
                ])
                ds_actual_amount_ll = list(df_repay_amount_amount_ll)
                ds_actual_amount = 0
                if ds_actual_amount_ll:
                    ds_actual_amount = ds_actual_amount_ll[0].get('actual_amount')
                total_dscgje += ds_actual_amount

                # 代收成功手续费
                df_repay_amount_amount_ll = CollectionOrderTable.collection().aggregate([
                    {"$match": fff2},
                    {"$group": {"_id": None, "repay_amount": {"$sum": '$repay_amount'}}},
                ])
                ds_repay_amount_ll = list(df_repay_amount_amount_ll)
                ds_repay_amount = 0
                if ds_repay_amount_ll:
                    ds_repay_amount = ds_repay_amount_ll[0].get('repay_amount')
                total_dscgsxf += ds_repay_amount

                _dd.update({
                    'ds_success_rate': str(ds_success_rate) + '%',
                    'ds_success_count': success_order_counts,
                    'ds_success_money': self.format_money(ds_actual_amount),
                    'ds_success_repay': ds_repay_amount,
                    'ds_order_count': order_counts
                })
                datas.append(_dd)

        total_data = {
            'total_dssqds': total_dssqds,
            'total_dscgds': total_dscgds,
            'total_dscgje': self.format_money(total_dscgje),
            'total_dscgsxf': self.format_money(total_dscgsxf),
        }
        self.context['all_datas'] = datas
        self.context['title'] = self.title
        self.context['search_res'] = search_res
        self.context['PAY_METHOD'] = PAY_METHOD
        self.context['total_data'] = total_data
        
        html =  render_template(self.template, **self.context)
        return update_language(self.current_admin_dict.get("language"), html)



class ReconciliationView(CmsFormViewBase):
    add_url_rules = [['/reconciliationForm', 'reconciliationForm']]
    title = '对账日报'
    MCLS = CollectionOrderTable
    template = 'cms/finance/reconciliationForm.html'

    def view_get(self):
        kkk1 = f'{current_app.config.get("PROJECT_NAME")}_reconciliationForm_datas'
        kkk2 = f'{current_app.config.get("PROJECT_NAME")}_reconciliationForm_total_data'
        _datas = SiteRedis.get(kkk1)
        _total_data = SiteRedis.get(kkk2)
        merchant = request.args.get('merchant')
        orderDate = request.args.get('orderDate')
        datas = []
        total_data = {}
        search_res = {}
        if not merchant and not orderDate:
            if _datas:
                datas = json.loads(_datas.decode())
            if _total_data:
                total_data = json.loads(_total_data.decode())

        if not datas:
            fff = {'is_review': True}
            if merchant and merchant.strip():
                fff['$or'] = [{'merchant_id': merchant.strip()}, {'merchant_name': merchant.strip()}]
                search_res['merchant'] = merchant
            if orderDate and orderDate.strip():
                start_time, end_time = PagingCLS.by_silce(orderDate)
            else:
                crrdate = datetime.datetime.now()
                start_time, end_time = datetime.datetime(crrdate.year, crrdate.month, crrdate.day, 0, 0, 0), datetime.datetime(crrdate.year, crrdate.month, crrdate.day, 23, 59, 59)
                orderDate = start_time.strftime('%Y-%m-%d %H:%M:%S') + '|' + end_time.strftime('%Y-%m-%d %H:%M:%S')
            search_res['orderDate'] = orderDate

            if self.current_admin_dict.get('role_code') == ROlE_ALL.AGENTADMIN:
                fff['agentadmin_uuid'] = self.current_admin_dict.get('uuid')
            elif self.current_admin_dict.get('role_code') == ROlE_ALL.SYSTEMUSER:
                fff['agentadmin_uuid'] = self.current_admin_dict.get('agentadmin_uuid')

            # 代收申请单数
            total_ds_sqds = 0
            # 代收成功单数
            total_ds_cgds = 0
            # 代收成功金额
            total_ds_cgje = 0
            # 代收成功手续费
            total_ds_cgsxf = 0
            # 代付成功单数
            total_df_cgds = 0
            # 代付成功金额
            total_df_cgje = 0
            # 代付手续费
            total_df_zsxf = 0
            # 下发申请单数
            total_xf_sqds = 0
            # 下发申请金额
            total_xf_sqje = 0
            # 下发成功金额
            total_xf_cgje = 0
            # 下发总手续费
            total_xf_sxf = 0
            # 充值总费用
            total_cz = 0
            # 充值总手续费
            total_cz_sxf = 0

            mdatas = MerchantTable.find_many(fff)
            for mdata in mdatas:
                _dd = {
                    'merchant_id': mdata.get('merchant_id'),
                    'merchant_name': mdata.get('merchant_name'),
                }
                orderdatas = CollectionOrderTable.find_many({'order_time': {'$gte': start_time, '$lte': end_time}, 'pay_statu': True, 'callback_statu': CallbackState.SUCCESS, 'merchant_id': mdata.get('merchant_id'), 'agentadmin_uuid': mdata.get('agentadmin_uuid')})
                if not orderdatas:
                    _dd.update({
                        'ds_order_count': 0,
                        'ds_success_count': 0,
                        'ds_success_money': 0,
                        'ds_success_repay': 0,
                    })
                else:
                    success_count = 0
                    failed_count = 0
                    total_money = 0
                    repay_money = 0
                    for odata in orderdatas:
                        if odata.get('pay_statu'):
                            success_count += 1
                            total_money += odata.get('actual_amount') or 0
                            repay_money += odata.get('repay_amount') or 0
                        else:
                            failed_count += 1

                    _dd.update({
                        'ds_order_count': success_count + failed_count,
                        'ds_success_count': success_count,
                        'ds_success_money': self.format_money(total_money),
                        'ds_success_repay': self.format_money(repay_money),
                    })
                total_ds_sqds += _dd.get('ds_order_count') or 0
                total_ds_cgds += _dd.get('ds_success_count') or 0
                total_ds_cgje += float(str(_dd.get('ds_success_money')).replace(',','')) or 0
                total_ds_cgsxf += float(str(_dd.get('ds_success_repay')).replace(',','')) or 0

                wdatas = WithdrawTable.find_many({'merchant_uuid': mdata.get('uuid'), 'create_time': {'$gte': start_time, '$lte': end_time}, 'agentadmin_uuid': mdata.get('agentadmin_uuid')})
                if not wdatas:
                    _dd.update({
                        'xf_count': 0,
                        'xf_money': 0,
                        'xf_success_money': 0,
                        'xf_total_repay': 0,
                    })
                else:
                    xf_count = len(wdatas)
                    xf_money = 0
                    xf_success_money = 0
                    xf_total_repay = 0
                    for wdata in wdatas:
                        xf_money += wdata.get('amount') or 0
                        if wdata.get('statu') == WITHDRAW_STATUS.success:
                            xf_success_money += wdata.get('amount') or 0
                            xf_total_repay += wdata.get('repay_amount') or 0
                    _dd.update({
                        'xf_count': xf_count,
                        'xf_money': self.format_money(xf_money),
                        'xf_success_money': self.format_money(xf_success_money),
                        'xf_total_repay': self.format_money(xf_total_repay),
                    })
                total_xf_sqds += _dd.get('xf_count')
                total_xf_sqje += float(str(_dd.get('xf_money')).replace(',','')) or 0
                total_xf_cgje += float(str(_dd.get('xf_success_money')).replace(',','')) or 0
                total_xf_sxf += float(str(_dd.get('xf_total_repay')).replace(',','')) or 0

                if _dd.get('ds_order_count') == 0 and _dd.get('xf_count') == 0:
                    continue

                # 代付成功订单数
                dfsuccess_total = behalfPayOrderTable.count({'order_time': {'$gte': start_time, '$lte': end_time}, 'pay_statu': True, 'merchant_id': mdata.get('merchant_id'), 'agentadmin_uuid': mdata.get('agentadmin_uuid')})
                total_df_cgds += dfsuccess_total

                # 代付成功支付金额
                dfsuccess_amount_ll = behalfPayOrderTable.collection().aggregate([
                    {"$match": {'order_time': {'$gte': start_time, '$lte': end_time}, 'pay_statu': True, 'merchant_id': mdata.get('merchant_id'), 'agentadmin_uuid': mdata.get('agentadmin_uuid')}},
                    {"$group": {"_id": None, "order_amount": {"$sum": '$order_amount'}}},
                ])
                dfsuccess_amount_l = list(dfsuccess_amount_ll)
                dfsuccess_amount = 0
                if dfsuccess_amount_l:
                    dfsuccess_amount = dfsuccess_amount_l[0].get('order_amount')
                total_df_cgje += dfsuccess_amount

                # 代付手续费
                df_repay_amount_amount_ll = behalfPayOrderTable.collection().aggregate([
                    {"$match": {'order_time': {'$gte': start_time, '$lte': end_time}, 'pay_statu': True, 'merchant_id': mdata.get('merchant_id'), 'agentadmin_uuid': mdata.get('agentadmin_uuid')}},
                    {"$group": {"_id": None, "repay_amount": {"$sum": '$repay_amount'}}},
                ])
                df_repay_amount_amount_l = list(df_repay_amount_amount_ll)
                df_repay_amount_total = 0
                if df_repay_amount_amount_l:
                    df_repay_amount_total = df_repay_amount_amount_l[0].get('repay_amount')
                total_df_zsxf += df_repay_amount_total

                _dd['dfsuccess_total'] = dfsuccess_total or 0
                _dd['dfsuccess_amount'] = self.format_money(dfsuccess_amount or 0)
                _dd['df_repay_amount_total'] = self.format_money(df_repay_amount_total or 0)

                # 内充金额
                cz_amount_ll = RechargeMoneyTable.collection().aggregate([
                    {"$match": {'create_time': {'$gte': start_time, '$lte': end_time}, 'merchant_id': mdata.get('merchant_id')}},
                    {"$group": {"_id": None, "amount": {"$sum": '$amount'}}},
                ])
                cz_amount_l = list(cz_amount_ll)
                cz_amount = 0
                if cz_amount_l:
                    cz_amount = cz_amount_l[0].get('amount')
                total_cz += cz_amount
                _dd['cz_amount'] = self.format_money(cz_amount or 0)

                # 内充手续费
                cz_amount_sxf_ll = RechargeMoneyTable.collection().aggregate([
                    {"$match": {'create_time': {'$gte': start_time, '$lte': end_time}, 'merchant_id': mdata.get('merchant_id')}},
                    {"$group": {"_id": None, "amount": {"$sum": '$amount'}}},
                ])
                cz_amount_sxf_l = list(cz_amount_sxf_ll)
                cz_amount_sxf = 0
                if cz_amount_sxf_l:
                    cz_amount_sxf = cz_amount_sxf_l[0].get('amount')
                total_cz_sxf += cz_amount_sxf
                _dd['cz_amount_sxf'] = self.format_money(cz_amount_sxf or 0)

                datas.append(_dd)
            total_data = {
                'total_ds_sqds': total_ds_sqds,
                'total_ds_cgds': total_ds_cgds,
                'total_ds_cgje': self.format_money(total_ds_cgje),
                'total_ds_cgsxf': self.format_money(total_ds_cgsxf),
                'total_df_cgds': total_df_cgds,
                'total_df_cgje': self.format_money(total_df_cgje),
                'total_df_zsxf': self.format_money(total_df_zsxf),
                'total_xf_sqds': total_xf_sqds,
                'total_xf_sqje': self.format_money(total_xf_sqje),
                'total_xf_cgje': self.format_money(total_xf_cgje),
                'total_xf_sxf': self.format_money(total_xf_sxf),
                'total_cz': self.format_money(total_cz),
                'total_cz_sxf': self.format_money(total_cz_sxf),
            }

            SiteRedis.set(kkk1, json.dumps(datas), expire=10*60)
            SiteRedis.set(kkk2, json.dumps(total_data), expire=10*60)

        self.context['title'] = self.title
        self.context['all_datas'] = datas
        self.context['search_res'] = search_res
        self.context['total_data'] = total_data
        
        html =  render_template(self.template, **self.context)
        return update_language(self.current_admin_dict.get("language"), html)



class BankcardFormView(CmsFormViewBase):
    add_url_rules = [['/bankcardForm', 'bankcardForm']]
    title = '银行卡报表'
    MCLS = BankCardTable
    template = 'cms/finance/bankcardForm.html'

    def is_xhr(self):
        X_Requested_With = request.headers.get('X-Requested-With')
        if not X_Requested_With or X_Requested_With.lower() != 'xmlhttprequest':
            return
        return True

    def deal_duration(self, duration: int) -> str:
        """
        处理时长 example: 90 --> 00:01:30
        :param duration: int 时长 单位s
        :return: str '00:01:30'
        """
        try:
            return time.strftime('%H:%M:%S', time.gmtime(int(duration)))
        except:
            return ''

    def format_money(self, data):
        try:
            if '.' in str(data):
                return format(float(data), ",")
            return format(int(data), ",")
        except:
            return data

    def get_context(self):
        _back_datas = BankTable.find_many({})
        back_datas = []
        for d in _back_datas:
            if d.get('code') in BANK_CODE:
                back_datas.append(d)
        res = {
            'back_datas': back_datas,
            'format_money': self.format_money,
        }
        crrdate = datetime.datetime.now()
        start_time, end_time = datetime.datetime(crrdate.year, crrdate.month, crrdate.day, 0, 0, 0), datetime.datetime(
            crrdate.year, crrdate.month, crrdate.day, 23, 59, 59)
        dataDate = start_time.strftime('%Y-%m-%d %H:%M:%S') + '|' + end_time.strftime('%Y-%m-%d %H:%M:%S')
        search_res = {
            'dataDate': dataDate,
        }
        if self.current_admin_roleCode == ROlE_ALL.SUPERADMIN or self.current_admin_roleCode == ROlE_ALL.ADMINISTRATOR:
            search_res['bankcard_type'] = BankCardType.SYSTEM_CARD
        if self.current_admin_roleCode == ROlE_ALL.AGENTADMIN or self.current_admin_roleCode == ROlE_ALL.SYSTEMUSER:
            search_res['bankcard_type'] = BankCardType.AGENTADMIN_CARD
        res['search_res'] = search_res
        return res

    def search_data_func(self):
        account = request.args.get('account')
        bank_uid = request.args.get('bank_uid')
        dataDate = request.args.get('dataDate')
        datas = []
        search_res = {}
        filter_dict = {}
        if account and account.strip():
            filter_dict['account'] = account.strip()
            search_res['account'] = account
        if bank_uid and bank_uid.strip():
            filter_dict['bank_uid'] = bank_uid.strip()
            search_res['bank_uid'] = bank_uid
        if dataDate and dataDate.strip():
            start_time, end_time = PagingCLS.by_silce(dataDate)
        else:
            crrdate = datetime.datetime.now()
            start_time, end_time = datetime.datetime(crrdate.year, crrdate.month, crrdate.day, 0, 0, 0), datetime.datetime(crrdate.year, crrdate.month, crrdate.day, 23, 59, 59)
            dataDate = start_time.strftime('%Y-%m-%d %H:%M:%S') + '|' + end_time.strftime('%Y-%m-%d %H:%M:%S')

        bankcard_type = request.args.get('bankcard_type')
        if bankcard_type:
            filter_dict['bankcard_type'] = bankcard_type.strip()
            search_res['bankcard_type'] = bankcard_type

        crr_agentadmin_uuid = ''
        if self.current_admin_dict.get('role_code') == ROlE_ALL.AGENTADMIN:
            crr_agentadmin_uuid = self.current_admin_dict.get('uuid')
            if self.current_admin_dict.get('is_syscard'):
                filter_dict['$or'] = [{'bankcard_type': BankCardType.AGENTADMIN_CARD}, {'agentadmin_uuid': self.current_admin_dict.get('uuid')}]
            else:
                filter_dict['agentadmin_uuid'] = self.current_admin_dict.get('uuid')
        elif self.current_admin_dict.get('role_code') == ROlE_ALL.SYSTEMUSER:
            crr_agentadmin_uuid = self.current_admin_dict.get('agentadmin_uuid')
            if self.current_admin_dict.get('agentadmin_data').get('is_syscard'):
                filter_dict['$or'] = [{'bankcard_type': BankCardType.AGENTADMIN_CARD}, {'agentadmin_uuid': self.current_admin_dict.get('agentadmin_uuid')}]
            else:
                filter_dict['agentadmin_uuid'] = self.current_admin_dict.get('agentadmin_uuid')

        bankcard_money_total = 0
        bank_dict = {}
        search_res['dataDate'] = dataDate
        bcdatas = BankCardTable.find_many(filter_dict)
        for bcdata in bcdatas:
            _dd = {
                'account': bcdata.get('account'),
                'account_username': bcdata.get('account_username'),
            }
            bank_data = bank_dict.get(bcdata.get('bank_uid'))
            if not bank_data:
                bank_data = BankTable.find_one({'uuid': bcdata.get('bank_uid')}) or {}
                bank_dict[bcdata.get('bank_uid')] = bank_data
            _dd['shortName'] = bank_data.get('shortName')
            _dd['bank_code'] = bank_data.get('code')

            fff1 = {
                'order_time': {'$gte': start_time, '$lte': end_time}, 'bankcard_id': bcdata.get('uuid'),
            }
            if crr_agentadmin_uuid:
                fff1.update({'agentadmin_uuid': crr_agentadmin_uuid})
            order_total_counts = CollectionOrderTable.count(fff1)

            fff3 = {
                'order_time': {'$gte': start_time, '$lte': end_time}, 'bankcard_id': bcdata.get('uuid'),
                'pay_statu': True,
            }
            if crr_agentadmin_uuid:
                fff3.update({'agentadmin_uuid': crr_agentadmin_uuid})
            success_counts = CollectionOrderTable.count(fff3)

            # 成功支付金额
            fff4 = {
                'pay_statu': True, 'bankcard_id': bcdata.get('uuid'),
                'order_time': {'$gte': start_time, '$lte': end_time},
            }
            if crr_agentadmin_uuid:
                fff4.update({'agentadmin_uuid': crr_agentadmin_uuid})
            ddsls = CollectionOrderTable.collection().aggregate([
                {"$match": fff4},
                {"$group": {"_id": None, "actual_amount": {"$sum": '$actual_amount'}}},
            ])
            dddss = list(ddsls)
            if dddss:
                total_sk_amount = dddss[0].get('actual_amount')
            else:
                total_sk_amount = 0

            if order_total_counts:
                py_rate = round(success_counts / order_total_counts * 100, 2)
            else:
                py_rate = 0

            ff5 = {
                'pay_statu': True, 'callback_statu': CallbackState.SUCCESS, 'is_lose': False,
                'bankcard_id': bcdata.get('uuid'), 'order_time': {'$gte': start_time, '$lte': end_time}
            }
            if crr_agentadmin_uuid:
                ff5.update({'agentadmin_uuid': crr_agentadmin_uuid})

            # 订单到回调完成时间
            total_succsed_ddd = CollectionOrderTable.collection().aggregate([
                {"$match": ff5},
                {"$group": {"_id": None, "success_seconds": {"$sum": '$success_seconds'}}},
            ])
            total_success_seconds = list(total_succsed_ddd)
            ff6 = {
                'pay_statu': True, 'callback_statu': CallbackState.SUCCESS, 'is_lose': False,
                'bankcard_id': bcdata.get('uuid'), 'order_time': {'$gte': start_time, '$lte': end_time},
            }
            if crr_agentadmin_uuid:
                ff6.update({'agentadmin_uuid': crr_agentadmin_uuid})
            total_success_count = CollectionOrderTable.count(ff6) or 0
            if total_success_count and total_success_seconds:
                success_second_rate = int(total_success_seconds[0].get('success_seconds') / total_success_count)
            else:
                success_second_rate = 0

            fff7 = {
                'pay_statu': True, 'callback_statu': CallbackState.SUCCESS, 'is_lose': False,
                'bankcard_id': bcdata.get('uuid'), 'order_time': {'$gte': start_time, '$lte': end_time}
            }
            if crr_agentadmin_uuid:
                fff7.update({'agentadmin_uuid': crr_agentadmin_uuid})

            # 订单到支付时间
            total_suc_datas1 = CollectionOrderTable.find_many(fff7) or []
            total_suc_count1 = len(total_suc_datas1)
            total_success_seconds1 = 0
            total_sf_money = 0
            for dd1 in total_suc_datas1:
                pay_time = dd1.get('pay_time')
                order_time = dd1.get('order_time')
                actual_amount = dd1.get('actual_amount') or 0
                _ts_seconds = int((pay_time - order_time).seconds)
                total_success_seconds1 += _ts_seconds
                total_sf_money += actual_amount

            if total_suc_count1 and total_success_seconds1:
                success_second_rate1 = int(total_success_seconds1 / total_suc_count1)
            else:
                success_second_rate1 = 0

            # 掉单金额
            ff9 = {
                'pay_statu': True, 'is_lose': True,
                'bankcard_id': bcdata.get('uuid'), 'order_time': {'$gte': start_time, '$lte': end_time}
            }
            _lose_money_total = CollectionOrderTable.collection().aggregate([
                {"$match": ff9},
                {"$group": {"_id": None, "actual_amount": {"$sum": '$actual_amount'}}},
            ])
            lose_money_total_ll = list(_lose_money_total)
            lose_money_total = 0
            if lose_money_total_ll:
                lose_money_total = lose_money_total_ll[0].get('actual_amount')

            # 爬虫收到金额
            fff10 = {
                'create_time': {'$gte': start_time, '$lte': end_time}, 'bankacrd_uuid': bcdata.get('uuid'), 'bill_type': BankBillTypes.INCOME_ORDER
            }
            _income_money_total = BankCardBillTable.find_many(fff10)
            _income_money_total = BankCardBillTable.collection().aggregate([
                {"$match": fff10},
                {"$group": {"_id": None, "amount": {"$sum": '$amount'}}},
            ])
            income_money_total_ll = list(_income_money_total)
            income_money_total = 0
            if income_money_total_ll:
                income_money_total = income_money_total_ll[0].get('amount')

            # 爬虫转出金额
            fff11 = {
                'create_time': {'$gte': start_time, '$lte': end_time}, 'bankacrd_uuid': bcdata.get('uuid'), 'bill_type': BankBillTypes.OUT_ORDER
            }
            _out_money_total_ll = BankCardBillTable.collection().aggregate([
                {"$match": fff11},
                {"$group": {"_id": None, "amount": {"$sum": '$amount'}}},
            ])
            out_money_total_ll = list(_out_money_total_ll)
            out_money_total = 0
            if out_money_total_ll:
                out_money_total = out_money_total_ll[0].get('amount')

            # 成功订单金额
            fff12 = {
                'pay_statu': True, 'callback_statu': CallbackState.SUCCESS,
                'bankcard_id': bcdata.get('uuid'), 'order_time': {'$gte': start_time, '$lte': end_time}
            }
            if crr_agentadmin_uuid:
                fff12.update({'agentadmin_uuid': crr_agentadmin_uuid})
            _success_order_money_total = CollectionOrderTable.collection().aggregate([
                {"$match": fff12},
                {"$group": {"_id": None, "order_amount": {"$sum": '$order_amount'}}},
            ])
            success_order_money_total_ll = list(_success_order_money_total)
            success_order_money_total = 0
            if success_order_money_total_ll:
                success_order_money_total = success_order_money_total_ll[0].get('order_amount')

            # 成功回调金额
            fff13 = {
                'callback_statu': CallbackState.SUCCESS, 'bankcard_id': bcdata.get('uuid'),
                'callback_time': {'$gte': start_time, '$lte': end_time},
            }
            if crr_agentadmin_uuid:
                fff13.update({'agentadmin_uuid': crr_agentadmin_uuid})
            ddsls = CollectionOrderTable.collection().aggregate([
                {"$match": fff13},
                {"$group": {"_id": None, "actual_amount": {"$sum": '$actual_amount'}}},
            ])
            dddss = list(ddsls)
            if dddss:
                success_callback_money = dddss[0].get('actual_amount')
            else:
                success_callback_money = 0
            bankcard_money_total += success_callback_money

            _dd.update({
                'order_total_counts': order_total_counts,
                'success_counts': success_counts,
                'success_second_rate': self.deal_duration(success_second_rate),
                'success_second_rate1': self.deal_duration(success_second_rate1),
                'py_rate': str(py_rate) +'%',
                'bankcard_type': BankCardType.name_dict.get(bcdata.get('bankcard_type')) or '',
                'success_order_money_total': self.format_money(success_order_money_total),
                'total_sk_amount': self.format_money(total_sk_amount),
                'success_callback_money': self.format_money(success_callback_money),
                'lose_money_total': self.format_money(lose_money_total),
                'income_money_total': self.format_money(income_money_total),
                'out_money_total': self.format_money(abs(out_money_total)),
            })
            datas.append(_dd)
        return self.xtjson.json_result(data={'datas': datas, 'bankcard_money_total': self.format_money(bankcard_money_total),})

    def view_get(self):
        if self.is_xhr():
            return self.search_data_func()
        self.context['title'] = self.title
        self.context['BankCardType'] = BankCardType
        res = self.get_context()
        self.context.update(res)
        
        html =  render_template(self.template, **self.context)
        return update_language(self.current_admin_dict.get("language"), html)



class MerchantBillStatementView(CmsTableViewBase):
    add_url_rules = [['/billStatement', 'merchantBillStatement']]
    title = '账单流水'
    MCLS = MerchantBillStatementTable
    template = 'merchant/billStatement.html'
    per_page = 30

    def get_filter_dict(self):
        return {'merchant_uuid': self.current_admin_dict.get('uuid')}

    def dealwith_main_context(self):
        all_datas = self.context.get('all_datas')
        datas = []
        for da in all_datas:
            merchant_data = MerchantTable.find_one({'uuid': da.get('merchant_uuid')})
            da['merchant_data'] = merchant_data
            datas.append(da)
        self.context['all_datas'] = datas
        self.context['BILL_STATEMEN_TYPES'] = BILL_STATEMEN_TYPES



class MerchantBillFormView(CmsFormViewBase):
    add_url_rules = [['/merchantForm', 'merchantForm']]
    title = '商户报表'
    MCLS = MerchantBillStatementTable
    template = 'cms/finance/merchantForm.html'

    def is_xhr(self):
        X_Requested_With = request.headers.get('X-Requested-With')
        if not X_Requested_With or X_Requested_With.lower() != 'xmlhttprequest':
            return
        return True

    def search_data_func(self):
        if request.args.get('search_type') == "merchant_search":
            return self.search_merchant_func()
        if request.args.get('search_type') == "agent_search":
            return self.search_agent_func()

    def search_agent_func(self):
        merchant = request.args.get('merchant')
        dataDate = request.args.get('dataDate')
        search_type = request.args.get('search_type')
        agentadmin_account = request.args.get('agentadmin_account')
        datas = []
        search_res = {}
        filter_dict_agent = {}

        if merchant and merchant.strip():
            filter_dict_agent['username'] = merchant.strip()
            search_res['merchant'] = merchant
        if agentadmin_account and agentadmin_account.strip():
            filter_dict_agent['account'] =  agentadmin_account.strip()

        if dataDate and dataDate.strip():
            start_time, end_time = PagingCLS.by_silce(dataDate)
        else:
            crrdate = datetime.datetime.now()
            start_time, end_time = datetime.datetime(crrdate.year, crrdate.month, crrdate.day, 0, 0, 0), datetime.datetime(crrdate.year, crrdate.month, crrdate.day, 23, 59, 59)
            dataDate = start_time.strftime('%Y-%m-%d %H:%M:%S') + '|' + end_time.strftime('%Y-%m-%d %H:%M:%S')

        crr_agentadmin_uuid = ''

        if self.current_admin_dict.get('role_code') == ROlE_ALL.AGENTADMIN:
            crr_agentadmin_uuid = self.current_admin_dict.get('uuid')
        elif self.current_admin_dict.get('role_code') == ROlE_ALL.SYSTEMUSER:
            filter_dict_agent['agentadmin_uuid'] = self.current_admin_dict.get('agentadmin_uuid')

        if crr_agentadmin_uuid:
            filter_dict_agent['agentadmin_uuid'] = crr_agentadmin_uuid

        # 代收金额
        total_dsje = 0
        # 代收手续费
        total_dssxf = 0
        # 代付金额
        total_sfje = 0
        # 代付手续费
        total_sfsxf = 0
        # 手动下发金额
        total_sdxfje = 0
        # 手动下发手续费
        total_sdxfjxf = 0
        total_incharge_amount = 0
        total_incharge_fee = 0

        search_res['dataDate'] = dataDate
        search_res['search_type'] = search_type

        filter_dict_agent['role_code'] = ROlE_ALL.AGENTADMIN
        agents = CmsUserTable.find_many(filter_dict_agent)
        for agent in agents:
            _dd = {
                'agent_account': agent.get('account'),
                'agent_name': agent.get('username'),
            }
            mdatas = MerchantTable.find_many({"agentadmin_uuid": agent["uuid"]})

            ds_aomunt_total_agent = 0
            dssxf_aomunt_total_agent = 0
            df_aomunt_total_agent = 0
            dfsxf_aomunt_total_agent = 0
            sdxf_aomunt_total_agent = 0
            sdxfsxf_aomunt_total_agent = 0
            end_balance_amount_agent = 0
            start_balance_amount_agent = 0
            wc_vv_agent = 0
            for mdata in mdatas:
                # 代收金额
                fff1 = {
                    'callback_time': {'$gte': start_time, '$lte': end_time},
                    'pay_statu': True,
                    'callback_statu': CallbackState.SUCCESS,
                    'merchant_id': mdata.get('merchant_id'),
                }

                ds_aomunt_total = 0
                dssxf_aomunt_total = 0
                collectionOrders = CollectionOrderTable.find_many(fff1)
                for collectionOrder in collectionOrders:
                    ds_aomunt_total += collectionOrder.get("actual_amount")
                    dssxf_aomunt_total += collectionOrder.get("repay_amount")
                    tennel = TunnelTable.find_one({"code": collectionOrder.get("pay_method")})
                    merchant_tennel = MerchantTunnleTable.find_one({"tunnle_id":tennel.get("uuid"), "merchant_uuid":mdata.get("uuid")})
                    agent_rate = 0
                    if collectionOrder.get("pay_method") == "VNBANKQR":
                        agent_rate = agent.get("in_vnbankqr_rate")
                    elif collectionOrder.get("pay_method") == "VNZALO":
                        agent_rate = agent.get("in_vnbankqr_rate")
                    elif collectionOrder.get("pay_method") == "VNMOMO":
                        agent_rate = agent.get("in_vnbankqr_rate")
                    elif collectionOrder.get("pay_method") == "VNVTPAY":
                        agent_rate = agent.get("in_vnbankqr_rate")
                    elif collectionOrder.get("pay_method") == "VNMO2MO":
                        agent_rate = agent.get("in_vnbankqr_rate")
                    elif collectionOrder.get("pay_method") == "VNZA2LO":
                        agent_rate = agent.get("in_vnbankqr_rate")
                    elif collectionOrder.get("pay_method") == "VNVT2PAY":
                        agent_rate = agent.get("in_vnbankqr_rate")
                    elif collectionOrder.get("pay_method") == "VNBANKQR2":
                        agent_rate = agent.get("in_vnbankqr_rate")

                    wc_vv_agent += collectionOrder.get("actual_amount")*(merchant_tennel["rate"]-agent_rate)

                ds_aomunt_total_agent += ds_aomunt_total
                dssxf_aomunt_total_agent += dssxf_aomunt_total

                # 代付金额
                fff3 = {
                    'order_time': {'$gte': start_time, '$lte': end_time},
                    'pay_statu': True,
                    'merchant_id': mdata.get('merchant_id'),
                }
                df_aomunt_total_ll = behalfPayOrderTable.collection().aggregate([
                    {"$match": fff3},
                    {"$group": {"_id": None, "order_amount": {"$sum": '$order_amount'}}},
                ])
                df_aomunt_total = 0
                df_aomunt_total_l = list(df_aomunt_total_ll)
                if df_aomunt_total_l:
                    df_aomunt_total = df_aomunt_total_l[0].get('order_amount')
                df_aomunt_total_agent += df_aomunt_total
                wc_vv_agent += df_aomunt_total * (mdata["payment_rate"] - agent["paybehalf_rate"])

                # 代付手续费
                fff4 = {
                    'order_time': {'$gte': start_time, '$lte': end_time},
                    'pay_statu': True,
                    'merchant_id': mdata.get('merchant_id'),
                }
                dfsxf_aomunt_total_ll = behalfPayOrderTable.collection().aggregate([
                    {"$match": fff4},
                    {"$group": {"_id": None, "repay_amount": {"$sum": '$repay_amount'}}},
                ])
                dfsxf_aomunt_total = 0
                dfsxf_aomunt_total_l = list(dfsxf_aomunt_total_ll)
                if dfsxf_aomunt_total_l:
                    dfsxf_aomunt_total = dfsxf_aomunt_total_l[0].get('repay_amount')
                dfsxf_aomunt_total_agent += dfsxf_aomunt_total

                # 手动下发
                fff5 = {
                    'create_time': {'$gte': start_time, '$lte': end_time},
                    'statu': WITHDRAW_STATUS.success,
                    'merchant_uuid': mdata.get('uuid'),
                }
                sdxf_aomunt_total_ll = WithdrawTable.collection().aggregate([
                    {"$match": fff5},
                    {"$group": {"_id": None, "amount": {"$sum": '$amount'}}},
                ])
                sdxf_aomunt_total = 0
                sdxf_aomunt_total_l = list(sdxf_aomunt_total_ll)
                if sdxf_aomunt_total_l:
                    sdxf_aomunt_total = sdxf_aomunt_total_l[0].get('amount')
                sdxf_aomunt_total_agent += sdxf_aomunt_total
                wc_vv_agent += sdxf_aomunt_total * (mdata["issued_money_rate"] - agent["issued_money_rate"])

                # 手动下发手续费
                fff6 = {
                    'create_time': {'$gte': start_time, '$lte': end_time},
                    'statu': WITHDRAW_STATUS.success,
                    'merchant_uuid': mdata.get('uuid'),
                }
                sdxfsxf_aomunt_total_ll = WithdrawTable.collection().aggregate([
                    {"$match": fff6},
                    {"$group": {"_id": None, "repay_amount": {"$sum": '$repay_amount'}}},
                ])
                sdxfsxf_aomunt_total = 0
                sdxfsxf_aomunt_total_l = list(sdxfsxf_aomunt_total_ll)
                if sdxfsxf_aomunt_total_l:
                    sdxfsxf_aomunt_total = sdxfsxf_aomunt_total_l[0].get('repay_amount')
                sdxfsxf_aomunt_total_agent += sdxfsxf_aomunt_total

                fff7 = {
                    'create_time': {'$gte': start_time, '$lte': end_time},
                    'merchant_id': mdata.get('merchant_id'),
                }
                recharges = RechargeMoneyTable.find_many(fff7)
                internal_charge_amount = 0
                for recharge in recharges:
                    internal_charge_amount += recharge.get('amount')
                wc_vv_agent += internal_charge_amount * (mdata["recharge_money_rate"] - agent["recharge_money_rate"])

            end_mb_data = AgentadminBillLogTable.find_one({'agentadmin_uuid': agent["uuid"], "bill_type": "recharge",'create_time': {'$gte': start_time, '$lte': end_time}}, sort=[['create_time', -1]]) or {}
            if not end_mb_data:
                end_mb_data = MerchantBillStatementTable.find_one(
                    {'agentadmin_uuid': agent["uuid"], "bill_type": "recharge", 'create_time': {'$lte': start_time}},
                    sort=[['create_time', -1]]) or {}
            if end_mb_data:
                end_balance_amount_agent = self.format_money(end_mb_data.get('balance_amount') or 0)
            else:
                end_balance_amount_agent = 0

            start_mb_data = AgentadminBillLogTable.find_one(
                {'agentadmin_uuid': agent['uuid'], "bill_type": "recharge", 'create_time': {'$gte': start_time}},
                sort=[['create_time', 1]]) or {}
            if start_mb_data:
                start_balance_amount_agent = self.format_money(
                    start_mb_data['balance_amount'] - start_mb_data['amount'] + start_mb_data["repay_amount"] or 0)
            else:
                start_balance_amount_agent = 0

            _dd['ds_aomunt_total'] = self.format_money(ds_aomunt_total_agent)
            _dd['dssxf_aomunt_total'] = self.format_money(dssxf_aomunt_total_agent)
            _dd['df_aomunt_total'] = self.format_money(df_aomunt_total_agent)
            _dd['dfsxf_aomunt_total'] = self.format_money(dfsxf_aomunt_total_agent)
            _dd['sdxf_aomunt_total'] = self.format_money(sdxf_aomunt_total_agent)
            _dd['sdxfsxf_aomunt_total'] = self.format_money(sdxfsxf_aomunt_total_agent)
            _dd['end_balance_amount'] = self.format_money(end_balance_amount_agent)
            _dd['start_balance_amount'] = self.format_money(start_balance_amount_agent)
            _dd['wc_vv'] = self.format_money(wc_vv_agent)

            datas.append(_dd)
            total_dsje += ds_aomunt_total_agent
            total_dssxf += dssxf_aomunt_total_agent
            total_sfje += df_aomunt_total_agent
            total_sfsxf += dfsxf_aomunt_total_agent
            total_sdxfje += sdxf_aomunt_total_agent
            total_sdxfjxf += sdxfsxf_aomunt_total_agent

        total_data = {
            'total_dsje': self.format_money(total_dsje),
            'total_dssxf': self.format_money(total_dssxf),
            'total_sfje': self.format_money(total_sfje),
            'total_sfsxf': self.format_money(total_sfsxf),
            'total_sdxfje': self.format_money(total_sdxfje),
            'total_sdxfjxf': self.format_money(total_sdxfjxf),
            'total_incharge_amount': self.format_money(total_incharge_amount),
            'total_incharge_fee': self.format_money(total_incharge_fee),
        }
        return self.xtjson.json_result(data={'datas': datas, 'total_data': total_data, 'search_res': search_res})

    def search_merchant_func(self):
        merchant = request.args.get('merchant')
        dataDate = request.args.get('dataDate')
        search_type = request.args.get('search_type')
        datas = []
        search_res = {}
        filter_dict = {}
        if merchant and merchant.strip():
            filter_dict['$or'] = [{'merchant_id': merchant.strip()}, {'merchant_name': merchant.strip()}]
            search_res['merchant'] = merchant

        agentadmin_account = request.args.get('agentadmin_account')
        print('agentadmin_account:', agentadmin_account)
        if agentadmin_account and agentadmin_account.strip():
            agentadmin_data = CmsUserTable.find_one({'account': agentadmin_account.strip()})
            filter_dict['agentadmin_uuid'] = agentadmin_data.get('uuid')
            search_res['agentadmin_account'] = agentadmin_account

        if dataDate and dataDate.strip():
            start_time, end_time = PagingCLS.by_silce(dataDate)
        else:
            crrdate = datetime.datetime.now()
            start_time, end_time = datetime.datetime(crrdate.year, crrdate.month, crrdate.day, 0, 0, 0), datetime.datetime(crrdate.year, crrdate.month, crrdate.day, 23, 59, 59)
            dataDate = start_time.strftime('%Y-%m-%d %H:%M:%S') + '|' + end_time.strftime('%Y-%m-%d %H:%M:%S')

        crr_agentadmin_uuid = ''
        if self.current_admin_dict.get('role_code') == ROlE_ALL.AGENTADMIN:
            crr_agentadmin_uuid = self.current_admin_dict.get('uuid')
        elif self.current_admin_dict.get('role_code') == ROlE_ALL.SYSTEMUSER:
            filter_dict['agentadmin_uuid'] = self.current_admin_dict.get('agentadmin_uuid')
        if crr_agentadmin_uuid:
            filter_dict['agentadmin_uuid'] = crr_agentadmin_uuid

        # 代收金额
        total_dsje = 0
        # 代收手续费
        total_dssxf = 0
        # 代付金额
        total_sfje = 0
        # 代付手续费
        total_sfsxf = 0
        # 手动下发金额
        total_sdxfje = 0
        # 手动下发手续费
        total_sdxfjxf = 0
        # 统计商户结尾金额
        total_shjwje = 0
        #内部费用金额
        total_incharge_amount = 0
        #内部收费
        total_incharge_fee = 0

        search_res['dataDate'] = dataDate
        search_res['search_type'] = search_type
        
        mdatas = MerchantTable.find_many(filter_dict)
        agentadmin_datas = {}
        for mdata in mdatas:

            _dd = {
                'merchant_id': mdata.get('merchant_id'),
                'merchant_name': mdata.get('merchant_name'),
                # 'agentadmin_account': agentadmin_data.get('account') or '',
            }
            if self.current_admin_dict.get('role_code') in [ROlE_ALL.SUPERADMIN, ROlE_ALL.ADMINISTRATOR]:
                agentadmin_data = agentadmin_datas.get(mdata.get('agentadmin_uuid')) or {}
                if not agentadmin_data:
                    agentadmin_data = CmsUserTable.find_one({'uuid': mdata.get('agentadmin_uuid')}) or {}
                _dd['agentadmin_account'] = agentadmin_data.get('account') or ''

            # 代收金额
            fff1 = {
                'callback_time': {'$gte': start_time, '$lte': end_time},
                'pay_statu': True,
                'callback_statu': CallbackState.SUCCESS,
                'merchant_id': mdata.get('merchant_id'),
            }
            ds_aomunt_total_ll = CollectionOrderTable.collection().aggregate([
                {"$match": fff1},
                {"$group": {"_id": None, "actual_amount": {"$sum": '$actual_amount'}}},
            ])
            ds_aomunt_total = 0
            ds_aomunt_total_l = list(ds_aomunt_total_ll)
            if ds_aomunt_total_l:
                ds_aomunt_total = ds_aomunt_total_l[0].get('actual_amount')
            _dd['ds_aomunt_total'] = self.format_money(ds_aomunt_total)
            total_dsje += ds_aomunt_total

            # 代收手续费
            fff2 = {
                'callback_time': {'$gte': start_time, '$lte': end_time},
                'pay_statu': True,
                'merchant_id': mdata.get('merchant_id'),
                'callback_statu': CallbackState.SUCCESS,
            }
            dssuf_aomunt_total_ll = CollectionOrderTable.collection().aggregate([
                {"$match": fff2},
                {"$group": {"_id": None, "repay_amount": {"$sum": '$repay_amount'}}},
            ])
            dssxf_aomunt_total = 0
            dssuf_aomunt_total_l = list(dssuf_aomunt_total_ll)
            if dssuf_aomunt_total_l:
                dssxf_aomunt_total = dssuf_aomunt_total_l[0].get('repay_amount')
            _dd['dssxf_aomunt_total'] = self.format_money(dssxf_aomunt_total)
            total_dssxf += dssxf_aomunt_total

            # 代付金额
            fff3 = {
                'order_time': {'$gte': start_time, '$lte': end_time},
                'pay_statu': True,
                'merchant_id': mdata.get('merchant_id'),
            }
            df_aomunt_total_ll = behalfPayOrderTable.collection().aggregate([
                {"$match": fff3},
                {"$group": {"_id": None, "order_amount": {"$sum": '$order_amount'}}},
            ])
            df_aomunt_total = 0
            df_aomunt_total_l = list(df_aomunt_total_ll)
            if df_aomunt_total_l:
                df_aomunt_total = df_aomunt_total_l[0].get('order_amount')
            _dd['df_aomunt_total'] = self.format_money(df_aomunt_total)
            total_sfje += df_aomunt_total

            # 代付手续费
            fff4 = {
                'order_time': {'$gte': start_time, '$lte': end_time},
                'pay_statu': True,
                'merchant_id': mdata.get('merchant_id'),
            }
            dfsxf_aomunt_total_ll = behalfPayOrderTable.collection().aggregate([
                {"$match": fff4},
                {"$group": {"_id": None, "repay_amount": {"$sum": '$repay_amount'}}},
            ])
            dfsxf_aomunt_total = 0
            dfsxf_aomunt_total_l = list(dfsxf_aomunt_total_ll)
            if dfsxf_aomunt_total_l:
                dfsxf_aomunt_total = dfsxf_aomunt_total_l[0].get('repay_amount')
            _dd['dfsxf_aomunt_total'] = self.format_money(dfsxf_aomunt_total)
            total_sfsxf += dfsxf_aomunt_total

            # 手动下发
            fff5 = {
                'create_time': {'$gte': start_time, '$lte': end_time},
                'statu': WITHDRAW_STATUS.success,
                'merchant_uuid': mdata.get('uuid'),
            }
            sdxf_aomunt_total_ll = WithdrawTable.collection().aggregate([
                {"$match": fff5},
                {"$group": {"_id": None, "amount": {"$sum": '$amount'}}},
            ])
            sdxf_aomunt_total = 0
            sdxf_aomunt_total_l = list(sdxf_aomunt_total_ll)
            if sdxf_aomunt_total_l:
                sdxf_aomunt_total = sdxf_aomunt_total_l[0].get('amount')
            _dd['sdxf_aomunt_total'] = self.format_money(sdxf_aomunt_total)
            total_sdxfje += sdxf_aomunt_total

            # 手动下发手续费
            fff6 = {
                'create_time': {'$gte': start_time, '$lte': end_time},
                'statu': WITHDRAW_STATUS.success,
                'merchant_uuid': mdata.get('uuid'),
            }
            sdxfsxf_aomunt_total_ll = WithdrawTable.collection().aggregate([
                {"$match": fff6},
                {"$group": {"_id": None, "repay_amount": {"$sum": '$repay_amount'}}},
            ])
            sdxfsxf_aomunt_total = 0
            sdxfsxf_aomunt_total_l = list(sdxfsxf_aomunt_total_ll)
            if sdxfsxf_aomunt_total_l:
                sdxfsxf_aomunt_total = sdxfsxf_aomunt_total_l[0].get('repay_amount')
            _dd['sdxfsxf_aomunt_total'] = self.format_money(sdxfsxf_aomunt_total)
            total_sdxfjxf += sdxfsxf_aomunt_total

            #内部费用金额 内部收费
            fff7 = {
                'create_time': {'$gte': start_time, '$lte': end_time},
                'merchant_id': mdata.get('merchant_id'),
            }
            recharges = RechargeMoneyTable.find_many(fff7)
            internal_charge_amount = 0
            internal_fee_amount = 0
            for recharge in recharges:
                internal_charge_amount += recharge.get('amount')
                internal_fee_amount += recharge.get('repay_amount')

            _dd['internal_charge_amount'] = self.format_money(internal_charge_amount)
            _dd['internal_fee_amount'] = self.format_money(internal_fee_amount)
            total_incharge_amount += internal_charge_amount
            total_incharge_fee += internal_fee_amount

            end_mb_data = MerchantBillStatementTable.find_one({'merchant_uuid': mdata.get('uuid'), 'create_time': {'$gte': start_time, '$lte': end_time}}, sort=[['create_time', -1]]) or {}
            if not end_mb_data:
                end_mb_data = MerchantBillStatementTable.find_one({'merchant_uuid': mdata.get('uuid'), 'create_time': {'$lte': start_time}}, sort=[['create_time', -1]]) or {}
            if end_mb_data:
                _dd['end_balance_amount'] = self.format_money(end_mb_data.get('balance_amount') or 0)
            else:
                _dd['end_balance_amount'] = 0

            start_mb_data = MerchantBillStatementTable.find_one({'merchant_uuid': mdata.get('uuid'), 'create_time': {'$lt': start_time}},sort=[['create_time', -1]]) or {}
            if start_mb_data:
                _dd['start_balance_amount'] = self.format_money(start_mb_data.get('balance_amount') or 0)
            else:
                _dd['start_balance_amount'] = 0

            if str(ds_aomunt_total) == '0' and str(df_aomunt_total) == '0':
                continue

            # end_balance_amount = float(str(_dd.get('end_balance_amount')).replace(',',''))
            # start_balance_amount = float(str(_dd.get('start_balance_amount')).replace(',',''))
            # wc_vv = start_balance_amount + float(_dd.get('ds_aomunt_total').replace(',','')) - float(_dd.get('dssxf_aomunt_total').replace(',','')) - float(_dd.get('df_aomunt_total').replace(',', '')) - float(_dd.get('dfsxf_aomunt_total').replace(',','')) - float(_dd.get('sdxf_aomunt_total').replace(',','')) + float(_dd.get('sdxfsxf_aomunt_total').replace(',',''))
            # total_shjwje += end_balance_amount or 0

            end_balance_amount = float(str(_dd.get('end_balance_amount')).replace(',',''))
            start_balance_amount = float(str(_dd.get('start_balance_amount')).replace(',',''))
            wc_vv = start_balance_amount + float(_dd.get('ds_aomunt_total').replace(',','')) - float(_dd.get('dssxf_aomunt_total').replace(',','')) - float(_dd.get('df_aomunt_total').replace(',', '')) - float(_dd.get('dfsxf_aomunt_total').replace(',','')) - float(_dd.get('sdxf_aomunt_total').replace(',','')) + float(_dd.get('sdxfsxf_aomunt_total').replace(',','')) + float(_dd.get('internal_charge_amount').replace(',','')) - float(_dd.get('internal_fee_amount').replace(',',''))

            wc_vvv = end_balance_amount - (wc_vv or 0)
            if float(wc_vvv) == 0:
                wc_vvv = 0
            _dd['wc_vv'] = self.format_money(wc_vvv or 0)

            datas.append(_dd)

        total_data = {
            'total_dsje': self.format_money(total_dsje),
            'total_dssxf': self.format_money(total_dssxf),
            'total_sfje': self.format_money(total_sfje),
            'total_sfsxf': self.format_money(total_sfsxf),
            'total_sdxfje': self.format_money(total_sdxfje),
            'total_sdxfjxf': self.format_money(total_sdxfjxf),
            'total_shjwje': self.format_money(total_shjwje),
            'total_incharge_amount': self.format_money(total_incharge_amount),
            'total_incharge_fee': self.format_money(total_incharge_fee),
        }
        return self.xtjson.json_result(data={'datas': datas, 'total_data': total_data, 'search_res': search_res})

    def view_get(self):
        if self.is_xhr():
            return self.search_data_func()
        search_res = {}
        crrdate = datetime.datetime.now()
        start_time, end_time = datetime.datetime(crrdate.year, crrdate.month, crrdate.day, 0, 0, 0), datetime.datetime(crrdate.year, crrdate.month, crrdate.day, 23, 59, 59)
        dataDate = start_time.strftime('%Y-%m-%d %H:%M:%S') + '|' + end_time.strftime('%Y-%m-%d %H:%M:%S')
        search_res['dataDate'] = dataDate
        self.context['title'] = self.title
        self.context['search_res'] = search_res
        self.context['BILL_STATEMEN_TYPES'] = BILL_STATEMEN_TYPES
        
        html =  render_template(self.template, **self.context)
        return update_language(self.current_admin_dict.get("language"), html)


