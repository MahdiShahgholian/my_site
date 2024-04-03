from django.shortcuts import render, get_object_or_404
from .models import Post

def blog_home_view(request, cat_name=None, author_name=None):
    posts = Post.objects.filter(status=True)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_name:
        posts = posts.filter(author__username=author_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single_view(request, pid):
    posts = Post.objects.filter(status=True)
    post = get_object_or_404(Post, id=pid, status=True)

    # ایجاد لیست آیدی پست‌ها
    post_ids = [p.id for p in posts]

    # پیدا کردن آیدی پست فعلی
    current_post_index = post_ids.index(int(pid))

    # دریافت آیدی پست بعدی و پیشین
    next_post_index = current_post_index + 1
    prev_post_index = current_post_index - 1

    next_post = None
    prev_post = None

    if next_post_index < len(post_ids):
        next_post_id = post_ids[next_post_index]
        next_post = Post.objects.get(id=next_post_id)

    if prev_post_index >= 0:
        prev_post_id = post_ids[prev_post_index]
        prev_post = Post.objects.get(id=prev_post_id)

    context = {
        'post': post,
        'next_post': next_post,  # ارسال پست بعدی به قالب
        'prev_post': prev_post   # ارسال پست قبلی به قالب
    }

    return render(request, 'blog/blog-single.html', context)
