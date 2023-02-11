import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { Recipe } from "../models/Recipe";

interface RecipeState {
  recipes: Recipe[];
}

const initialState: RecipeState = {
  recipes: []
};

const recipeSlice = createSlice({
  name: "recipes",
  initialState,
  reducers: {
    addRecipe: (state, action: PayloadAction<Recipe>) => {
      state.recipes.push(action.payload);
    }
  }
});

export const { addRecipe } = recipeSlice.actions;
export default recipeSlice.reducer;
