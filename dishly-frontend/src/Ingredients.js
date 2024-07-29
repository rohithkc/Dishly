import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Ingredients() {
  const [ingredientsList, setIngredientsList] = useState([]);

  useEffect(() => {
    const fetchIngredients = async () => {
      try {
        const response = await axios.get('http://localhost:5000/ingredients');
        setIngredientsList(response.data.ingredients);
      } catch (error) {
        console.error('Error fetching ingredients:', error);
      }
    };

    fetchIngredients();
  }, []);

  return (
    <div>
      <h1>Ingredients</h1>
      <ul>
        {ingredientsList.map((ingredient, index) => (
          <li key={index}>{ingredient}</li>
        ))}
      </ul>
    </div>
  );
}

export default Ingredients;
