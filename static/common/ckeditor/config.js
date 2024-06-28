/**
 * @license Copyright (c) 2003-2020, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';

	config.toolbar = [
		[
		    'Source','Preview', 'Print','Undo', 'Redo','Find','Replace',
			'Bold', 'Underline','Format',
			'RemoveFormat','NumberedList', 'BulletedList',
			'Outdent', 'Indent','JustifyLeft', 'JustifyCenter', 'JustifyRight',
			'JustifyBlock','Link', 'Unlink', 'Anchor','Image','Table',
			'HorizontalRule', 'SpecialChar','FontSize',
			'TextColor', 'BGColor','Maximize', 'Html5video'
        ]
	];
	config.extraPlugins = 'html5video';
	config.filebrowserFlvPlayerUploadUrl = window.location.href;
	config.image_previewText=' ';
	config.filebrowserUploadUrl = window.location.href;
    config.filebrowserImageUploadUrl = window.location.href;
    config.filebrowserFlashUploadUrl = window.location.href;
};
