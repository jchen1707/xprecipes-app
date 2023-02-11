import React from "react";
import "./Recipe.scss";
import { Recipe as RecipeType } from "../../models/Recipe";

interface Props {
  recipe: RecipeType;
}

const Recipe: React.FC<Props> = ({ recipe }) => {
  return (
    <div className="recipe">
      <h2 className="recipe__title">{recipe.title}</h2>
      <p className="recipe__ingredients">
        {recipe.ingredients} ({recipe.ingredient_quantity} {recipe.unit})
      </p>
      {recipe.image_url && (
        <img className="recipe__image" src={recipe.image_url} alt={recipe.title} />
      )}
      <p className="recipe__calories">{recipe.calories} calories</p>
      {recipe.cooktime && <p className="recipe__cooktime">Cook time: {recipe.cooktime}</p>}
    </div>
  );
};

export default Recipe;
