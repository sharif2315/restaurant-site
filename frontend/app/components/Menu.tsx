"use client";
import { useState, useEffect } from "react";
import { MenuCategory, MenuItem } from "@/menu.types";
import { BsChevronRight } from "react-icons/bs";

interface MenuProps {
  menuList: MenuCategory[];
}


const Menu: React.FC<MenuProps> = ({ menuList }) => {


  return (
    <div className="my-24 flex flex-col justify-center items-center">

      <h1 className="text-6xl">Menu</h1>
      
      <div className="grid grid-cols-1 lg:grid-cols-2 2xl:grid-cols-3 justify-center">

        {menuList.map((category) => (
          <div key={category.id} className="flex flex-col p-10 w-full max-w-xl">

            <div className="flex items-baseline justify-between">
              <h2 className="text-4xl">{category.name}</h2>

              {/* Arrow Icon */}
              <div className="XXX_lg:hidden">
                <BsChevronRight className="text-3xl text-gray-500 hover:text-gray-800 transform transition-transform duration-200 hover:cursor-pointer" />
              </div>

            </div>

            {/* display category description if it exists in category */}
            {category.description && (
              <p className="text-sm">{category.description}</p>
            )}

            {/* Menu Items Container */}
            {/* run a for loop over the menu_items existing in each category */}
            {category.menu_items.map((item) => (
              <div key={item.id} className={`flex flex-col gap-2 mt-4 lg:overflow-y-auto lg:max-h-[50rem] lg:pr-4`}>
                <div className="flex gap-4 items-center justify-between">
                  <div className="w-3/4">
                    <h3 className="font-semibold">{item.name}</h3>
                    <p className="text-sm">{item.description}</p>
                  </div>
                  <p>{item.price}</p>
                </div>
              </div>
            ))}          

          </div>
        ))}

      </div>
    </div>
  );
};

export default Menu;
