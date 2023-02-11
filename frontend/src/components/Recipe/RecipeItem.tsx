import React from 'react';
import { Recipe } from '../../models/Recipe';
import './RecipeItem.scss';

interface Props {
  recipe: Recipe;
}

const RecipeItem: React.FC<Props> = ({ recipe }) => {
  return (
    <div className="recipe-item">
      <h3 className="recipe-item__title">{recipe.title}</h3>
      <p className="recipe-item__ingredients">{recipe.ingredients}</p>
      <p className="recipe-item__quantity">
        {recipe.ingredient_quantity} {recipe.unit}
      </p>
      <p className="recipe-item__calories">{recipe.calories} calories</p>
      <p className="recipe-item__cooktime">{recipe.cooktime}</p>
      {recipe.image_url && (
        <img
          className="recipe-item__image"
          src={recipe.image_url}
          alt={recipe.title}
        />
      )}
    </div>
  );
};

export default RecipeItem;
