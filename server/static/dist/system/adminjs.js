$(document).ready(function () {
    $(".user-select").change(function(){
        console.log("Working..");
        let apiUrl = "http://127.0.0.1:8000/api/v1/public/categories/";
        $.ajax({url: apiUrl, success: function(result){
            console.log(result);
        }, error: function(error){
            console.log(error);
        }})
    });
});
