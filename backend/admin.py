from django.contrib import admin
from backend.user.models import User
from backend.category.models import Category
from backend.store.models import Product
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name',
                    'last_login', 'is_active', 'updated')
    readonly_fields = ('password', 'created', 'updated')
    ordering = ('first_name', 'last_name')
    list_display_links = ('email', 'first_name', 'last_name')
    list_per_page = 10
    search_fields = ('username', 'first_name', 'last_name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug', 'updated')
    ordering = ('created', 'updated')
    list_per_page = 10
    search_fields = ('category_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'price', 'stock',
                    'category', 'created', 'updated')
