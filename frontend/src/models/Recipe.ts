export interface Recipe {
  title: string;
  ingredients: string;
  ingredient_quantity: number;
  unit: string;
  calories: number;
  cooktime?: string;
  image_url?: string;
}
