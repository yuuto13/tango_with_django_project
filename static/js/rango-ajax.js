$(document).ready(function () {

    $('#like_btn').click(function() {
        let categoryid = $(this).attr('data-categoryid');

        $.get("/rango/like_category/", {'category_id': categoryid}, data => {
            $('#like_count').html(data);
            $('#like_btn').hide();
        });
    });

    $('#search-input').keyup(function() {
        let query;
        query = $(this).val();

        $.get("/rango/suggest/", {'suggestion': query}, data => {
            $('#categories-listing').html(data);
            feather.replace();
        });
    });

    $('.rango-page-add').click(function() {
        let categoryid = $(this).attr('data-categoryid');
        let title = $(this).attr('data-title');
        let url = $(this).attr('data-url');

        send_items = {'category_id': categoryid, 'title': title, 'url': url};

        $.get("/rango/search_add_page/", send_items, data => {
            $('#pages-listing').html(data);
            $(this).hide();
        });
    });

});