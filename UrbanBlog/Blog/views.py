from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *

# Create your views here.

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')

    posts_per_page = request.GET.get('posts_per_page', 10)
    paginator = Paginator(posts, int(posts_per_page))

    page_number = request.GET.get('page')
    try:
        page_posts = paginator.page(page_number)
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)

    return render(request, 'post_list.html', {
        'page_posts': page_posts,
        'posts_per_page': posts_per_page
    })
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})