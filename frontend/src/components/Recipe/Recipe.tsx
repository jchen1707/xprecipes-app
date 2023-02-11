import React from "react";
import "./Recipe.scss";

interface RecipeProps {
  title: string;
  ingredients: string;
  ingredient_quantity: number;
  unit: string;
  image: string;
  calories: number;
  cooktime: string;
}

const Recipe: React.FC<RecipeProps> = ({
  title,
  ingredients,
  ingredient_quantity,
  unit,
  image,
  calories,
  cooktime,
}) => {
  return (
    <div className="recipe">
      <h2 className="recipe__title">{title}</h2>
      <p className="recipe__ingredients">
        {ingredients} ({ingredient_quantity} {unit})
      </p>
      <img className="recipe__image" src={image} alt={title} />
      <p className="recipe__calories">{calories} calories</p>
      <p className="recipe__cooktime">Cook time: {cooktime}</p>
    </div>
  );
};

export default Recipe;
