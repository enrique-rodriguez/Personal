
function sendMessage(token) {
    let thisForm = document.querySelector('.email-form');
    let formData = new FormData( thisForm );
    let action = thisForm.getAttribute('action');

    thisForm.querySelector('.loading').classList.add('d-block');
    thisForm.querySelector('.error-message').classList.remove('d-block');
    thisForm.querySelector('.sent-message').classList.remove('d-block');

    formData.set('recaptcha-response', token);
    email_form_submit(thisForm, action, formData);
}

function email_form_submit(thisForm, action, formData) {
    fetch(action, {
        method: 'POST',
        body: formData,
    }).then(response => {
        if( response.ok || response.status == 400 ) return response.json();
        else throw new Error('Message could not be sent. Please try again later.');
    }).then(data => {
        thisForm.querySelector('.loading').classList.remove('d-block');
        if ( !('error' in data ) ) {
            thisForm.querySelector('.sent-message').classList.add('d-block');
            thisForm.reset();
        } else throw new Error(data.detail);
    }).catch(error => displayError(thisForm, error));
}

function displayError(thisForm, error) {
    thisForm.querySelector('.loading').classList.remove('d-block');
    thisForm.querySelector('.error-message').innerHTML = error;
    thisForm.querySelector('.error-message').classList.add('d-block');
}