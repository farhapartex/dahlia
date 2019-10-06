$(document).ready(function () {
    $(".user-select").change(function () {
        let apiUrl = "http://127.0.0.1:8000/api/v1/public/categories/";
        $.ajax({
            url: apiUrl, success: function (result) {
                console.log(result);
            }, error: function (error) {
                console.log(error);
            }
        })
    });


    $(".modal-img").click(function () {
        let modal_image_id = $(this).attr('id');
        $("#id_avatar").val(modal_image_id);
        $('.media-browser-modal').modal('hide');
    });

    $(".objDelete").click(function () {
        var id = $(this).attr("id");
        var href = $(this).attr("href");
        // var href = "/cms/categories/"+ id +"/delete/";
        $('#alertModal').modal('show');
        $(".cateDelete").attr("href", href);
        return false;
    });

    $("#postText").keyup(function () {
        let postContent = $(this).html();
        $("#id_body").text(postContent);
    });
});
