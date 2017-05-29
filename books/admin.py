from django.contrib import admin
from books.models import (
    Book, Publisher, VendorLink,
    Review, Theme, Series,
    SeriesEntry, SiteImage,
    )


class VendorAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('book', 'name', 'format')

class ReviewAdmin(admin.ModelAdmin):
    save_as = True

admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(VendorLink, VendorAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Theme)
admin.site.register(Series)
admin.site.register(SeriesEntry)
admin.site.register(SiteImage)
