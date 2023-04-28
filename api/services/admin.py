from django.contrib import admin

from api.services.models import Reaction

# Register your models here.

class ReactionAdmin(admin.ModelAdmin):
    ordering = ["id"]
    model = Reaction
    list_display = ["id","user"]
    list_display_links = ["id", "user"]
    list_filter = ["post"]

admin.site.register(Reaction,ReactionAdmin)