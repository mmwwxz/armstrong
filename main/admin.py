from django.contrib import admin
from main.models import Category, Product, Blog, Comment, Request, Info, HomePage, BlogDetail


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_type']
    search_fields = ['name', 'category_type']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'retail_price', 'wholesale_price', 'bulk_price', 'warranty', 'region')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'region')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    ordering = ('-created_at',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'created_at')
    ordering = ('-created_at',)

class RequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'comments', 'created_at')
    ordering = ('-created_at',)


class InfoAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'social_link_insta', 'social_link_facebook', 'social_link_whatsapp', 'social_link_telegram')

class HomePageAdmin(admin.ModelAdmin):
    list_display = ('titile_1_line', 'titile_2_line', 'description')

class BlogDetailAdmin(admin.ModelAdmin):
    list_display = ('title')
    ordering = ('-created_at',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(Info, InfoAdmin)
admin.site.register(HomePage, HomePageAdmin)
admin.site.register(BlogDetail, BlogDetail)