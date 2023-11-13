from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(model_or_iterable=Post, admin_class=PostAdmin)