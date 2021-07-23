$(document).ready( () => {
    $('#suggested-tab').on('click', event => {
        $('#all-events').css('display', 'none');
        $('#my-events').css('display', 'none');
        $('#suggested-events').css('display', 'block');
    });

    $('#all-tab').on('click', event => {
        $('#all-events').css('display', 'block');
        $('#my-events').css('display', 'none');
        $('#suggested-events').css('display', 'none');
    });

    $('#my-tab').on('click', event => {
        $('#all-events').css('display', 'none');
        $('#my-events').css('display', 'block');
        $('#suggested-events').css('display', 'none');
    });

    $('.cornhusking').toArray().forEach(elem => {
        $(elem).on('click', event => {
            window.location.replace('/events/cornhusking');
        });
    });

    $('#register-btn').on('click', event => {
        console.log('hello');
        $('#register-page').css('display', 'none');
        $('#registered-page').css('display', 'flex');
    });

    $('#view-registration-btn').on('click', event => {
        window.location.replace('/events/cornhusking/qr');
    })
});