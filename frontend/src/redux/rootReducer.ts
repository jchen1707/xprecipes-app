import { combineReducers } from "redux";
import { IngredientStorage } from "../models/IngredientStorage";
import {
  ADD_INGREDIENT,
  REMOVE_INGREDIENT,
  UPDATE_INGREDIENT,
} from "../actions/ingredientActions";

interface State {
    ingredients: IngredientStorage[];
  }
  
  const initialState: State = {
    ingredients: [],
  };
  
  const ingredientReducer = (
    state = initialState.ingredients,
    action: { type: string; ingredient?: IngredientStorage }
  ) => {
    switch (action.type) {
      case ADD_INGREDIENT:
        return [...state, action.ingredient];
      case REMOVE_INGREDIENT:
        return state.filter((ingredient) => ingredient !== action.ingredient);
      case UPDATE_INGREDIENT:
        return state.map((ingredient) => {
          if (ingredient === action.ingredient) {
            return {
              ...ingredient,
              ...action.ingredient,
            };
          }
          return ingredient;
        });
      default:
        return state;
    }
  };
  
  const rootReducer = combineReducers({
    ingredients: ingredientReducer,
  });
  
  export type RootState = ReturnType<typeof rootReducer>;
  
  export default rootReducer;
  