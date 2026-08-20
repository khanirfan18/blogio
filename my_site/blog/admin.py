from django.contrib import admin
from blog.models import Post,Author,Tag
# Register your models here.

class Post_admin(admin.ModelAdmin):
    list_filter=("author","caption","date",)
    list_display=("title","date","author")
    prepopulated_fields  = {"slug":("title",)}

admin.site.register(Post,Post_admin)
admin.site.register(Author)

admin.site.register(Tag)

