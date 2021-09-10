from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Post

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'blog/index.html', context)


def details(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post':post}
    return render(request, 'blog/detail.html', context)