$(document).ready(function () {

    mediaTagId = null;

    url = window.location.pathname;
    url_data = url.split("/");
    if (url_data[2] == "posts" && url_data[4] == "change") {
        let postContent = $("#id_body").text();
        $("#postText").html(postContent);
    }


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


    $(".site-media").click(function () {
        mediaTagId = $(this).attr("id");
        $('.media-browser-modal').modal('show');
    });

    $(".modal-img").click(function () {
        let modal_image_id = $(this).attr('id');
        console.log("1"+mediaTagId);
        if(mediaTagId){
            if(mediaTagId == "site_logo"){
                console.log("1"+mediaTagId);
                $("#id_site_logo").val(modal_image_id);
                console.log("2"+$("#id_site_logo").val())
            }
            else if(mediaTagId == "site_favicon"){
                console.log(mediaTagId);
                $("#id_site_favicon").val(modal_image_id);
                console.log("3"+$("#id_site_favicon").val()); 
            }
            $('.media-browser-modal').modal('hide');
            mediaTagId = null;
            console.log("4"+mediaTagId);
        }
        else{
            
            $("#id_avatar").val(modal_image_id);
            $('.media-browser-modal').modal('hide');
        }
        
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
