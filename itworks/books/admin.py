from django.contrib import admin
from books.models import Book, Author, Country


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Country)

