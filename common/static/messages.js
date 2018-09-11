$( document ).ready(function () {
    $('#alert').fadeOut(4000);
    $('.closebtn').click(function (){
        $('#alert').remove();
    });
});