import { configureStore } from '@reduxjs/toolkit';
import { ingredientReducer } from '../redux/ingredientReducer';

export const store = configureStore({
  reducer: {
    ingredients: ingredientReducer,
  },
});