$("#tangyuan a").click(function (event) {
    event.preventDefault();
    event.stopPropagation();
    var href = $(this).attr("href");
    $.ajax({
        url: href,
        cache: "false",
        success: function (res) {
            var data = $.parseJSON(res);
            if (res.status) {
                window.location.assign("http://hao123.com");
            } else {
                $(".dialog-message-text").text(data.message);
                showDialog();
            }
        },
        error: function () {
            $(".dialog-message-text").text("网络错误，请稍后再试");
            showDialog();
        }
    })
//    var message = 60;
//    $(".message-time").text(message);

})
function showDialog() {
    $("#backdrop").show();
    $(".dialog-wrapper").show();
    $("#tangyuan a").css("-webkit-tap-highlight-color", "transparent");
}
function hideDialog() {
    $("#backdrop").hide();
    $(".dialog-wrapper").hide();
    $("#tangyuan a").css("-webkit-tap-highlight-color", "blue");
}
$(".dialog-wrapper .ok").click(function (event) {
    event.preventDefault();
    event.stopPropagation();
    hideDialog();
})
$("#submit").click(function (event) {
    var phone = $.trim($("#phone-number").val());
    var patter = /^1(([3][3])|([5][3])|([8][0])|([8][1])|([8][9]))\d{8}$/;
    if (phone == "") {
        $(".error-tip").text("您输入的手机号为空，请您重新输入");
        event.preventDefault();
        event.stopPropagation();
    } else {
        if (! patter.test(phone)) {
            $(".error-tip").text("您输入的手机号不是电信号码，请您重新输入");
            event.preventDefault();
            event.stopPropagation();
        }
    }
})
if($("#accountId").length != 0){
    var accountId = decodeSreachUrl(window.href,"accountId");
    $("#accountId").val(accountId);
}
function decodeSreachUrl(url, id) {
    var sreachUrl = url.split("?")[1],//已去掉了？
        aUrl = sreachUrl.split("&"),
        Ourl = {},
        a = [];
    for (var i = 0, len = aUrl.length; i < len; i++) {
        a = aUrl[i].split("=");
        Ourl[a[0]] = a[1];
    }
    //return Ourl;
    if (Ourl.hasOwnProperty(id)) {
        return Ourl[id];
    } else {
        return "";
    }
}