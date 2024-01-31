// DOM Selection

// SELECTORS SELECTORS SELECTORS SELECTORS SELECTORS SELECTORS SELECTORS
// SELECTORS SELECTORS SELECTORS SELECTORS SELECTORS SELECTORS SELECTORS
// SELECTORS SELECTORS SELECTORS SELECTORS SELECTORS SELECTORS SELECTORS
// SELECTORS SELECTORS SELECTORS SELECTORS SELECTORS SELECTORS SELECTORS

// GetElementById() ==================================================
// 1. Skapa en variabel som heter title som är lika med rubriken
// Logga title till consolen

const title = document.getElementById('main-heading');
console.log(title);

// GetElementByClassName() ===========================================
// 2. Skapa en variabel som heter listItemsByClass som innehåller alla list-items (node list)
// Logga listItemsByClass till consolen

const listItemsByClass = document.getElementsByClassName('list-items');
console.log(listItemsByClass);

// GetElementByTagName() =============================================
// 3. Skapa en variabel som heter listItemsByTag som innehåller alla list-items
// Logga listItemsByTag till consolen

const listItemsByTag = document.getElementsByTagName('li');
console.log(listItemsByTag);

// QuerySelector() - Väljer den FÖRSTA element som matchar  ==========
// 4. Selekta den första div tag och lägg den i en variabel som heter container
// Logga container till consolen

const container = document.querySelector('div');
console.log(container);

// QuerySelectorAll() - Väljer ALLA element som matchar ==============
// 5. Skapa en variabel som heter allDivs och logga den till consolen

const allDivs = document.querySelectorAll('div');
console.log(allDivs);

// STYLING STYLING STYLING STYLING STYLING STYLING STYLING STYLING STYLING
// STYLING STYLING STYLING STYLING STYLING STYLING STYLING STYLING STYLING
// STYLING STYLING STYLING STYLING STYLING STYLING STYLING STYLING STYLING
// STYLING STYLING STYLING STYLING STYLING STYLING STYLING STYLING STYLING

// 6. Ändra färgen på rubriken. Använd QuerySelector

const rubrik = document.querySelector('#main-heading');
rubrik.style.color = "red";

// 7. Gör font storlek lite större för alla list items.
// Använd QuerySelectorAll
// Tips Kanske behöver en loop

const listOfMovies = document.querySelectorAll('li');
listOfMovies.forEach((movie) => movie.style.scale="100%"); // t.ex 120%

// 8. Flytta texten i footer till höger... det ser konstigt ut när den står i mitten
// Använd querySelector

const footerText = document.querySelector('.footer');
footerText.style.textAlign="right";

// CREATING CREATING CREATING CREATING CREATING CREATING CREATING CREATING
// CREATING CREATING CREATING CREATING CREATING CREATING CREATING CREATING
// CREATING CREATING CREATING CREATING CREATING CREATING CREATING CREATING
// CREATING CREATING CREATING CREATING CREATING CREATING CREATING CREATING

// 9. Jag glömde Indiana Jones! Lägg till det i din ul (lite svårare)
// Tips: Undvik innerHTML då det finns säkerhetsrisker

const moviesList = document.querySelector('ul');
const newMovie = document.createElement('li');
newMovie.innerText = "Indiana Jones";
moviesList.append(newMovie);

// 10. På samma sätt som i övning 9 vill jag att du lägga till The Hoobit (lite svårare)
// OBS: Denna gång vill jag att The Hobbit hamnar högst upp i listan


const newMovie2 = document.createElement('li');
newMovie2.innerText = "The Hobbit";
moviesList.prepend(newMovie2);

// Method 1 Det finns en metod som heter removeAttribute också!

// Jag uppdaterar fontstorleken för att matcha övning 7



// REMOVING REMOVING REMOVING REMOVING REMOVING REMOVING REMOVING REMOVING
// REMOVING REMOVING REMOVING REMOVING REMOVING REMOVING REMOVING REMOVING
// REMOVING REMOVING REMOVING REMOVING REMOVING REMOVING REMOVING REMOVING
// REMOVING REMOVING REMOVING REMOVING REMOVING REMOVING REMOVING REMOVING

// 11. Min fru hatar Keanu Reeves... ta bort alla filmer som han är med i.
// Tips: Du får uppdatera HTML koden

// TRAVERSING THE DOM TRAVERSING THE DOM TRAVERSING THE DOM TRAVERSING THE DOM
// TRAVERSING THE DOM TRAVERSING THE DOM TRAVERSING THE DOM TRAVERSING THE DOM
// TRAVERSING THE DOM TRAVERSING THE DOM TRAVERSING THE DOM TRAVERSING THE DOM
// TRAVERSING THE DOM TRAVERSING THE DOM TRAVERSING THE DOM TRAVERSING THE DOM

// 12. Log till consolen parent till din lista

// 13. Log till consolen grandparent till din lista

// 14. Log till consolen child till din lista
// OBS: Även tabbarna räknas som en text node (så du kanske inte förväntade dig resultatet)

// 15. Gör first child i din lista till en röd background

// 16. Log till console previous sibling till din lista

// 17. Log till console next sibling till din lista