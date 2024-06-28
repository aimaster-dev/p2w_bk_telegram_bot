/**
 * Created by Administrator on 2017/3/24.
 */

// 页面刷新, 用于图形验证码的点击切换,和排序,原理是刷新url
function refreshs_xtparam(refobj, keys) {
    var xtparam = {
        setParam: function (href,key,value) {
            var isReplaced = false;
            var urlArray = href.split('?');
            if(urlArray.length > 1){
                var queryArray = urlArray[1].split('&');
                for(var i=0; i < queryArray.length; i++){
                    var paramsArray = queryArray[i].split('=');
                    if(paramsArray[0] == key){
                        paramsArray[1] = value;
                        queryArray[i] = paramsArray.join('=');
                        isReplaced = true;
                        break;
                    }
                }
                if(!isReplaced){
                    var params = {};
                    params[key] = value;
                    if(urlArray.length > 1){
                        href = href + '&' + $.param(params);
                    }else{
                        href = href + '?' + $.param(params);
                    }
                }else{
                    var params = queryArray.join('&');
                    urlArray[1] = params;
                    href = urlArray.join('?');
                }
            }else{
                var param = {};
                param[key] = value;
                if(urlArray.length > 1){
                    href = href + '&' + $.param(param);
                }else{
                    href = href + '?' + $.param(param);
                }
            }
            return href;
        }
    };
    if(refobj=='' || typeof(refobj)=='undefined' || refobj=='undefined'){xtalert.alertError('请传入refobj！'); return }
    var lodsrc = refobj.attr('src');
    var keys = keys ? keys : '';
    var href = xtparam.setParam(lodsrc, keys, Math.random());
    refobj.attr('src',href);
}

// 关闭搜索
function exitsearch() {
    var c_url = window.location.href;
    var new_url = c_url.split('?')[0];
    window.location.href = new_url;
}

// 获取剪贴板内容
function get_clipboard_func() {
    navigator.clipboard.readText().then((v) => {
        return v;
    }).catch((v) => {
        return '';
    });
}

// 页面刷新
function reloadpage(redi_url,seconds) {
    if(redi_url=='' || typeof(redi_url)=='undefined' || redi_url=='undefined'){var redi_url = window.location.href}
    if(seconds=='' || typeof(seconds)=='undefined' || seconds=='undefined'){var seconds = 500}
    setTimeout(function (){window.location.href = redi_url;},seconds)
}

function clipboard_copy(data) {
    //控制剪贴板
    var text = document.createElement('textarea');
    text.value = data;
    document.body.appendChild(text);
    text.select();
    document.execCommand('Copy');
    text.remove();
    xtalert.alertSuccessToast('复制成功!');
}

// 禁用右键、文本选择功能、复制按键
function restrict_ban() {
    $(document).bind("contextmenu",function(){return false;});//禁止右键
    $(document).bind("selectstart",function(){return false;});//禁止选择
    document.onkeydown = function () {
        if (window.event && window.event.keyCode == 123) {
            event.returnValue = false;
            event.keyCode = 0;
            return false;
        }
    };
}

function _deletebyid(params) {
    xtajax.get({
        'url': params['get_url'],
        'data': {'action': params['action'], 'data_uuid': params['data_uuid']},
        'success': function (data) {
            if (data.code == 200) {
                xtalert.alertSuccessToast('删除成功');
                reloadpage(params['redi_url']);
            } else {
                xtalert.alertError(data.message);
            }
        }
    })
}

function delete_by_id(action,data_uuid,name,redi_url,get_url) {
    if (data_uuid=='' || typeof(data_uuid)=='undefined' || data_uuid=='undefined') {xtalert.alertError('要删除的ID不能为空!');return false}
    if (name=='' || typeof(name)=='undefined' || name=='undefined') {var msg='确定删除？'}else{var msg='确定删除:"'+name+'"吗?'}
    if (action ==  '' || typeof(action)=='undefined' || action=='undefined') {var action='del'}
    if (typeof(redi_url)=='undefined' || redi_url=='undefined') {var redi_url=''}
    if (typeof(get_url)=='undefined' || get_url=='undefined') {var get_url=''}
    xtalert.alertConfirm({'msg':msg,'confirmCallback':_deletebyid,'funcargs':{'data_uuid':data_uuid,'action':action,'redi_url':redi_url,'get_url':get_url}})
}

function _update_statu(params) {
    Swal({
        title: '',
        text: '请求中...',
        showCloseButton: false,
        showCancelButton: false,
        showconfirmButton: false,
        allowOutsideClick: false,
        onBeforeOpen: () => {
            Swal.showLoading()
        }
    });
    var method = params['method'];
    var ajax_params = {
        'url':params['get_url'],
        'data':{'data_uuid':params['data_uuid'],'action':params['action']},
        'success':function (data) {
            if(data.code==200){
                if (data.message){xtalert.alertSuccessToast(data.message);}else {xtalert.alertSuccessToast('操作成功');}
                if (params['redi_url']){reloadpage(params['redi_url']);}else {reloadpage();}
            }else{xtalert.alertError(data.message)}
        }
    };
    if(method=='post'){xtajax.post(ajax_params)}else{xtajax.get(ajax_params)}
}

