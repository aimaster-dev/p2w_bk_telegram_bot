# -*- coding:utf-8 -*-
from views.cms_views import bp as cms_bp
from views.api_views import bp as api_bp
from views.front_views import bp as front_bp
from views.common_views import bp as common_bp
from views.merchant_view import bp as merchant_bp
from views.common_views.common_view import img_cap

from views.cms_views.cms_view import CmsIndexView, SettingView, TunnelView, BankScriptListView, SystemLogListView, VpnView, ExportFilesView, ApiLogView
from views.cms_views.cms_login import CmsLogin, CmsLoginOut
from views.cms_views.cms_user import UserListView
from views.cms_views.collect_view import BankCardView, BankView, ZaloListView, ViettelPayView, MomoView, BankCardBillLogView
from views.cms_views.finance_view import MerchantTunnleTotalView, ReconciliationView, BankcardFormView, MerchantBillFormView
from views.cms_views.merchant_view import MerchantListView, MerchantInfoView, OrderListView, MerchantReviewView, RechargeMoneyView, ReduceMoneyView, LoseOrderListView, WithdrawListView, \
    CallbackLogView, unknownIncomeView, MerchantFundsDetailView, AgentadminBillLogView, SubMerchantView
from views.cms_views.behalfPay_view import behalfPayOrderView, behalfPayCallbackLogView, behalfPayScriptView, behalfPayTaskView, behalfPayConfigView, CnBankCardView, WithdrawalBankCardView, TransactionFlowView


from views.front_views.front_view import FrontIndex, PayBankSelectView, DocView, PayBankView, PaySuccessView, PayOrderView

from views.merchant_view.login import MerchantLogin, MerchantLoginOut
from views.merchant_view.index_view import MerchantIndexView, MerchantUserView, MerchantBankCardView, MerchantOrderListView, MerchantBillStatementView, WithdrawApplyView, ExportDownload, MerchPayBehalfOrderView, MerchantReportView, SubAccountListView
from views.api_views.api_view import payApi, payOrderQuery, OrderPayTask, OrderQueryApi, behalfPayApi, behalfPayQueryApi, behalfPayTaskApi, BankBillLogApi, BankCardListApi



CMS_VIEWS = [
    CmsIndexView,
    CmsLogin, CmsLoginOut, SettingView, UserListView, BankCardView, SubMerchantView,
    MerchantListView, TunnelView, MerchantInfoView, OrderListView, MerchantReviewView, RechargeMoneyView, LoseOrderListView, WithdrawListView, ReduceMoneyView, CallbackLogView, unknownIncomeView, MerchantFundsDetailView,
    BankView, BankScriptListView, SystemLogListView, ZaloListView, ViettelPayView, MomoView, VpnView, BankCardBillLogView, ExportFilesView,
    MerchantTunnleTotalView, ReconciliationView, BankcardFormView, AgentadminBillLogView, MerchantBillFormView,
    behalfPayOrderView, behalfPayCallbackLogView, behalfPayScriptView, behalfPayTaskView, behalfPayConfigView, ApiLogView, CnBankCardView,WithdrawalBankCardView, TransactionFlowView
]

API_VIEWS = [
    payApi, payOrderQuery, OrderPayTask, OrderQueryApi, behalfPayApi, behalfPayQueryApi, behalfPayTaskApi, BankBillLogApi,BankCardListApi
]

FRONT_VIEWS = [
    FrontIndex, PayBankSelectView, DocView, PayBankView, PaySuccessView, PayOrderView
]

MERCHANT_VIEWS = [
    MerchantLogin, MerchantLoginOut, MerchantIndexView, MerchantUserView, MerchantBankCardView, MerchantOrderListView, MerchantBillStatementView, WithdrawApplyView, ExportDownload, MerchPayBehalfOrderView, MerchantReportView, SubAccountListView
]


ALL_VIEWS = {
    cms_bp: CMS_VIEWS,
    api_bp: API_VIEWS,
    front_bp: FRONT_VIEWS,
    merchant_bp: MERCHANT_VIEWS,
}


for _bp, vs in ALL_VIEWS.items():
    for view_cls in vs:
        if not hasattr(view_cls, 'add_url_rules'):
            continue
        if not getattr(view_cls, 'add_url_rules'):
            continue
        for rule in view_cls.add_url_rules:
            try:
                _bp.add_url_rule(rule[0], view_func=view_cls.as_view(rule[1]))
            except Exception as e:
                print(f'{view_cls.__name__}  error:', e)
                exit()

