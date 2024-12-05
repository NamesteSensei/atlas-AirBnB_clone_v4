document.addEventListener('DOMContentLoaded', function () {
    const apiStatusDiv = document.getElementById('api_status');
    const filterForm = document.getElementById('filter-form');
    const placesSection = document.querySelector('.places');

    // Function to check the status of the API
    function checkApiStatus() {
        fetch('http://0.0.0.0:5001/api/v1/status/')
            .then(response => response.json())
            .then(data => {
                if (data.status === 'OK') {
                    apiStatusDiv.classList.add('available');
                } else {
                    apiStatusDiv.classList.remove('available');
                }
            });
    }

    // Fetch and display places based on selected amenities
    function fetchFilteredPlaces() {
        const formData = new FormData(filterForm);
        const amenities = formData.getAll('amenities');

        fetch('http://0.0.0.0:5001/api/v1/places_search/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ amenities: amenities })
        })
        .then(response => response.json())
        .then(places => {
            placesSection.innerHTML = ''; // Clear previous results
            places.forEach(place => {
                const placeArticle = document.createElement('article');
                placeArticle.innerHTML = `
                    <h2>${place.name}</h2>
                    <p>${place.description}</p>
                    <span>${place.price_by_night} USD/night</span>
                `;
                placesSection.appendChild(placeArticle);
            });
        });
    }

    // Event listener for form submission
    filterForm.addEventListener('submit', function (event) {
        event.preventDefault();
        fetchFilteredPlaces();
    });

    // Initial API status check
    checkApiStatus();
});
