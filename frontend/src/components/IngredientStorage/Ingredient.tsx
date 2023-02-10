  import React, { useState } from 'react';
  import { useDispatch } from 'react-redux';
  import { updateIngredient } from '../../actions/ingredientActions';
  import { IngredientStorage } from '../../models/IngredientStorage';
  import './Ingredient.scss';

  interface Props {
    ingredient: IngredientStorage;
  }

  const Ingredient: React.FC<Props> = ({ ingredient }) => {
    const [isEditing, setIsEditing] = useState(false);
    const [currentIngredient, setCurrentIngredient] = useState({
      ...ingredient
    });
    const dispatch = useDispatch();

    const handleEdit = () => {
      setIsEditing(true);
    };

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
      setCurrentIngredient({
        ...currentIngredient,
        [e.target.name]: e.target.value
      });
    };

    const handleSave = (e: React.FormEvent<HTMLFormElement>) => {
      e.preventDefault();
      dispatch(updateIngredient(currentIngredient));
      setIsEditing(false);
    };

    return (
      <>
        {isEditing ? (
          <form onSubmit={handleSave}>
            <input
              type="text"
              name="ingredient"
              value={currentIngredient.ingredient}
              onChange={handleChange}
              placeholder="Ingredient"
            />
            <input
              type="number"
              name="amount"
              value={currentIngredient.amount}
              onChange={handleChange}
              placeholder="Amount"
            />
            <input
              type="text"
              name="unit"
              value={currentIngredient.unit}
              onChange={handleChange}
              placeholder="Unit"
            />
            <button type="submit">Save</button>
          </form>
        ) : (
          <>
            <p>
              {ingredient.ingredient} - {ingredient.amount} {ingredient.unit}
            </p>
            <button onClick={handleEdit}>Modify</button>
          </>
        )}
      </>
    );
  };

  export default Ingredient;
