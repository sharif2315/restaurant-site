from wagtail.snippets.models import register_snippet
from .models import MenuCategory, MenuItem

from wagtail.admin.panels import FieldPanel
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup


class MenuCategoryViewSet(SnippetViewSet):
    model = MenuCategory
    field_panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('order'),
    ]
    list_display = ('name', 'description', 'order')
    add_to_admin_menu = True
    

class MenuItemViewSet(SnippetViewSet):
    model = MenuItem
    field_panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('price'),
        FieldPanel('category'),
    ]
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)
    add_to_admin_menu = True

register_snippet(MenuCategoryViewSet)
register_snippet(MenuItemViewSet)


# class MenuViewSetGroup(SnippetViewSetGroup):
#     menu_name = 'menu'
#     menu_label = 'Menu'
#     items = [MenuCategoryViewSet, MenuItemViewSet]

# register_snippet(MenuViewSetGroup)

# register_snippet(MenuCategory)
# register_snippet(MenuItem)