function dumprogressbar() {
    document.writeln('<div class="progress">');
    document.writeln('<div id="progressbar" class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="min-width: 2em;width: 0%">');
    document.writeln('0%</div></div>');
}

function no_callbackfunc() {
    $("#showbar").hide()
}

function showprogress(evt) {
    var loaded = evt.loaded;
    var tot = evt.total;
    var percent = Math.floor(100*loaded/tot);
    var progressbar = $('#progressbar');
    progressbar.html(percent+'%');
    progressbar.attr('aria-valuenow',percent);
    progressbar.css('width',percent +'%');
}
function hideprogressbar() {
    var progressbar = $('#progressbar');
    progressbar.html('0%');
    progressbar.attr('aria-valuenow',0);
    progressbar.css('width','0%');
    $('#showbar').hide();
}

// upobj:触发对象; toobj:目标对象; types:类型方法; posturl:目标url; thumb_img:修改目标img的对象;
function upload_file(upobj,toobj,action,posturl,thumb_img,data_uuid,progress,callbackfunc) {
    if (typeof(upobj)=='undefined' || upobj=='undefined') {xtalert.alertErrorToast('upobj不能为空!');return false}
    if (action=='' || typeof(action)=='undefined' || action=='undefined') {var action='upimg'}
    if (typeof(toobj)=='undefined' || toobj=='undefined') {var toobj=''}
    if (typeof(posturl)=='undefined' || posturl=='undefined') {var posturl=''}
    if (typeof(thumb_img)=='undefined' || thumb_img=='undefined') {var thumb_img=''}
    if (typeof(data_uuid)=='undefined' || data_uuid=='undefined') {var data_uuid=''}
    if (typeof(progress)=='undefined' || progress=='undefined') {var progress=''}
    var imgpath = upobj.get(0).files[0];
    if(imgpath==''){
        xtalert.alertErrorToast('请选择文件！')
    }else{
        Swal({
            title: false,
            text: '数据提交中...',
            showCloseButton: false,
            showCancelButton: false,
            showconfirmButton: false,
            allowOutsideClick: false,
            onBeforeOpen: () => {
                Swal.showLoading()
            }
        });
        // 控制进度条
        if(progress=='progress'){$('#showbar').show(500);}
        var formdata = new FormData();
        formdata.append("upload",imgpath);
        formdata.append("action",action);
        formdata.append("data_uuid",data_uuid);
        params = {
            'url':posturl,
            'data':formdata,
            'contentType':false,
            'processData': false,
            'success':function (data) {
                if(data.code==200){
                    upobj.val('');
                    if(toobj){toobj.val(data.message);}
                    if(thumb_img){thumb_img.attr('src',data.message)}
                    if(callbackfunc){callbackfunc()}else{xtalert.alertSuccessToast('上传成功！');}
                }else{
                    xtalert.alertError(data.message)
                }
                 if(progress=='progress'){
                    hideprogressbar();
                }
            }
        };
        if(progress=='progress'){
            params['progress'] = showprogress;
        }
        xtajax.post(params);
    }
}

// 添加进度条添加方式
// <div id="showbar" style="display: none">
//     <script>dumprogressbar();</script>
// </div>
