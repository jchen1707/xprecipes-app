import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { v4 as uuidv4 } from 'uuid';

interface Ingredient {
  id: string;
  ingredient: string;
  amount: number;
  unit: string;
}

interface IngredientsState {
  ingredients: Ingredient[];
}

const initialState: IngredientsState = {
  ingredients: [],
};

const ingredientSlice = createSlice({
  name: 'ingredients',
  initialState,
  reducers: {
    addIngredient: (state, action: PayloadAction<string>) => {
      state.ingredients.push({
        id: uuidv4(),
        ingredient: action.payload,
        amount: 0,
        unit: '',
      });
    },
  },
});

export const ingredientReducer = ingredientSlice.reducer;
export const { addIngredient } = ingredientSlice.actions;
