import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { addRecipe } from "../../redux/recipesSlice";
import "./AddRecipe.scss";

interface RecipeData {
  title: string;
  ingredients: string;
  ingredient_quantity: number;
  unit: string;
  image: File | null;
  calories: number;
  cooktime: string;
}

const AddRecipe: React.FC = () => {
  const [recipeData, setRecipeData] = useState<RecipeData>({
    title: "",
    ingredients: "",
    ingredient_quantity: 0,
    unit: "",
    image: null,
    calories: 0,
    cooktime: "",
  });

  const dispatch = useDispatch();

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setRecipeData({ ...recipeData, [name]: value });
  };

  const handleFileInputChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setRecipeData({ ...recipeData, image: event.target.files?.[0] || null });
  };

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    dispatch(addRecipe(recipeData));
    setRecipeData({
      title: "",
      ingredients: "",
      ingredient_quantity: 0,
      unit: "",
      image: null,
      calories: 0,
      cooktime: "",
    });
  };

  return (
    <form className="add-recipe" onSubmit={handleSubmit}>
      <input
        type="text"
        name="title"
        value={recipeData.title}
        onChange={handleInputChange}
        placeholder="Recipe title"
      />
      <input
        type="text"
        name="ingredients"
        value={recipeData.ingredients}
        onChange={handleInputChange}
        placeholder="Ingredients"
      />
      <input
        type="number"
        name="ingredient_quantity"
        value={recipeData.ingredient_quantity}
        onChange={handleInputChange}
        placeholder="Ingredient quantity"
      />
      <input
        type="text"
        name="unit"
        value={recipeData.unit}
        onChange={handleInputChange}
        placeholder="Unit"
      />
      <input type="file" name="image" onChange={handleFileInputChange} />
      <input
        type="number"
        name="calories"
        value={recipeData.calories}
        onChange={handleInputChange}
        placeholder="Calories"
      />
      <input
        type="text"
        name="cooktime"
        value={recipeData.cooktime}
        onChange={handleInputChange}
        placeholder="Cooktime"
      />
      <button type="submit">Add Recipe</button>
    </form>
  );
};

export default AddRecipe;
