/*
window.onload = function () {

    var scroll_top = 0;
    window.onscroll = function () {
        scroll_top = scroll().top;

        scroll_top > 0 ? show($("to_top")) : hide($("to_top"));
    }

    $("#to_top").click(function(e) {
       TweenMax.to(window, 1.5, {scrollTo:0, ease: Expo.easeInOut});

       var huojian = new TimelineLite();
    	huojian.to("#to_top", 1, {rotationY:720, scale:0.6, y:"+=40", ease:  Power4.easeOut})
    	.to("#to_top", 1, {y:-1000, opacity:0, ease:  Power4.easeOut}, 0.6)
    	.to("#to_top", 1, {y:0, rotationY:0, opacity:1, scale:1, ease: Expo.easeOut, clearProps: "all"}, "1.4");

     });

    /*
    var scroll_top = 0, begin = 0, end = 0, timer = null;

    window.onscroll = function () {
        scroll_top = scroll().top;

        scroll_top > 0 ? show($("to_top")) : hide($("to_top"));
        begin = scroll_top;
    }

    $("to_top").onclick = function () {
        clearInterval(timer);

        timer = setInterval(function () {
            begin = begin + (end - begin) / 10;
            window.scrollTo(0, begin);

            if (parseInt(begin) === end){
                clearInterval(timer);
            }

        }, 20);
    }
    */
};
*/
function $(id) {
    return typeof id === "string" ? document.getElementById(id) : null;
}

function show(obj) {
    return obj.style.display = "block";
}

function hide(obj) {
    return obj.style.display = "none";
}

function scroll() {
    if (window.pageXOffset !== null){
        return{
            top: window.pageYOffset,
            left: window.pageXOffset
        }
    }else if (document.compatMode === "CSSCompat"){
        return{
            top: document.documentElement.scrollTop,
            left: document.documentElement.scrollLeft
        }
    }

    return{
        top: document.body.scrollTop,
        left: document.body.scrollLeft
    }

}
