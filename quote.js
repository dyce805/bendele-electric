/**
 * Bendele Electric - Quote Form Handler
 * Handles form validation and EmailJS submission
 */

// Initialize EmailJS
emailjs.init('mzrX2T3SvfkbAxGZ6');

// Wait for DOM to be ready
document.addEventListener('DOMContentLoaded', function() {
    
    // Prefill property type from URL parameter
    const urlParams = new URLSearchParams(window.location.search);
    const propertyTypeParam = urlParams.get('type');
    
    // Show/hide "Other" property field based on selection
    const propertyTypeSelect = document.getElementById('propertyType');
    const otherPropertyGroup = document.getElementById('otherPropertyGroup');
    const otherPropertyInput = document.getElementById('otherProperty');

    // If URL parameter exists and is valid, prefill the select
    if (propertyTypeParam && ['residential', 'commercial', 'industrial', 'other'].includes(propertyTypeParam)) {
        propertyTypeSelect.value = propertyTypeParam;
        // Trigger change event in case 'other' is selected
        if (propertyTypeParam === 'other') {
            otherPropertyGroup.style.display = 'block';
            otherPropertyInput.required = true;
        }
    }

    propertyTypeSelect.addEventListener('change', function() {
        if (this.value === 'other') {
            otherPropertyGroup.style.display = 'block';
            otherPropertyInput.required = true;
        } else {
            otherPropertyGroup.style.display = 'none';
            otherPropertyInput.required = false;
            otherPropertyInput.value = '';
            clearFieldError(otherPropertyInput);
        }
    });

    // Set minimum date to today for completion date
    const completionDateInput = document.getElementById('completionDate');
    const today = new Date().toISOString().split('T')[0];
    completionDateInput.setAttribute('min', today);

    // Form elements
    const form = document.getElementById('quoteForm');
    const submitButton = form.querySelector('button[type="submit"]');

    // Validation patterns
    const patterns = {
        phone: /^[\d\s\-\(\)\+\.]{10,}$/,
        email: /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    };

    // Error message display functions
    function showFieldError(field, message) {
        clearFieldError(field);
        field.classList.add('form-input--error');
        const errorDiv = document.createElement('div');
        errorDiv.className = 'form-error';
        errorDiv.textContent = message;
        field.parentNode.appendChild(errorDiv);
    }

    function clearFieldError(field) {
        field.classList.remove('form-input--error');
        const existingError = field.parentNode.querySelector('.form-error');
        if (existingError) {
            existingError.remove();
        }
    }

    function clearAllErrors() {
        document.querySelectorAll('.form-error').forEach(el => el.remove());
        document.querySelectorAll('.form-input--error').forEach(el => {
            el.classList.remove('form-input--error');
        });
    }

    // Sanitize input to prevent XSS
    function sanitizeInput(str) {
        if (typeof str !== 'string') return '';
        return str
            .trim()
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#x27;');
    }

    // Validate individual fields
    function validateField(field) {
        const value = field.value.trim();
        const fieldName = field.name;

        // Required field check
        if (field.required && !value) {
            const label = field.parentNode.querySelector('.form-label')?.textContent.replace('*', '').trim() || fieldName;
            showFieldError(field, `${label} is required`);
            return false;
        }

        // Skip further validation if empty and not required
        if (!value) {
            clearFieldError(field);
            return true;
        }

        // Specific field validations
        switch (fieldName) {
            case 'email':
                if (!patterns.email.test(value)) {
                    showFieldError(field, 'Please enter a valid email address');
                    return false;
                }
                break;
            case 'phone':
                if (!patterns.phone.test(value)) {
                    showFieldError(field, 'Please enter a valid phone number (at least 10 digits)');
                    return false;
                }
                break;
            case 'name':
                if (value.length < 2) {
                    showFieldError(field, 'Name must be at least 2 characters');
                    return false;
                }
                if (value.length > 100) {
                    showFieldError(field, 'Name must be less than 100 characters');
                    return false;
                }
                break;
            case 'serviceAddress':
                if (value.length < 5) {
                    showFieldError(field, 'Please enter a complete address');
                    return false;
                }
                break;
            case 'workType':
                if (value.length < 3) {
                    showFieldError(field, 'Please provide more detail about the work needed');
                    return false;
                }
                break;
            case 'completionDate':
                const selectedDate = new Date(value);
                const todayDate = new Date();
                todayDate.setHours(0, 0, 0, 0);
                if (selectedDate < todayDate) {
                    showFieldError(field, 'Please select a future date');
                    return false;
                }
                break;
        }

        clearFieldError(field);
        return true;
    }

    // Real-time validation on blur
    form.querySelectorAll('.form-input, .form-select, .form-textarea').forEach(field => {
        field.addEventListener('blur', function() {
            // Mark field as touched for CSS validation styling
            this.classList.add('touched');
            validateField(this);
        });

        // Also mark as touched on change (for select and date inputs)
        field.addEventListener('change', function() {
            this.classList.add('touched');
            validateField(this);
        });

        // Clear error when user starts typing
        field.addEventListener('input', function() {
            if (this.classList.contains('form-input--error')) {
                clearFieldError(this);
            }
        });
    });

    // Form submission handler
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        clearAllErrors();

        // Validate all fields
        let isValid = true;
        const fields = form.querySelectorAll('.form-input, .form-select, .form-textarea');
        
        fields.forEach(field => {
            // Skip hidden fields
            if (field.offsetParent === null && field.id !== 'otherProperty') {
                return;
            }
            // For otherProperty, only validate if visible
            if (field.id === 'otherProperty' && otherPropertyGroup.style.display === 'none') {
                return;
            }
            if (!validateField(field)) {
                isValid = false;
            }
        });

        if (!isValid) {
            // Scroll to first error
            const firstError = form.querySelector('.form-input--error');
            if (firstError) {
                firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
                firstError.focus();
            }
            return;
        }

        // Disable submit button and show loading state
        submitButton.disabled = true;
        const originalText = submitButton.textContent;
        submitButton.textContent = 'Submitting...';

        try {
            // Collect and sanitize form data
            const formData = {
                name: sanitizeInput(document.getElementById('name').value),
                phone: sanitizeInput(document.getElementById('phone').value),
                email: sanitizeInput(document.getElementById('email').value),
                contactMethod: document.getElementById('contactMethod').value,
                serviceAddress: sanitizeInput(document.getElementById('serviceAddress').value),
                propertyType: document.getElementById('propertyType').value,
                otherProperty: sanitizeInput(document.getElementById('otherProperty').value),
                workType: sanitizeInput(document.getElementById('workType').value),
                projectDescription: sanitizeInput(document.getElementById('projectDescription').value),
                urgency: document.getElementById('urgency').value,
                completionDate: document.getElementById('completionDate').value,
                howHeard: document.getElementById('howHeard').value,
                additionalComments: sanitizeInput(document.getElementById('additionalComments').value),
                submittedAt: new Date().toISOString()
            };

            // Send email via EmailJS
            await emailjs.send('service_n4hez7p', 'template_4u8tm7q', formData);

            // Success
            showSuccessMessage();
            form.reset();
            otherPropertyGroup.style.display = 'none';
            otherPropertyInput.required = false;

        } catch (error) {
            console.error('Form submission error:', error);
            showErrorMessage('There was a problem submitting your request. Please try again or call us directly.');
        } finally {
            // Re-enable submit button
            submitButton.disabled = false;
            submitButton.textContent = originalText;
        }
    });

    // Success message display
    function showSuccessMessage() {
        const existingMessage = document.querySelector('.form-message');
        if (existingMessage) existingMessage.remove();

        const successDiv = document.createElement('div');
        successDiv.className = 'form-message form-message--success';
        successDiv.innerHTML = `
            <svg class="form-message__icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
            </svg>
            <div>
                <strong>Thank you!</strong>
                <p>Your quote request has been submitted successfully. We'll contact you within 72 hours.</p>
            </div>
        `;
        form.parentNode.insertBefore(successDiv, form);
        form.style.display = 'none';
        successDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    // Error message display
    function showErrorMessage(message) {
        const existingMessage = document.querySelector('.form-message--error');
        if (existingMessage) existingMessage.remove();

        const errorDiv = document.createElement('div');
        errorDiv.className = 'form-message form-message--error';
        errorDiv.innerHTML = `
            <svg class="form-message__icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <div>
                <strong>Submission Error</strong>
                <p>${message}</p>
            </div>
        `;
        form.insertBefore(errorDiv, form.firstChild);
        errorDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

});
