// $(document).ready(function () {
//     $("#psearch").keydown(function () {
//         var host = $(location).attr('host');
//         var purl = host + "/api/v1/public/posts";
//         $.ajax({
//             type: "get",
//             url: purl,
//             dataType: "json",
//             success: function (result) {
//                 console.log(result);
//             },
//             error: function (error) {
//                 console.log("data pay na");
//             }
//         });

//     });
// });
http://127.0.0.1:8000/cms/posts/
var app5 = new Vue({
    el: '#cms',
    data: {
        host: location.host,
        public_api: "/api/v1/public/"
    },
    methods: {
        getPostList() {
            axios
                .get('http://' + this.host + this.public_api + "posts/")
                .then(response => (
                    console.log(response.data)
                ))
                .catch(error => console.log(error))
        },
        postSearch: function () {
            console.log("Working..");
            console.log(this.host);

        }
    },
    mounted() {
        this.getPostList();
    },
})