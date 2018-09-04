$( document ).ready(function() {

    var url = new URLSearchParams(window.location.search);
    var id = null;

    if (url.has('sort_time')) setFilter('#time', url.get('sort_time'));
    if (url.has('sort_price')) setFilter('#price', url.get('sort_price'));

    function setFilterUrl(element) {
        var value = 'up';

        if (url.has(element)) {
            value = url.get(element);
            if (value === 'up') value = 'down';
            else if (value === 'down') value = 'up';
        }

        url.set(element, value);
        var parameterToRemove = 'sort_time';
        if (element === 'sort_time') parameterToRemove = 'sort_price';
        url.delete(parameterToRemove);
        window.location = '?' + url.toString()
    }

    function setFilter(element, value) {
        var icon = $(element + ' i');
        value = value || 'up';

        if (value === 'up'){
            icon.removeClass('fa-arrow-down').addClass('fa-arrow-up');
            $(element).addClass('fbold');
        } else if (value === 'down') {
            icon.removeClass('fa-arrow-up').addClass('fa-arrow-down');
            $(element).addClass('fbold');
        }
    }

    $('#time').click(function () {
        setFilterUrl('sort_time');
    });

    $('#price').click(function () {
        setFilterUrl('sort_price');
    });

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