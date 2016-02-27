$(function(){
    $('[id^="error_"]').siblings('input').focus(function(){
        var elem = $(this).parents('.form-group');
        elem.find('.form-control-feedback').remove();
        elem.removeClass('has-error has-feedback');
        elem.find('.text-danger').remove();
    });
});
