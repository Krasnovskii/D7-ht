from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

# from .views import index
from .views import AuthorEdit, AuthorList, author_create_many, books_author_create_many
from .views import FriendEdit, FriendList, BookCreate, BookUpdate
from .views import list_biblio
from .views import book_decrement, book_increment

from allauth.account.views import login, logout
from .views import index, RegisterView, CreateUserProfile
from django.urls import reverse_lazy



app_name = 'p_library'
urlpatterns = [
    path('', index, name='index'),
    path('list_biblio/', list_biblio, name='list_biblio'),
    path('author/create', AuthorEdit.as_view(), name='author_create'),
    path('authors', AuthorList.as_view(), name='author_list'),
    path('author/create_many', author_create_many, name='author_create_many'),
    path('author_book/create_many', books_author_create_many, name='books_author_create_many'),
    path('friend/create', FriendEdit.as_view(), name='friend_create'),
    path('friends', FriendList.as_view(), name='friend_list'),
    # path('', StartTemplate.as_view()),
    path('book/create', BookCreate.as_view()),
    path('book/update/<int:pk>', BookUpdate.as_view()),
    path('index/book_increment/', book_increment),
    path('index/book_decrement/', book_decrement),

    path('login/', login, name='login'),  
    path('logout/', logout, name='logout'),
	path(
        'register/',
        RegisterView.as_view(
            template_name='register.html',
            success_url=reverse_lazy('p_library:profile-create')
        ),
        name='login'
    ),
    path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += staticfiles_urlpatterns()
