from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin



class CustomUserAdmin(UserAdmin):

    # actions = [download_csv,]

    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ("user_type",  "phone","ios" , "ios_id", "bharatx_verified", "uuid", "augmont_user", "augmont_bank", "upi", "user_preference", "profile_url","device_id","device_id_dict", 
    #     "name", "gender", "aadhaar_number")}),
    # )
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {'fields': ("user_type", "phone", "uuid", "augmont_user", "augmont_bank", "upi", "user_preference", "profile_url","device_id" , "device_id_dict", 
    #     "name", "gender", "aadhaar_number")}),
    # )

    list_display = ("username" ,"first_name" ,"email","date_joined")

    readonly_fields = ("email",)
    search_fields = ('username','first_name','last_name','email',)


# Register your models here.
admin.site.register(User , CustomUserAdmin)