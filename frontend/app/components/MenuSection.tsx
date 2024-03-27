import { MenuCategory } from "@/menu.types";
import Menu from "./Menu";

const MenuSection = async() => {
    const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL
    const response = await fetch(`${BACKEND_URL}/api/menu_items/`);

    if (!response.ok) {
        throw new Error('Failed to fetch menu categories');
    }
            
    const data: MenuCategory[] = await response.json();

    return(
        <>
            <Menu menuList={data} />
        </>

    )
}
export default MenuSection;