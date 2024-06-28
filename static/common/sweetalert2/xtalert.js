/**
 * Created by Administrator on 2016/12/14.
 */

var xtalert = {
    /*
        功能：弹出toast（1s后消失）
        参数：
            - msg：提示消息
            - type：toast的类型
    */
    'alertToast':function (type, title, msg) {
        swal({
            'title': msg,
            'text': title,
            'type': type,
            'showCancelButton': false,
            'showConfirmButton': false,
            'timer': 1000,
        });
    },
    /*
        功能：信息toast提示（1s后消失）
        参数：
            - msg：提示消息
    */
    'alertInfoToast':function (msg) {
        this.alertToast('info', msg);
    },
    /*
        功能：成功toast提示（1s后消失）
        参数：
            - msg：提示消息
    */
    'alertSuccessToast':function (msg) {
        if(!msg){msg = '成功！';}
        this.alertToast('success', msg);
    },
    /*
        功能：错误toast提示（1s后消失）
        参数：
            - msg：提示消息
    */
    'alertErrorToast':function (msg) {
        this.alertToast('error', msg);
    },
    /*
        功能：网络错误提示
        参数：无
    */
    'alertNetworkErrorToast':function () {
        this.alertErrorToast('网络错误');
    },
    /*
        功能： 关闭弹窗
    */
    'close': function () {
        swal.close();
    },
    /*
        功能： 错误提示（确认后消失）
        参数：
            - msg：提示消息
    */
    'alertError': function (msg, title='') {
        swal(title, msg,'error');
    },
    /*
        功能： 预警提示（确认后消失）
        参数：
            - msg：提示消息
    */
    'alertInfo':function (msg, title='') {
        swal(title,msg,'warning');
    },
    /*
        功能： 成功提示（确认后消失）
        参数：
            - msg：提示消息
    */
    'alertSuccess': function (msg='操作成功!', title='') {
        swal(title, msg, 'success');
    },
    /*
        功能： 网络错误提示（确认后消失）
        参数：
            - msg: 提示内容
    */
    'alertQuestion': function (msg, title='') {
        swal(title, msg, 'question');
    },
    /*
        功能： 内容提示（确认后消失）
        参数：
            - msg：提示内容
    */
    'alertContent': function (content, title='') {
        // swal(title, content,);
        swal({
            'title': title,
            'text': content,
            'cancelButtonText': '关闭',
            'showCancelButton': true,
            'showConfirmButton': false,
        })
    },
    /*
        功能： input显示错误
        参数:
            -msg: 错误提示。
    */
    'showValidationError': function (msg) {
        swal.showValidationError(msg);
    },
    'alertSuccessWithCallback':function (msg,confirmCallback) {
        swal({'title': '', 'text': msg, 'type': 'success'}).then(
            function (result) {
                if(result.value){
                    confirmCallback()
                }
            }
        )
    },
    'alertInfoWithCallback':function (msg,confirmCallback) {
        swal({'title': '', 'text': msg, 'type': 'warning'}).then(
            function (result) {
                if(result.value){
                    confirmCallback()
                }
            }
        )
    },
    'alertSuccessWithTitle':function (title,msg) {
        swal(title,msg,'success');
    },
    'alertInfoWithTitle': function (title,msg) {
        swal(title,msg,'warning');
    },
    'alertErrorWithTitle': function (title,msg) {
        swal(title,msg,'error');
    },
    'alertContentWithTitle': function (title,content) {
        swal(title,content);
    },
    'alertContentInTextarea': function (content,title,text) {
        swal({
            'title': title ? title : '内容',
            'text': text ? text : '',
            'input':'textarea',
            'inputValue': content,
            'confirmButtonText': '关闭',
            'showConfirmButton': false,
            'showCloseButton': true,
            'inputClass':'font16'
        })
    },
    'alertImg':function (title,imgurl,imgwidth,imgheigth) {
        swal({
            'title': title ? title : '图片',
            'text':'',
            'imageUrl':imgurl,
            'imageWidth':imgwidth,
            'imageHeight':imgheigth,
            'cancelButtonText': '关闭',
            'showCancelButton': true,
            'showConfirmButton': false,
            'showCloseButton': true,
        });
    },
    'alertConfirm':function (params) {
        swal({
            'title': params['title'] ? params['title'] : '提示',
            'showCancelButton': true,
            'showConfirmButton': true,
            'type': params['type'] ? params['type'] : 'warning',
            'confirmButtonText': params['confirmText'] ? params['confirmText'] : '确定',
            'cancelButtonText': params['cancelText'] ? params['cancelText'] : '取消',
            'text': params['msg'] ? params['msg'] : '',
            'reverseButtons': true,
            'allowOutsideClick': false
        }).then(
            function (result) {
                if(result.value){
                    if(params['confirmCallback']){
                        if(params['funcargs']){params['confirmCallback'](params['funcargs'])}else{params['confirmCallback']()}
                    }
                }else{
                    if(params['cancelCallback']){
                        if(params['funcargs']){params['cancelCallback'](params['funcargs'])}else{params['cancelCallback']()}
                    }
                }
            }
        )
    },
    'alertOneInput': function (params) {
        if(params['inputValue']){
            var confirmButtonText = '修改';
            if(params['title']){
                var title = params['title']
            }else{
                var title = '原始内容';
            }
        }else{
            if(params['confirmText']){
                var confirmButtonText = params['confirmText']
            }else{
                var confirmButtonText = '确定';
            }
            if(params['title']){
                var title = params['title']
            }else{
                var title = ''
            }
        }
        swal({
            'title': title,
            'text': params['text'] ? params['text'] : '',
            'input':'text',
            'showCancelButton': true,
            'inputPlaceholder': params['placeholder'] ? params['placeholder'] : '',
            'inputValue': params['inputValue'] ? params['inputValue'] : '',
            'confirmButtonText': confirmButtonText,
            'cancelButtonText': params['cancelText'] ? params['cancelText'] : '取消',
            'inputValidator':function (value) {return !value && '输入框不能为空!'},
            'reverseButtons': true
        }).then(function (result) {
            if(result.value){
                if(params['confirmCallback']){
                    if(params['funcargs']){params['confirmCallback'](result.value,params['funcargs'])}else{params['confirmCallback'](result.value)}
                }
            }
        })
        ;
    },
    'alertOneTextarea': function (params) {
        if(params['inputValue']){
            var confirmButtonText = '修改';
            if(params['title']){
                var title = params['title']
            }else{
                var title = '原始内容';
            }
        }else{
            if(params['confirmText']){
                var confirmButtonText = params['confirmText']
            }else{
                var confirmButtonText = '确定'
            }
            if(params['title']){
                var title = params['title']
            }else{
                var title = ''
            }
        }
        swal({
            'title': title,
            'text': params['text'] ? params['text'] : '',
            'input':'textarea',
            'showCancelButton': true,
            'inputPlaceholder': params['placeholder'] ? params['placeholder'] : '',
            'inputValue': params['inputValue'] ? params['inputValue'] : '',
            'confirmButtonText': confirmButtonText,
            'cancelButtonText': params['cancelText'] ? params['cancelText'] : '取消',
            'inputValidator':function (value) {return !value && '输入框不能为空!'},
            'reverseButtons': true
        }).then(function (result) {
            if(result.value){
                if(params['confirmCallback']){
                    if(params['funcargs']){params['confirmCallback'](result.value,params['funcargs'])}else{params['confirmCallback'](result.value)}
                }
            }
        });
    },

    /* 微信支付宝支付*/
    'alertPayment':function (conten) {
        swal({
            'title': '',
            'html':conten,
            'animation':'slide-from-top',
            'showCancelButton': false,
            'showConfirmButton': false,
            'allowOutsideClick':true,
        });
    }
};


/*
SweetAlert2 参数:
title: 标题，
text： 文本，
type： 弹窗类型（success(成功)、error(错误)、warning(警告)、info(提示)、question(提问)）
showCancelButton：是否显示“Cancel（取消）”按钮。 true/false
showConfirmButton：是否显示“Confirm（确认）”按钮。true/false
confirmButtonText：确认按钮上的文本。
cancelButtonText：取消按钮上的文本。
confirmButtonColor：确认按钮颜色。
html： 自定义html，
animation： 是否显示动画效果，默认true。
reverseButtons：反转两个按钮的位置， 左边 确定  右边 取消
position：模态框的位置（ 'top', 'top-start', 'top-end', 'center', 'center-start', 'center-end', 'bottom', 'bottom-start', or 'bottom-end'.）
timer： 显示时间 1000
footer： 脚页
backdrop： 是否显示遮罩层，默认true,
background: 背景颜色。
allowOutsideClick:是否允许点击对话框外部来关闭对话框。
allowEscapeKey:是否允许按下Esc键来关闭对话框。

swal.showValidationError('修改出错！')
*/
