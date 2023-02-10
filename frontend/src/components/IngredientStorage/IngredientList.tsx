import React from "react";
import { useSelector } from "react-redux";
import { RootState } from "../../redux/rootReducer";
import { IngredientStorage } from "../../models/IngredientStorage";
import Ingredient from "./Ingredient";
import "./IngredientList.scss";

const IngredientList: React.FC = () => {
  const ingredients = useSelector(
    (state: RootState) => state.ingredients
  ) as IngredientStorage[];

  return (
    <ul className="ingredient-list">
      {ingredients.map((ingredient: IngredientStorage) => (
        <li key={ingredient.id} className="ingredient-list__item">
          <Ingredient ingredient={ingredient} />
        </li>
      ))}
    </ul>
  );
};

export default IngredientList;
