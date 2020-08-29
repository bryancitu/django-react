from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField('name', max_length=30)
    description = models.TextField('description', blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='user', blank=True, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('tag')
        verbose_name_plural = ('tags')


class Link(models.Model):
    name = models.CharField('name', max_length=30)
    url = models.URLField('url')
    pending = models.BooleanField('pending', default=False)
    description = models.TextField('description', blank=True, null=True)
    tags = models.ManyToManyField(Tag, through='LinkTag', editable=True)
    user = models.ForeignKey(User, verbose_name='user',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'link'
        verbose_name_plural = 'links'


class LinkTag(models.Model):
    link = models.ForeignKey(Link, verbose_name='link',on_delete=models.CASCADE)

    tag = models.ForeignKey(Tag, verbose_name='tag',on_delete=models.CASCADE)


    class Meta:
        unique_together = (('link', 'tag'))
        verbose_name = 'link x tag'
        verbose_name_plural = 'link x tag'