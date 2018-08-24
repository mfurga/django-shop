$( document ).ready(function() {

    var url = new URLSearchParams(window.location.search);
    var id = null;

    if (url.has('category')) {
        id = url.get('category');
        var category = $('#cat-' + id);
        var categoryName = category.find('.icon-title').text();

        category.addClass('active');
        $("#active a").text(categoryName).attr('href', '?category=' + id);
        $("#active").show();
    } 

    $("li[id*='cat-']").click(function() {
        $("li[id*='cat-']").removeClass('active');
        $(this).addClass('active');
        id = $(this).attr('id').replace(/[^0-9]/g, '');
    });

    $('#form').submit(function() {
        var input = $("<input>")
               .attr("type", "hidden")
               .attr("name", "category").val(id);
        $(this).append(input);

        $(this).find(":input").filter(function(){ return !this.value; }).attr("disabled", "disabled");

    });
})