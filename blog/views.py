from django.views.generic import ListView, DetailView, UpdateView, DeleteVie
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class BlogListView(ListView)
    model = Post
    template_name = 'home.html'
    


class BlogDetailView(DetailView):
    model = Post
    template_name= 'post_detail.html'
    

class BlogCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Post
    template_name = 'post_new.html'
    fields= "__all__"

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Post
    template_name = 'post_edit.html'
    fields=['title', 'body']

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Post
    template_name= 'post_delete.html'
    success_url = reverse_lazy('home')
    
