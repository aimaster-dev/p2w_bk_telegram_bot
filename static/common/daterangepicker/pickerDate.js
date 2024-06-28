$.extend({
    // 年月日——时间
    picker_YY_HH_DD_HH_MM_SS: function (obj) {
        var _this = $(obj);
        _this.daterangepicker({
            opens:'left',
            timePicker: true,
            timePicker24Hour: true,
            autoApply: false,
            defaultDateRange: false,
            locale: {
                startDate: '',
                applyLabel: '确定',
                cancelLabel: '取消',
                separator: '|',
                format:'YYYY-MM-DD HH:mm:ss',
                daysOfWeek: ['日', '一', '二', '三', '四', '五', '六'],
                monthNames: ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'],
             }
        }, function (start, end, label) {});
    },
    // 年月日
    picker_YY_HH_DD: function (obj) {
        var _this = $(obj);
        _this.daterangepicker({
            opens:'left',
            locale: {
                applyLabel: '确定',
                cancelLabel: '取消',
                separator: '|',
                format:'YYYY-MM-DD',
                daysOfWeek: ['日', '一', '二', '三', '四', '五', '六'],
                monthNames: ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'],
             }
        }, function (start, end, label) {})
    },
    // 年月日(单选)
    single_YY_MM_DD: function (obj) {
        var _this = $(obj);
        b = new Date;
        var starYear = b.getFullYear() - 130 ;//最小选项
        var maxYear = b.getFullYear() + 20;//最大的选项
        _this.daterangepicker({
            opens:'left',
            singleDatePicker:true,
            showDropdowns:true,
            // minYear:1901,
            // maxYear: parseInt(moment().format('YYYY'),10),
            minYear :starYear,
            maxYear : maxYear,
            locale: {
                applyLabel: '确定',
                cancelLabel: '取消',
                format:'YYYY-MM-DD',
                daysOfWeek: ['日', '一', '二', '三', '四', '五', '六'],
                monthNames: ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'],
             }
        }, function (start, end, label) {})
    },
    // 单选时间
    single_time: function (obj) {
        var _this = $($.trim(obj));
        _this.daterangepicker({
            opens:'left',
            timePicker: true,
            timePicker24Hour: true,
            singleDatePicker:true,
            showDropdowns:true,
            minYear:1901,
            maxYear:parseInt(moment().format('YYYY'),10),
            locale: {
                firstDay: 1,
                applyLabel: '确定',
                cancelLabel: '取消',
                format:'YYYY-MM-DD HH:mm:ss',
                daysOfWeek: ['日', '一', '二', '三', '四', '五', '六'],
                monthNames: ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'],
             }
        }, function (start, end, label) {})
    }
});
