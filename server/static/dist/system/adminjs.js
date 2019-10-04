$(document).ready(function () {
    $(".user-select").change(function () {
        console.log("Working..");
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
        console.log(modal_image_id);
        $("#id_avatar").val(modal_image_id);
        $('.media-browser-modal').modal('hide');
    })
});
