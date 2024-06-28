from . import dbModel
from constants import ExportStatu



class ExportDataModel(dbModel):
    """导出数据"""
    __tablename__ = 'export_data_table'
    uuid = dbModel.UUIDField()
    filename = dbModel.StringField('文件名', nullable=False, is_index=True)
    path = dbModel.StringField('文件路径', nullable=False)
    file_size = dbModel.IntegerField('文件大小(KB)', nullable=False)
    total = dbModel.IntegerField('数据量', nullable=False)
    out_count = dbModel.IntegerField('已导出')
    statu = dbModel.DictField('导出状态', dict_cls=ExportStatu, nullable=False, btn_show=True, is_index=True)
    note = dbModel.StringField('备注')
    merchant_uuid = dbModel.StringField('商户UUID', is_index=True)
    agentadmin_uuid = dbModel.StringField('代理ID', is_index=True)

    @classmethod
    def field_search(cls):
        return ['statu', 'filename', 'create_time', 'note', 'merchant_uuid', 'agentadmin_uuid']

