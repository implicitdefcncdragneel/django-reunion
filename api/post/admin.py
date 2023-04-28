from django.contrib import admin

from api.post.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    ordering = ["id"]
    model = Post
    list_display = ["id","title"]
    list_display_links = ["id", "title"]
    list_filter = ["author"]

admin.site.register(Post,PostAdmin)