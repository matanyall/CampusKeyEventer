$(document).ready( () => {
    // Bind "onclick" to hamburger
    $('#hamburger').bind('click', event => {
        // Set dropdown-container to display: block;
        $('#dropdown-container').slideToggle('fast');
    });

    $(document).on('click', event => {
        console.log(event.target);
        var drop = $('#hamburger');
        console.log(drop[0]);
        if (drop[0] !== event.target) {
            $('#dropdown-container').slideUp('fast');
        }
    });
});