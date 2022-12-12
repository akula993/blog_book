from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from blog.models import Post


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)  # По 3 статьи на каждой странице
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, возвращаем первую страницу.
        posts = paginator.page(1)
    except EmptyPage:
        # Если номер страници больше, чем общее количество страниц, возвращаем последюю.
        posts = paginator.page(paginator.num_pages)

    context = {
        'page': page,
        'posts': posts,
    }

    return render(request, 'blog/post/list.html', context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month,
                             publish__day=day)
    title = Post.title
    context = {
        'title': title,
        'post': post,
    }
    return render(request, 'blog/post/detail.html', context)
