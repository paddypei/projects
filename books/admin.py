#encoding:utf-8
from django.contrib import admin

# Register your models here.
from books.models import Book,Publisher,Author

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publication_date',)
    list_filter = ('title',)
    ordering = ('-publication_date',)
    #显示list字段 publisher_name属于表publisher的字段
    #出版社名称
    def publisher_name(self,obj):
        return obj.publisher.name
    #显示作者名称，many_to_many
    def author_name(self,obj):
        authors = ""
        for author in obj.authors.all():
            authors = author.name + "," + authors
        return authors

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