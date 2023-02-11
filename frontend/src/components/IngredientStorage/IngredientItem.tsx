import React from 'react';
import { IngredientStorage } from '../../models/IngredientStorage';
import './IngredientItem.scss';

interface Props {
  ingredient: IngredientStorage;
}

const IngredientItem: React.FC<Props> = ({ ingredient }) => {
  return (
    <div className="ingredient-item">
      <h3 className="ingredient-item__name">{ingredient.ingredient}</h3>
      <p className="ingredient-item__amount">{ingredient.amount} {ingredient.unit}</p>
    </div>
  );
};

export default IngredientItem;
