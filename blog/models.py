from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    make_email_anonomous = models.BooleanField(default=True)
    bio = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['last_name']


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)  # Make unique true so you don't reuse a title.
    slug = models.SlugField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=True)
    author = models.ForeignKey(Author)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-creation_date']
