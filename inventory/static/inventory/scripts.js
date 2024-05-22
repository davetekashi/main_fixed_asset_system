document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.item-form');
    const inputs = form.querySelectorAll('input, select');

    // Function to update input classes based on validity
    function updateInputClasses(input) {
        if (input.checkValidity()) {
            input.classList.remove('invalid');
            input.classList.add('valid');
        } else {
            input.classList.remove('valid');
            input.classList.add('invalid');
        }
    }

    // Attach input event listeners to all inputs
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            updateInputClasses(input);
        });
    });

    // Form submit event listener
    form.addEventListener('submit', function(event) {
        let allValid = true;
        inputs.forEach(input => {
            updateInputClasses(input);
            if (!input.checkValidity()) {
                allValid = false;
            }
        });
        if (!allValid) {
            event.preventDefault();
            alert('Please fill out all fields correctly.');
        }
    });
});
