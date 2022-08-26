from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin



class CustomUserAdmin(UserAdmin):
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ("age_bracket" , "streak_count" , "streak_day" , "profile_url" , "user_preference" ,"courseOnBoarded" , "currentWPM")}),
    )

    list_display = ("username" ,"first_name" ,"email","date_joined")

    readonly_fields = ("email",)
    search_fields = ('username','first_name','last_name','email',)


# Register your models here.
admin.site.register(User , CustomUserAdmin)