$(window).on("scroll", function () {
    if ($(this).scrollTop() > 100) {
        $('#responsive').addClass("custom_fix_menu");
    } else {
        $('#responsive').removeClass("custom_fix_menu");
    }
});

$(window).load(function () {
    if ($(this).scrollTop() > 100) {
        $('#responsive').addClass("custom_fix_menu");
    } else {
        $('#responsive').removeClass("custom_fix_menu");
    }
});