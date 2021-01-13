from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse

from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'prod/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'prod/post_detail.html', {'post':post})