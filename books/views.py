from django.views.generic import ListView, DetailView, TemplateView
from books.models import Book

class ListView(ListView):

    context_object_name = "book_list"
    model = Book

    def get_queryset(self):

        filter = self.kwargs.get('filter', None)
        pub_type = self.request.GET.get('pub_type', None)
        query_set = Book.objects.all().exclude(
            publisher__name="Ellora's Cave").order_by('-pub_date')

        if filter == 'erotica':
            query_set = Book.objects.filter(genre='EROTICA')
        if filter == 'romance':
            query_set = Book.objects.filter(genre='ROMANCE')
        if pub_type == 'ebook':
            return  query_set.filter(vendorlink__format__exact='EBOOK').distinct()
        if pub_type == 'print':
            return query_set.filter(vendorlink__format__exact='PAPERBACK').distinct()

        return query_set.order_by('-pub_date')

    def render_to_response(self, context, **kwargs):
        context.update({'request': self.request})
        return super(ListView, self).render_to_response(context, **kwargs)

    template_name = "books/list_view.html"


class RomanceList(ListView):

    context_object_name = "book_list"
    model = Book

    def get_queryset(self):
        query_set = Book.objects.filter(genre='ROMANCE')
        return query_set.order_by('-pub_date')

    def render_to_response(self, context, **kwargs):
        context.update({'request': self.request})
        return super(RomanceList, self).render_to_response(context, **kwargs)

    template_name = "books/megmaguire/list_view.html"


class BookDetail(DetailView):
    template_name = "books/book_detail.html"
    model = Book


class Home(TemplateView):
    template_name = "books/index.html"


class About(TemplateView):
    template_name = "books/contact.html"
