export interface MenuItem {
    id: number;
    name: string;
    description: string;
    price: string;
    category: number;
    category_name: string;
    category_description: string | null;
}

export interface MenuCategory {
    id: number;
    name: string;
    description: string | null;
    menu_items: MenuItem[];
}