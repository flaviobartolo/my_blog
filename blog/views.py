from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Post

import logging

# Create your views here.

def starting_page(request):

  latest_posts = Post.objects.all().order_by('-date')[:3]

  return render(request, 'blog/index.html', {'posts': latest_posts})

def posts(request):
  all_posts = Post.objects.all().order_by('-date')
  return render(request, 'blog/all-posts.html', {'all_posts': all_posts})

def post_detail(request, slug):
  post = get_object_or_404(Post, slug=slug)
  return render(request, 'blog/post_detail.html', {
    'post': post,
    'tags': post.tags.all(),
  
  })
