from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from mysite.forms import PostForm,CommentForm
from django.views.generic import (ListView,CreateView,
                                  DeleteView,UpdateView,
                                  DetailView)
from mysite.models import Post,Comment
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

class PostListView(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name=''

    form_class = PostForm
    model = Post

class UpdatePostView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = ''

    model = Post

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = ''

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-created_date')

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = POST
    success_url = reverse_lazy('')

####################################
## Functions requires pk to match ##
####################################


@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('',pk=pk)


@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    request.method == "POST"
    comment = CommentForm(request.post)
    if comment.is_valid():
        comment = comment.save(commit = False)
        comment.post = post
        comment.save()
        return redirect(request,'',pk = post.pk)
    else:
        form = CommentForm()
    return render(request,'',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('',pk=post_pk)
