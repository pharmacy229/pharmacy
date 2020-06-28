from django.contrib import admin

# Register your models here.
from med.models import medicine
from med.models import blog
from med.models import upload, contactus

@admin.register(medicine)
class medicineAdmin(admin.ModelAdmin):
    pass
@admin.register(upload)
class uploadAdmin(admin.ModelAdmin):
    list_display=('name','address','phone','image',)
@admin.register(contactus)
class contactusAdmin(admin.ModelAdmin):
    list_display=('name','subject','email','message',)
@admin.register(blog)
class blogAdmin(admin.ModelAdmin):
    pass
    
