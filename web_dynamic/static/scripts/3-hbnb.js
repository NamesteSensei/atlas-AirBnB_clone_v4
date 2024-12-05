// This script dynamically loads places and checks the API status.

document.addEventListener('DOMContentLoaded', function () {
    const apiStatusDiv = document.getElementById('api_status');
    
    // Function to check the status of the API
    function checkApiStatus() {
        fetch('http://127.0.0.1:5001/api/v1/status/')
            .then(response => response.json())
            .then(data => {
                if (data.status === 'OK') {
                    apiStatusDiv.classList.add('available');
                } else {
                    apiStatusDiv.classList.remove('available');
                }
            })
            .catch(() => {
                apiStatusDiv.classList.remove('available');
            });
    }

    // Call the function to check the API status
    checkApiStatus();

    // Fetch places data
    fetch('http://127.0.0.1:5001/api/v1/places_search/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({})
    })
    .then(response => response.json())
    .then(places => {
        const placesSection = document.querySelector('.places');
        
        if (placesSection) { // Make sure the .places section exists
            places.forEach(place => {
                const placeArticle = document.createElement('article');
                placeArticle.innerHTML = `
                    <h2>${place.name}</h2>
                    <p>${place.description}</p>
                    <span>${place.price_by_night} USD/night</span>
                `;
                placesSection.appendChild(placeArticle);
            });
        }
    })
    .catch(err => console.error('Error fetching places:', err));
});
