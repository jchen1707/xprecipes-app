import { v4 as uuidv4 } from 'uuid';

const initialState = {
  ingredients: [],
};

export const ingredientReducer = (state = initialState, action: any) => {
  switch (action.type) {
    case 'ADD_INGREDIENT':
      return {
        ...state,
        ingredients: [
          ...state.ingredients,
          {
            id: uuidv4(),
            ingredient: action.ingredient,
            amount: 0,
            unit: ''
          },
        ],
      };
    default:
      return state;
  }
};