from django.contrib import admin
from blog.models import Post, Author


class BlogAdmin(admin.ModelAdmin):
    # select fields to display on main admin page
    list_display = ['title', 'author']
    # enable filtering your display list by field
    list_filter = ['published', 'creation_date']
    # enable search fields
    search_fields = ['title', 'author', 'content']
    # Display dropdown menus as radio buttons.
    radio_fields = {"author": admin.VERTICAL}
    # enable drilldown by date
    date_hierarchy = 'creation_date'
    # prepopulate the slug with the title
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, BlogAdmin)
admin.site.register(Author)
