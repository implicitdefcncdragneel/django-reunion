from django.contrib import admin
from api.account.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    ordering = ["id"]
    model = User
    list_display = ["id","email"]
    list_display_links = ["id", "email"]
    list_filter = ["email"]

admin.site.register(User,UserAdmin)