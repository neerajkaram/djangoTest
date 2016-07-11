from django.contrib import admin

# Register your models here.
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display=['name','email']
admin.site.register(Author,AuthorAdmin)
