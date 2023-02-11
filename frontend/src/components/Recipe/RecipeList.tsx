import React from "react";
import { useSelector } from "react-redux";
import { RootState } from "../../redux/rootReducer";
import { Recipe } from "../../models/Recipe";
import RecipeItem from "./RecipeItem";
import "./RecipeList.scss";

const RecipeList: React.FC = () => {
  const recipes = useSelector((state: RootState) => state.recipes) as Recipe[];

  return (
    <ul className="recipe-list">
      {recipes.map((recipe: Recipe) => (
        <li key={recipe.id} className="recipe-list__item">
          <RecipeItem recipe={recipe} />
        </li>
      ))}
    </ul>
  );
};

export default RecipeList;
