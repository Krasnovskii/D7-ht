from django.contrib import admin
from .models import Book
from .models import Author
from .models import PublishHouse
from .models import Friend
from .models import UserProfile


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author_full_name')
    # fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'publish_house', 'price')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(PublishHouse)
class PublishHouseAdmin(admin.ModelAdmin):
    pass


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass