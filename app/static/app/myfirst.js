
document.addEventListener('DOMContentLoaded', function() {
    const submit = document.querySelector('#submit-post');
    const newTitle = document.querySelector('#title_form');
    submit.disabled = true;
     // Listen for input to be typed into the input field
    newTitle.onkeyup = () => {
        if(newTitle.value.length > 0)
        {
            submit.disabled = false;
        }
        else{
            submit.disabled = true;
        
         }
    }

    // Listen for submission of form
    document.querySelector('form').onsubmit = () => {

        
        newTitle.value = '';

        // Disable the submit button again:
        submit.disabled = true;

        // Stop form from submitting
        return false;
    }
});