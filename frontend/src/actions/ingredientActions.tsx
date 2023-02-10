import { IngredientStorage } from '../models/IngredientStorage';

// Action Types
export const ADD_INGREDIENT = 'ADD_INGREDIENT';
export const REMOVE_INGREDIENT = 'REMOVE_INGREDIENT';
export const UPDATE_INGREDIENT = 'UPDATE_INGREDIENT';

// Action Creators
export const addIngredient = (ingredient: IngredientStorage) => ({
type: ADD_INGREDIENT,
ingredient
});

export const removeIngredient = (ingredient: IngredientStorage) => ({
type: REMOVE_INGREDIENT,
payload: ingredient
});

export const updateIngredient = (ingredient: IngredientStorage) => ({
type: UPDATE_INGREDIENT,
payload: ingredient
});