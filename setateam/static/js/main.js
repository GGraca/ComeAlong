$(document).ready(function () {
    $('.backtotop').click(function () {
        $('body,html').animate({
            scrollTop:0
        }, 1200);
        return false;
    });
});

$(document).on("scroll",function(){
    if($(document).scrollTop()>300){
        //$("#top-bar").addClass("small");
        $(".backtotop").removeClass("hidden")
    } else{
        //$("#top-bar").removeClass("small");
        $(".backtotop").addClass("hidden")
    }     
});
