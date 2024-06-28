$(document).ready(function () {

    // 当前菜单定位
    var a_tags = $("#sidebar").find("a");
    a_tags.each(function(index, data){
        if (window.location.pathname === $(this).attr('href')){
            $(this).addClass('active');
            $(this).siblings().removeClass("active");
            if ($(this).parent().prev().attr('datatype') === 'menu-group'){
                $(this).parent().slideDown(0);
                $(this).parent().prev().find(".icon-fangxiangxia").removeClass("icon-fangxiangxia").addClass("icon-fangxiangshang");
            }
        }
    });

    $("#sidebar a").on('click', function () {
        if ($(this).attr('datatype') === 'menu-group'){
            if ($(this).next().css('display') === 'none'){
                $(this).find(".icon-fangxiangxia").removeClass("icon-fangxiangxia").addClass("icon-fangxiangshang");
                $(this).next().slideDown();
            }else{
                $(this).find(".icon-fangxiangshang").removeClass("icon-fangxiangshang").addClass("icon-fangxiangxia");
                $(this).next().slideUp(100);
            }
        }
    })

    // 日期选择器
    $.picker_YY_HH_DD_HH_MM_SS('.pickerdate');

    // 初始化侧边栏
    if ($(window).width() > 990){
        $("#header").css('left', '210px');
        $("#sidebar").css('left', '0');
        $("#content_box").css('margin-left', '210px');
    }else {
        $("#header").css('left', '0');
        $("#sidebar").css('left', '-300px');
        $("#content_box").css('margin-left', '0');
    }

    // 搜索按钮
    var _page_url = window.location.href;
    if (_page_url.split("?").length > 1){
        var _search_btn_statu = true;
    }else {
        var _search_btn_statu = false;
    }
    $(".search_dispose_btn").each(function (index, data) {
        if (_search_btn_statu){$(this).show(0)}else {$(this).hide(0)}
    })

})

// 菜单开关切换
function menu_operation(obj) {
    if (obj.attr('datatype')=='menu-group') {
        if (obj.next().css('display') == 'none') {
            obj.next().slideDown(300);
            obj.find('.bi-chevron-down').removeClass('bi-chevron-down').addClass('bi-chevron-left');
        } else {
            obj.next().slideUp(300);
            obj.find('.bi-chevron-left').removeClass('bi-chevron-left').addClass('bi-chevron-down');
        }
    }
}

// 控制侧边栏
function sidebar_toggle() {
    if ($(window).width() > 990){
        if ($("#sidebar").css('left')=='0px'){
            $("#sidebar").css('left', '-210px');
            $("#header").css('left', '0');
            $("#content_box").css('margin-left', '0');
        } else {
            $("#sidebar").css('left','0px');
            $("#header").css('left','210px');
            $("#content_box").css('margin-left','210px');
        }
    }else {
        if ($("#sidebar").css('left')=='0px'){
            $("#sidebar").css('left', '-300px');
            $("#header").css('left', '0');
            $("#content_box").css('margin-left', '0');
        } else {
            $("#sidebar").css('left','0px');
            $("#header").css('left','210px');
            $("#content_box").css('margin-left','210px');
        }
    }
}

// var As=document.getElementById('sidebar_menus').getElementsByTagName('a');
// for(let i=0; i<As.length; i++){
//     let current_a = As[i];
//     if(window.location.href.indexOf(current_a.href)>=0){
//         current_a.parentNode.className = 'active';
//         break
//     }
// }
