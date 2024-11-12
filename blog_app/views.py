from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post


# Представление без выбора количества страниц
# def post_list(request):
#     posts = Post.objects.all()
#     paginator = Paginator(posts, 3)
#     page_number = request.GET.get('page')         # получаем номер страницы, на которую переходит пользователь
#     try:
#         page_posts = paginator.get_page(page_number)  # получаем посты для текущей страницы
#     except PageNotAnInteger:
#         page_posts = paginator.page(1)
#     except EmptyPage:
#         page_posts = paginator.page(paginator.num_pages)
#     context = {'page_posts': page_posts}
#     return render(request, 'post_list.html', context)


# Представление с выбором страниц
def post_list(request):
    posts = Post.objects.all()
    posts_per_page = request.GET.get('posts_per_page', 5)  # Задает число постов по умолчанию 5
    paginator = Paginator(posts, posts_per_page)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    return render(request, 'post_per_list.html',
                  {'page_posts': page_posts, 'posts_per_page': posts_per_page})
