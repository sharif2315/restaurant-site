'use client'
// import { useState, useEffect } from 'react';
import { MenuCategory } from './MenuSection';


// const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL

interface MenuProps {
    menuCategories: MenuCategory[];

}

const Menu: React.FC<MenuProps> = ({menuCategories}) => {
    // const [menuCategories, setMenuCategories] = useState<MenuCategory[]>([]);
    // const [openIndexes, setOpenIndexes] = useState<number[]>([]);
    // const [windowWidth, setWindowWidth] = useState(window.innerWidth);

    // const toggleIndex = (index: number) => {
    //     setOpenIndexes(prevIndexes =>
    //         prevIndexes.includes(index) ? prevIndexes.filter(i => i !== index) : [...prevIndexes, index]
    //     );
    // };

    // useEffect(() => {        
    //     // const fetchMenuCategories = async () => {
    //     //     try {
    //     //         // const response = await fetch('http://localhost:8000/api/menu_items/');
    //     //         // const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/menu_items/`);
    //     //         const response = await fetch(`${BACKEND_URL}/api/menu_items/`);

    //     //         if (!response.ok) {
    //     //             throw new Error('Failed to fetch menu categories');
    //     //         }
                
    //     //         const data: MenuCategory[] = await response.json();
    //     //         // console.log(data);
    //     //         setMenuCategories(data);
    //     //         setOpenIndexes(Array.from({ length: data.length }, (_, i) => i + 1));
    //     //     } catch (error) {
    //     //         console.error(error);
    //     //     }
    //     // };

    //     // fetchMenuCategories();

    //     // Event listener for window resize
    //     const handleResize = () => {
    //         setWindowWidth(window.innerWidth);
    //     };
    //     window.addEventListener('resize', handleResize);

    //     return () => {
    //         window.removeEventListener('resize', handleResize);
    //     };
    // }, []);    

    return (
        <div className="my-24 flex flex-col justify-center items-center">
            
            <h1 className="text-6xl">Menu</h1>

            <div className="grid grid-cols-1 lg:grid-cols-2 2xl:grid-cols-3 justify-center">

                {/* {menuCategories.map((category, index) => (
                    <div key={index} className="my-8">
                        <h2 className="text-4xl">{category.name}</h2>
                        <p className="text-lg">{category.description}</p>
                        <ul>
                            {category.menu_items.map((item, index) => (
                                <li key={index} className="my-4">
                                    <h3 className="text-2xl">{item.name}</h3>
                                    <p className="text-lg">{item.description}</p>
                                    <p className="text-lg">{item.price}</p>
                                </li>
                            ))}
                        </ul>
                    </div>         
                ))} */}

            </div>
        </div>
    );
};

export default Menu;
