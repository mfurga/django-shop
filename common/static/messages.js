$( document ).ready(function () {
    $('#alert').fadeOut(7000);
    $('.closebtn').click(function (){
        $('#alert').remove();
    });
});