from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView
from mysite.models import Post,Comment
# Create your views here.

class PostListView(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post
