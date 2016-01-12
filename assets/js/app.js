/**
 * Created by Job on 12/6/2015.
 */
$(function () {
    $('.text_area').ckeditor(
        {
            skin:'flat',
            removePlugins : 'elementspath'
        }
    );
    $("#owl-example").owlCarousel();
});
