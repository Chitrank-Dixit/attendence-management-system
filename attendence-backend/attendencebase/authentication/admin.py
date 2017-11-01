from django.contrib import admin

# Register your models here.
from authentication.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'get_full_name', 'is_active', 'is_staff', 'gender')
    search_fields = ('email', )
    readonly_fields = ('username', 'last_login')

admin.site.register(User, UserAdmin)