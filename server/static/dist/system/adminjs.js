$(document).ready(function () {
    $("#psearch").keydown(function () {
        var host = $(location).attr('host');
        var purl = host + "/api/v1/public/posts";
        $.ajax({
            type: "get",
            url: purl,
            dataType: "json",
            success: function (result) {
                console.log(result);
            },
            error: function (error) {
                console.log("data pay na");
            }
        });

    });
});