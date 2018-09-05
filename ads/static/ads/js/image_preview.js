$(document).ready(function () {

    function preview(input) {
        if(input.files && input.files[0]) {
            var reader = new FileReader();

            var id = $(input).attr('id').replace(/[^0-9]/g, '');
            var label = '#label' + id;

            reader.onload = function (ev) {
                $(label).css({
                    'background-image': 'url(' + ev.target.result + ')',
                    'background-repeat': 'no-repeat',
                    'background-size': 'contain',
                    'background-position': 'center'
                }).empty();
            };

            reader.readAsDataURL(input.files[0]);
        }
    }

    $(".photo").change(function () {
        preview(this);
    })

});