import React, { useState } from 'react';
import axios from 'axios';

function Home() {
  const [ingredients, setIngredients] = useState('');
  const [recipe, setRecipe] = useState('');
  const [error, setError] = useState('');

  const generateRecipe = async () => {
    try {
      const response = await axios.post('http://localhost:5000/generate-recipe', { ingredients });
      setRecipe(response.data.recipe);
      setError('');
    } catch (error) {
      setError(error.response ? error.response.data.error : 'Error generating recipe');
      console.error('Error generating recipe:', error);
    }
  };

  return (
    <div>
      <h1>Dishly</h1>
      <input
        type="text"
        placeholder="Enter ingredients separated by commas"
        value={ingredients}
        onChange={(e) => setIngredients(e.target.value)}
      />
      <button onClick={generateRecipe}>Generate Recipe</button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <div>
        <h2>Generated Recipe:</h2>
        <p>{recipe}</p>
      </div>
    </div>
  );
}

export default Home;
