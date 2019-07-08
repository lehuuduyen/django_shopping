$(document).on('submit', '#add-comment', function() {
    $.ajax({
        type: $(this).attr('method'),
        url: this.action,
        data: $(this).serialize(),
        context: this,
        success: function(data, status) {
            if (data == "True") {
                location.reload();
            }
        }
    });
    return false;
});


function click_reply(id) {

    alert(id)


}