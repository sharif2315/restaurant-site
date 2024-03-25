from django.db import models


class MenuCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'
        # return f'{self.name} - {self.order}'

    class Meta:
        verbose_name = "Menu Category"
        verbose_name_plural = "Menu Categories"
        ordering = ['order'] 


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)

    def __str__(self):
        # return self.name
        return f'{self.category} - {self.name}'

    class Meta:
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"


# class MenuCategoryFilter(WagtailFilterSet):
#     model = MenuCategory
#     fields = ['name']


# class MenuItemFilter(WagtailFilterSet):
#     model = MenuItem
#     fields = ['name', 'category']



# class ContactSubmission(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     message = models.TextField()
#     submitted_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Message from {self.name}"