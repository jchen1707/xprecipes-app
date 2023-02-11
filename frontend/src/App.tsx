import React from 'react';
import './App.scss';
import { Provider } from 'react-redux';
import { store } from './store/store';
import Recipe from './components/Recipe/Recipe';
import RecipeList from './components/Recipe/RecipeList';
import RecipeItem from './components/Recipe/RecipeItem';
import AddRecipe from './components/Recipe/AddRecipe';
import Ingredient from './components/IngredientStorage/Ingredient';
import IngredientList from './components/IngredientStorage/IngredientList';
import IngredientItem from './components/IngredientStorage/IngredientItem';
import AddIngredient from './components/IngredientStorage/AddIngredient';


function App() {
  
  const sampleRecipe = {
    title: "Sample Recipe",
    ingredients: "Sample Ingredient",
    ingredient_quantity: 1,
    unit: "g",
    calories: 100,
    cooktime: "10",
    image_url: "https://sample-image-url.com"
  };

  const sampleIngredient = {
    id: 1,
    ingredient: "Sample Ingredient",
    amount: 1,
    unit: "g"
  };

  return (
    <Provider store={store}>
      <div className="App">
        <Recipe recipe={sampleRecipe} />
        <AddRecipe />
        <RecipeList />
        <RecipeItem recipe={sampleRecipe} />
        <Ingredient ingredient = {sampleIngredient} />
        <AddIngredient />
        <IngredientList />
        <IngredientItem ingredient={sampleIngredient} />
      </div>
    </Provider>
  );
}

export default App;
