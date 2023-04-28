from django.contrib import admin

from api.services.models import Reaction,Comment

# Register your models here.

class ReactionAdmin(admin.ModelAdmin):
    ordering = ["id"]
    model = Reaction
    list_display = ["id","user"]
    list_display_links = ["id", "user"]
    list_filter = ["post"]

class CommentAdmin(admin.ModelAdmin):
    ordering = ["id"]
    model = Comment
    list_display = ["id","user","post"]
    list_display_links = ["id", "user","post"]
    list_filter = ["post"]

admin.site.register(Reaction,ReactionAdmin)
admin.site.register(Comment,CommentAdmin)