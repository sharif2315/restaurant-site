import Menu from "./Menu";

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
    name: string;
    description: string | null;
    menu_items: MenuItem[];
}

const MenuSection = async() => {
    const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL
    const response = await fetch(`${BACKEND_URL}/api/menu_items/`);

    if (!response.ok) {
        throw new Error('Failed to fetch menu categories');
    }
            
    const data: MenuCategory[] = await response.json();

    return(
        <Menu menuCategories={data} />
    )
}

export default MenuSection;