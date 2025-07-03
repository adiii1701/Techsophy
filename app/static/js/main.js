document.addEventListener('DOMContentLoaded', function() {
    const healthForm = document.getElementById('healthForm');
    
    if (healthForm) {
        healthForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            // Show loading state
            const submitBtn = healthForm.querySelector('.submit-btn');
            const originalBtnText = submitBtn.textContent;
            submitBtn.disabled = true;
            submitBtn.textContent = 'Processing...';
            
            try {
                // Collect form data
                const formData = {
                    age: parseInt(document.getElementById('age').value),
                    gender: document.getElementById('gender').value,
                    height_cm: parseFloat(document.getElementById('height').value),
                    weight_kg: parseFloat(document.getElementById('weight').value),
                    smoker: document.getElementById('smoker')?.checked || false,
                    family_diabetes: document.getElementById('family_diabetes')?.checked || false,
                    family_heart_disease: document.getElementById('family_heart_disease')?.checked || false,
                    family_obesity: document.getElementById('family_obesity')?.checked || false,
                    exercise_frequency: document.getElementById('exercise_frequency').value,
                    diet_quality: document.getElementById('diet_quality').value,
                    blood_pressure_systolic: document.getElementById('blood_pressure_systolic')?.value,
                    blood_pressure_diastolic: document.getElementById('blood_pressure_diastolic')?.value,
                    cholesterol_mgdl: document.getElementById('cholesterol_mgdl')?.value,
                    hdl_mgdl: document.getElementById('hdl_mgdl')?.value
                };
                
                // Send to API
                const response = await fetch('/api/assess', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(formData)
                });
                
                if (!response.ok) {
                    throw new Error(`Assessment failed: ${response.status}`);
                }
                
                const results = await response.json();
                
                // Store results in session storage for results page
                sessionStorage.setItem('assessmentResults', JSON.stringify(results));
                
                // Redirect to results page
                window.location.href = '/results';
                
            } catch (error) {
                console.error('Error:', error);
                alert('Error performing assessment: ' + error.message);
            } finally {
                // Reset form button
                submitBtn.disabled = false;
                submitBtn.textContent = originalBtnText;
            }
        });
    }
    
    // Results page logic
    if (window.location.pathname === '/results') {
        displayResults();
    }
    
    function displayResults() {
        const results = JSON.parse(sessionStorage.getItem('assessmentResults'));
        if (!results) {
            window.location.href = '/';
            return;
        }
        
        // Display results on the page
        console.log('Assessment results:', results);
        // Implementation would continue here to populate the results page
    }
});