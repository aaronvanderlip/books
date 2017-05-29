from django.conf.urls import patterns, include, url
from django.contrib import admin

from books.views import ListView, BookDetail, Home, About

admin.autodiscover()

urlpatterns = patterns('',
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
                        url(r'^$', Home.as_view(), name='home'),
                        url(r'^about/$', About.as_view(), name='About'),
                        url(r'^books/$', ListView.as_view()),
                        url(r'^books/erotica/$', ListView.as_view(),{'filter':'erotica'}),
                        url(r'^books/romance/$', ListView.as_view(), {'filter':'romance'}),
                        url(r'^books/(?P<slug>.+)/$', BookDetail.as_view(), name='book-detail'
                            ),)

# For dev
# from django.conf.urls.static import static
# from django.conf import settings
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
