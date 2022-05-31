$(document).ready(function(){

    var baseurl = 'http://127.0.0.1:8000/contas-pagar/';
    var filter = $('#filter');

    $(filter).change(function(){
        var filter = $(this).val();
        /*window.location.href = baseurl + '?filter=' + filter;*/
        console.log(filter);
    });
    
});