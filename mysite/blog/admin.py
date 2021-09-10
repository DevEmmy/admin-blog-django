from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_pub', 'likes', 'dislikes')
    filter = ('date_pub', 'likes')
    list_filter = ('date_pub', 'likes')

admin.site.register(Post, PostAdmin)