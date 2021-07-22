$(document).ready( () => {
    // Bind "onclick" to hamburger
    $('#hamburger').bind('click', event => {
        // Set dropdown-container to display: block;
        $('#dropdown-container').slideToggle('fast');
    });

    $(document).on('click', event => {
        let drop = $('#hamburger');
        if ((drop[0] != event.target) && (drop.children().filter(child => child[0] == event.target).length === 0)) {
            $('#dropdown-container').slideUp('fast');
        }
    });

    // $(".dropdown-item").toArray().forEach(item => {
    //     $(item).on('mousedown', event => {
    //         console.log(event.target);
    //         $(event.target).parent().css('background-color', '#FFF1F1');
    //     });
    // });
});