document.getElementById("searchForm").addEventListener("submit", function(event) {
    event.preventDefault();

    var searchQuery = document.getElementById("kundsok").value;
    var searchType = document.getElementById("soktyp").value;

    fetch('/search_kunder', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: searchQuery, type: searchType }),
    })
    .then(response => response.json())
    .then(data => {
        var resultsContainer = document.getElementById("resultat_kundsok");
        resultsContainer.innerHTML = ""; // Clear previous results
        data.forEach(function(kund) {
            var infoLink = "<a href='/kund/" + kund.id + "' class='btn'>Info</a>";
            resultsContainer.innerHTML += "<p>" + kund.name + " - " + kund.address + " " + infoLink + "</p>";
        });
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});