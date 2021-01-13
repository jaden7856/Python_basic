from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'count_text']
    list_display_links = ['title']

    def count_text(self, obj):
        return f'{len(obj.text)}글자'


admin.site.register(Post, PostAdmin)
