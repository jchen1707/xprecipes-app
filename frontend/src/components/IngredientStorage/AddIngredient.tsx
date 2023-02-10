import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { addIngredient } from '../../actions/ingredientActions';
import { IngredientStorage } from '../../models/IngredientStorage';
import './AddIngredient.scss'

const AddIngredient: React.FC = () => {
  const [ingredient, setIngredient] = useState('');
  const dispatch = useDispatch();

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const ingredientData: IngredientStorage = {
      id: Date.now(),
      ingredient,
      amount: 0,
      unit: ''
    };
    dispatch(addIngredient(ingredientData));
    setIngredient('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={ingredient}
        onChange={e => setIngredient(e.target.value)}
        placeholder="Add Ingredient"
      />
      <button type="submit">Add</button>
    </form>
  );
};

export default AddIngredient;
