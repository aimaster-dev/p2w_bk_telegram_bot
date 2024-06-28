/**
 * Created by Administrator on 2016/12/14.
 */
// 对jquery的ajax的封装

'use strict';

var xtajax = {
	'get':function(args) {
		args['method'] = 'get';
		this.ajax(args);
	},
	'post':function(args) {
		args['method'] = 'post';
		args['dataType'] = 'json';
		if(args['progress']){
			args['xhr'] = function(){
	　　　　　　var xhr = $.ajaxSettings.xhr();
	　　　　　　if(args['progress'] && xhr.upload) {
	　　　　　　　　xhr.upload.addEventListener("progress" , args['progress'], false);
	　　　　　　　　return xhr;
	　　　　　　}
	　　　　}
		}
		this.ajax(args);
	},
	'ajax':function(args) {
		// 设置csrftoken
		this._ajaxSetup();
		$.ajax(args);
	},
	'_ajaxSetup': function() {
		$.ajaxSetup({
			'beforeSend':function(xhr,settings) {
				if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    var csrftoken = $('meta[name=csrf-token]').attr('content');
                    xhr.setRequestHeader("X-CSRFToken", csrftoken)
                }
			}
		});
	}
};