function post_update_statu(action,data_uuid,msg,redi_url,get_url,method='post') {
    if (data_uuid=='' || typeof(data_uuid)=='undefined' || data_uuid=='undefined') {xtalert.alertError('要更新的ID不能为空!');return false}
    if (action=='' || typeof(action)=='undefined' || action=='undefined') {var action='statu'}
    if( typeof(redi_url)=='undefined' || redi_url=='undefined'){var redi_url = ''}
    if( typeof(get_url)=='undefined' || get_url=='undefined'){var get_url = ''}
    if( typeof(msg)=='undefined' || msg=='undefined'){var msg = '确定操作？'}
    xtalert.alertConfirm({'msg':msg,'confirmCallback':_update_statu,'funcargs':{'data_uuid':data_uuid,'action':action,'redi_url':redi_url,'get_url':get_url,'method': method}})
}

function _update(inputValue,params) {
    xtajax.post({
        'url':params['post_url'],
        'data':{'data_uuid':params['data_uuid'],'data_value':inputValue,'action':params['action']},
        'success':function (data) {
            if (data.code==200){
                if(data.message){xtalert.alertSuccess(data.message)}else{xtalert.alertSuccessToast('提交成功');}
                reloadpage(params['redi_url']);
            }else{xtalert.alertError(data.message)}
        }
    })
}

function updatetextarea(action,data_uuid,msg,redi_url,post_url,inputValue) {
    if (data_uuid=='' || typeof(data_uuid)=='undefined' || data_uuid=='undefined') {xtalert.alertError('数据UUID不能为空!');return false}
    if (action=='' || typeof(action)=='undefined' || action=='undefined') {xtalert.alertError('要更新的方法不能为空!');return false}
    if (typeof(msg)=='undefined' || msg=='undefined') {var msg=''}
    if (typeof(redi_url)=='undefined' || redi_url=='undefined') {var redi_url=''}
    if (typeof(post_url)=='undefined' || post_url=='undefined') {var post_url=''}
    if (typeof(inputValue)=='undefined' || inputValue=='undefined') {var inputValue=''}
    xtalert.alertOneTextarea({'title':'','text':msg,'confirmCallback':_update,'inputValue':inputValue,'funcargs':{'data_uuid':data_uuid,'redi_url':redi_url,'post_url':post_url,'action':action}})
}

function oneinput(action,data_uuid,title,placeholder,post_url,redi_url) {
    if (action=='' || typeof(action)=='undefined' || action=='undefined') {xtalert.alertError('要添加的方法不能为空!');return false}
    if (data_uuid=='' || typeof(data_uuid)=='undefined' || data_uuid=='undefined'){var data_uuid=''}
    if (typeof(title)=='undefined' || title=='undefined') {var title=''}
    if (typeof(redi_url)=='undefined' || redi_url=='undefined') {var redi_url=''}
    if (typeof(post_url)=='undefined' || post_url=='undefined') {var post_url=''}
    if (typeof(placeholder)=='undefined' || placeholder=='undefined') {var placeholder=''}
    xtalert.alertOneInput({'text':title, 'placeholder':placeholder, 'confirmCallback':_update,'funcargs':{'redi_url':redi_url,'post_url':post_url,'action':action,'data_uuid':data_uuid}})
}

// post提交数据处理方式
function post_data_way(params, showloading=false, loading_text='') {
    if (showloading){
        Swal({
            title: false,
            text: loading_text ? loading_text : '操作中，请稍等...',
            showCloseButton: false,
            showCancelButton: false,
            showconfirmButton: false,
            allowOutsideClick: false,
            onBeforeOpen: () => {
                Swal.showLoading();
            }
        });
    }
    xtajax.post({
        'url': params['url'] ? params['url'] : '',
        'data': params['data'],
        'success': function (data) {
            if (data.code == 200){
                if (params['successCallback']){
                    if (params['funcargs']){params['successCallback'](params['funcargs'])}else {params['successCallback']()}
                }else {
                    xtalert.alertSuccessToast();
                    reloadpage();
                }
            }else {
                if (params['failCallback']){
                    if (params['funcargs']){params['failCallback'](params['funcargs'])}else {params['failCallback']()}
                }else {
                    xtalert.alertError(data.message);
                }
            }
        }
    })
}

// 弹出请求数据
function alert_post_data(action, data_uuid, title, width) {
    if (!action){xtalert.alertError('提交类型不能为空!'); return }
    xtajax.post({
        'url': '',
        'data': {'action': action, 'data_uuid': data_uuid},
        'success': function (data) {
            if (data.code==200){
                var html = data.message;
                swal({
                    title: title ? title : '内容',
                    width: width ? width : 800,
                    html: html,
                    showCancelButton: false,
                    showConfirmButton: false,
                    allowOutsideClick: false,
                    showCloseButton: true,
                    allowEscapeKey: false
                })
            }else {
                xtalert.alertError(data.message);
            }
        }
    })
}

// 确认提交数据处理方式
function post_data_way_confirm(msg, params, confirm_func) {
    xtalert.alertConfirm({
        'msg':msg,
        'confirmCallback': confirm_func,
        'funcargs': params
    })
}

// 获取表单数据函数
function post_form_html(data, title, width, requestUrl='') {
    Swal({
        title: false,
        text: '数据请求中...',
        showCloseButton: false,
        showCancelButton: false,
        showconfirmButton: false,
        allowOutsideClick: false,
        onBeforeOpen: () => {
            Swal.showLoading()
        }
    });
    xtajax.post({
        'url': requestUrl,
        'data': data,
        'success':function (data) {
            if(data.code === 200){
                Swal({
                    title: title ? title : '操作',
                    width: width ? width : '',
                    html: data.message,
                    showCloseButton: true,
                    showCancelButton: false,
                    showConfirmButton: false,
                    allowOutsideClick: false,
                    allowEscapeKey: false,
                })
            }else{
                return xtalert.alertError(data.message);
            }
        }
    })
}
