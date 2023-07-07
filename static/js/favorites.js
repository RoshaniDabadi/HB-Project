document.addEventListener('DOMContentLoaded', function() {
  const favoriteButton = document.getElementById('favoriteButton');
  const heartIcon = document.querySelector('#favoriteButton svg path');

  favoriteButton.addEventListener('click', handleSubmit);

  function handleSubmit(evt) {
    evt.preventDefault();

    const isFavorite = favoriteButton.classList.contains('favorite');

    if (isFavorite) {
      removeFromFavorites();
    } else {
      addToFavorites();
    }
  }

  function addToFavorites() {
    // Display alert message
    alert('Added to your favorites!');

    favoriteButton.classList.add('favorite'); // Add the 'favorite' class
    heartIcon.setAttribute('fill', '#ff0000'); // Set fill color to red

    const recipeId = document.getElementById('recipe_id').value;
    const recipeTitle = document.getElementById('recipe_title').value;
    const recipeImage = document.getElementById('recipe_image').value;

    fetch('/dashboard', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        recipe_id: recipeId,
        recipe_title: recipeTitle,
        recipe_image: recipeImage
      })
    })
      .then(response => response.json())
      .then(data => {
        console.log('Recipe added to favorites!');
      })
      .catch(error => {
        console.error('Error adding recipe to favorites:', error);
      });
  }

  function removeFromFavorites() {
    // Display alert message
    alert('Removed from your favorites!');

    favoriteButton.classList.remove('favorite'); // Remove the 'favorite' class
    heartIcon.setAttribute('fill', 'green'); // Set fill color to default green

    const recipeId = document.getElementById('recipe_id').value;

    fetch('/dashboard', {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        recipe_id: recipeId
      })
    })
      .then(response => response.json())
      .then(data => {
        console.log('Recipe removed from favorites!');
      })
      .catch(error => {
        console.error('Error removing recipe from favorites:', error);
      });
  }
});
