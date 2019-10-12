$(document).ready(function () {

    mediaTagId = null;

    url = window.location.pathname;
    url_data = url.split("/");
    if (url_data[2] == "posts" && url_data[4] == "change") {
        let postContent = $("#id_body").text();
        $("#postText").html(postContent);
    }


    $(".user-select").change(function () {
        let host = window.location.host
        let apiUrl = host +"/api/v1/public/categories/";
        if(host == "localhost:8000" || host == "127.0.0.1:8000"){
            apiUrl = "http://" + apiUrl;
        }
        else{
            apiUrl = "https://" + apiUrl;
        }
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

    $("#select_all_cat").click(function () {
        if ($('#select_all_cat').prop('checked')){
            $('.cat_check').prop('checked', true);
        }
        else{
            $('.cat_check').prop('checked', false);
        }

        // $('.cat_check').prop('checked', false);
        
    });


    $(".action-select").change(function () {
        if($(this).val() == "delete"){

            $('input:checkbox.cat_check').each(function () {
                if(this.checked){
                    let id = $(this).val();
                    let host = window.location.host
                    let apiUrl = host + window.location.pathname + id + "/delete/";
                    if(host == "localhost:8000" || host == "127.0.0.1:8000"){
                        apiUrl = "http://" + apiUrl;
                    }
                    else{
                        apiUrl = "https://" + apiUrl;
                    }
                    $.ajax({
                        url: apiUrl, success: function (result) {
                            console.log(result);
                            
                        }, error: function (error) {
                            console.log(error);
                        }
                    });
                    window.location.reload();
                }
           });
        }
    });
});