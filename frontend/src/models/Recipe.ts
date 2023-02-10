export interface Recipe {
    id: number,
    title: string,
    ingredients: string,
    ingredient_quantity: number,
    unit: string,
    image_key: string | null,
    image_url: string | null,
    calories: number,
    cooktime: string,
  };

  