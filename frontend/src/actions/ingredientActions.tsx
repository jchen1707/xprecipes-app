import { Dispatch, AnyAction } from 'redux';
import { IngredientStorage } from '../models/IngredientStorage';


// Action Types
export const ADD_INGREDIENT = 'ADD_INGREDIENT';
export const REMOVE_INGREDIENT = 'REMOVE_INGREDIENT';

// Action Creators
export const addIngredient = (ingredient: IngredientStorage) => ({
  type: ADD_INGREDIENT,
  ingredient
});



export const removeIngredient = (ingredient: IngredientStorage) => ({
  type: REMOVE_INGREDIENT,
  payload: ingredient
});
