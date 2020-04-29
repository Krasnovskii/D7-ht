from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from .models import Book, Author, Friend, UserProfile
from .forms import AuthorForm, BookForm, FriendForm, BookUpdateForm
from django.views.generic import CreateView, ListView, TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic.base import View
from django.urls import reverse_lazy
from django.forms import formset_factory
from django.http.response import HttpResponseRedirect
import uuid
from django.conf import settings

from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileCreationForm

from django.contrib.auth import login, authenticate
from allauth.socialaccount.models import SocialAccount
from django.views.generic import FormView


def get_users_data(request):
    context = {}
    try:
        if request.user.is_authenticated:
            context['username'] = request.user.username
        try:
            context ['github_url'] = (
                    SocialAccount.objects.get(
                        provider='github',
                        user=request.user
                    ).extra_data['html_url'])
        except:
            context ['github_url'] = ''
        return context
    except:
        context['username'] = ''
        return context


class AuthorEdit(CreateView):
    # Добавление автора
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'authors_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_users_data(self.request))
        return context


class AuthorList(ListView):
    model = Author
    template_name = 'authors_list.html'
    # paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_users_data(self.request))
        return context


class FriendEdit(CreateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'friend_edit.html'


class FriendList(ListView):
    model = Friend
    template_name = 'friend_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_users_data(self.request))
        return context

class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('p_library:index')
    template_name = 'book_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_users_data(self.request))
        return context



class BookUpdate(UpdateView):
    model = Book
    template_name = 'book_edit.html'
    form_class = BookUpdateForm
    # form_class = BookForm
    success_url = reverse_lazy('p_library:list_biblio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_users_data(self.request))
        return context


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def author_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')
        if author_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
    return render(request,
                  'manage_authors.html',
                  {
                      'author_formset': author_formset,
                  }
                  )


def books_author_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    BookFormSet = formset_factory(BookForm, extra=2)
    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')
        if author_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            for book_form in book_formset:
                book_form.save()
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
        book_formset = BookFormSet(prefix='books')
    return render(request,
                  'manage_books_authors.html',
                  {
                      'author_formset': author_formset,
                      'book_formset': book_formset,
                  }
                  )



class RegisterView(FormView):
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        login(self.request, authenticate(
            username=username,
            password=raw_password
        ))
        return super(RegisterView, self).form_valid(form)


class CreateUserProfile(FormView):
    form_class = ProfileCreationForm
    template_name = 'profile-create.html'
    success_url = reverse_lazy('p_library:index')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return HttpResponseRedirect(reverse_lazy('p_library:login'))
        return super(CreateUserProfile, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super(CreateUserProfile, self).form_valid(form)


def index(request):
    template = loader.get_template('index.html')
    context = get_users_data(request)
    return HttpResponse(template.render(context, request))


def list_biblio(request):
    template = loader.get_template('list_biblio.html')
    books = Book.objects.all()
    context = {
        "title": "мою библиотеку",
        "books": books,
    }
    context.update(get_users_data(request))
    return HttpResponse(template.render(context, request))
