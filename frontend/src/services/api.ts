import axios from 'axios';
import { Recipe } from '../models/Recipe';
import { IngredientStorage } from '../models/IngredientStorage';


const api = axios.create({
    baseURL: "http://localhost:8080",
  });

  export const getRecipes = async (): Promise<Recipe[]> => {
    const { data } = await api.get("/recipes");
    return data;
  };
  
  export const getRecipeById = async (id: number): Promise<Recipe> => {
    const { data } = await api.get(`/recipes/${id}`);
    return data;
  };
  
  export const createRecipe = async (recipe: Recipe): Promise<Recipe> => {
    const { data } = await api.post("/recipes", recipe);
    return data;
  };
  
  export const updateRecipe = async (id: number, recipe: Recipe): Promise<Recipe> => {
    const { data } = await api.put(`/recipes/${id}`, recipe);
    return data;
  };
  
  export const deleteRecipe = async (id: number): Promise<void> => {
    await api.delete(`/recipes/${id}`);
  };
  
  export const getIngredients = async (): Promise<IngredientStorage[]> => {
    const { data } = await api.get("/ingredients");
    return data;
  };
  
  export const getIngredientById = async (id: number): Promise<IngredientStorage> => {
    const { data } = await api.get(`/ingredients/${id}`);
    return data;
  };
  
  export const createIngredient = async (ingredient: IngredientStorage): Promise<IngredientStorage> => {
    const { data } = await api.post("/ingredients", ingredient);
    return data;
  };
  
  export const updateIngredient = async (id: number, ingredient: IngredientStorage): Promise<IngredientStorage> => {
    const { data } = await api.put(`/ingredients/${id}`, ingredient);
    return data;
  };
  
  export const deleteIngredient = async (id: number): Promise<void> => {
    await api.delete(`/ingredients/${id}`);
  };