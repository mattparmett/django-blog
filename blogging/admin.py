from django.contrib import admin
from blogging.models import Post, Category

class CategorizationInline(admin.StackedInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [CategorizationInline,]

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)