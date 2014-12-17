from django.contrib import admin

# Register your models here.
from books.models import Book,Publisher,Author

class BookAdmin(admin.ModelAdmin):
    #list_display = ('title','publisher_id', 'publication_date')
    list_display = ('title','publication_date')
    list_filter = ('title',)
    ordering = ('-publication_date',)
admin.site.register(Book, BookAdmin)

class PubliserAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'website')
    list_filter = ('name',)
    ordering = ('-name',)

admin.site.register(Publisher, PubliserAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name',)
    ordering = ('-name',)
admin.site.register(Author, AuthorAdmin)