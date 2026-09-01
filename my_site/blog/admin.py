from django.contrib import admin
from blog.models import Post,Author,Tag,Comment
# Register your models here.

class Post_admin(admin.ModelAdmin):
    list_filter=("author","caption","date",)
    list_display=("title","date","author")
    prepopulated_fields  = {"slug":("title",)}


class Comment_Admin(admin.ModelAdmin):
    list_display=("user_name","post")

admin.site.register(Post,Post_admin)
admin.site.register(Author)

admin.site.register(Tag)
admin.site.register(Comment,Comment_Admin)


