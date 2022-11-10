from django.views.generic import ListView, DetailView
from .models import Book
# Create your views here.
class BookListView(ListView):
 model = Book
 context_object_name = 'book_list'
 template_name = 'books/book_list.html'
class BookDetailView(DetailView):
 model = Book
 template_name = 'books/book_detail.html'

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfileEditView(UpdateView):
    model = Profile
    template_name ='registration/edit_profile.html'
    fields = ['fav_author']
    success_url = reverse_lazy('home')

class ProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'