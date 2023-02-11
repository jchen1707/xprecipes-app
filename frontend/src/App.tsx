import React from 'react';
import './App.css';
import { Provider } from 'react-redux';
import { store } from './store/store';
import RecipeList from './components/Recipe/RecipeList';
import RecipeItem from './components/Recipe/RecipeItem';
import IngredientList from './components/IngredientStorage/IngredientList';
import IngredientItem from './components/IngredientStorage/IngredientItem';

function App() {
  const sampleRecipe = {
    title: "Sample Recipe",
    ingredients: "Ingredients",
    ingredient_quantity: 1,
    unit: "unit",
    calories: 100,
    cooktime: "10 minutes",
    image_url: "https://sample-image-url.com"
  };

  const sampleIngredient = {
    id: 1,
    ingredient: "Sample Ingredient",
    amount: 1,
    unit: "unit"
  };

  return (
    <Provider store={store}>
      <div className="App">
        <RecipeList />
        <RecipeItem recipe={sampleRecipe} />
        <IngredientList />
        <IngredientItem ingredient={sampleIngredient} />
      </div>
    </Provider>
  );
}

export default App;
