from django.db import models
from django.contrib.auth.models import User  


class Author(models.Model):
    full_name = models.TextField('Имя')
    birth_year = models.SmallIntegerField(verbose_name='День рождения')
    country = models.CharField(max_length=2, verbose_name='Страна')

    def __str__(self):
        return self.full_name


class PublishHouse(models.Model):
    publish_house_name = models.CharField('Издательство', max_length=30)
    publish_housse_sity = models.CharField('Город', max_length=20)

    def __str__(self):
        return self.publish_house_name


class Friend(models.Model):
    name_friend = models.CharField('Имя', max_length=20)

    def __str__(self):
        return self.name_friend


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField('Наименование')
    description = models.TextField('О книге')
    year_release = models.CharField('Год публикации', max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish_house = models.ForeignKey(
        PublishHouse,
        on_delete=models.CASCADE,
        default=1
    )
    copy_count = models.SmallIntegerField('Кол-во книг', default=1)
    price = models.DecimalField('Цена', max_digits=19, decimal_places=2)
    friend = models.ForeignKey(
        Friend,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='uploads/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    def __str__(self):
        return self.user.username