import itertools
from django.db import models
from autoslug import AutoSlugField


class Theme(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    GENRE_CHOICES = (('ROMANCE','Romance'),
                     ('EROTICA', 'Erotic Romance'),
                     ('LITERARY', 'Literary Fiction'))
    AUTHOR_CHOICES = (('MEG', 'Meg Maguire'),
                      ('CARA', 'Cara McKenna'))

    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published', null=True, blank=True)
    text = models.TextField(blank=True)
    isbn = models.CharField(max_length=200, blank=True)
    publisher = models.ForeignKey(Publisher, null=True, blank=True)
    theme = models.ManyToManyField(Theme, blank=True)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    cover_image = models.FileField(blank=True)
    thumbnail_image = models.FileField(blank=True)
    publisher_link = models.URLField()
    excerpt = models.URLField(null=True, blank=True)
    author = models.CharField(max_length=50, choices=AUTHOR_CHOICES)
    related = models.ManyToManyField('self', blank=True)
    slug = AutoSlugField(populate_from='title', unique=True, editable=True, null=True)


    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.title

    def get_ebook_vendors(self):
        return self.vendorlink_set.filter(format='EBOOK')

    def get_paperback_vendors(self):
        return self.vendorlink_set.filter(format='PAPERBACK')

    def get_audio_vendors(self):
        return self.vendorlink_set.filter(format='AUDIO')

    def get_reviews(self):
        return self.review_set.all()

    def get_series(self):
        try:
            series = Series.objects.get(seriesentry__book_id=self.id)
        except:
            series = None
        return series

    def get_other_books(self):
        series = self.get_series()
        if series:
            books = [se.book for se in SeriesEntry.objects.filter(series=series).order_by('number')]
        else:
            books = self.related.all()
        # Create list of chunks of 3 books
        books = [books[i:i+3] for i in xrange(0, len(books), 3) ]
        return books

    def get_other_books_count(self):
        books = self.get_other_books()
        # Flatten
        books = list(itertools.chain(*books))
        # Return a count of chunks of size 3
        # Example, if len is 4, then [0,1]
        return [i for i in range(len(books)) if i*3 < len(books)]


class VendorLink(models.Model):
    FORMAT_CHOICES = (('EBOOK', 'e-book'),
                      ('PAPERBACK', 'paperback'),
                      ('AUDIO', 'audio'),)

    name = models.CharField(max_length=200)
    url = models.URLField()
    format = models.CharField(max_length=50, choices=FORMAT_CHOICES)
    book = models.ForeignKey(Book)

    def __unicode__(self):
        return self.book.title + " - " + self.name


class Review(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    url = models.URLField()
    book = models.ForeignKey(Book, related_name='reviews')
    source = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.book.title + " - " + self.source


class Series(models.Model):

    class Meta:
        verbose_name_plural = 'Series'

    name = models.TextField()

    def __unicode__(self):
        return self.name


class SeriesEntry(models.Model):

    class Meta:
        verbose_name_plural = 'Series Entries'
    book = models.ForeignKey(Book, related_name='series')
    series = models.ForeignKey(Series)
    number = models.IntegerField()

    def __unicode__(self):
        return self.series.name + ' - ' + self.book.title + ' ' + str(self.number)


class SiteImage(models.Model):
    image = models.FileField()

    def __unicode__(self):
        return self.image.url
