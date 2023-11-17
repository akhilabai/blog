from django.contrib import admin

from blog.models import Blog, Category



# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=('title','category','author','is_featured')
    search_fields=('id','title','category__category_name')
    list_editable=('is_featured',)
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)


