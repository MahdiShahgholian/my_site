from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, EmptyPage
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import messages

def blog_home_view(request, **kwargs):
    
    posts = Post.objects.filter(status=True)
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_name'):
        posts = posts.filter(author__username=kwargs['author_name'])
    if kwargs.get('tag_name') :
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
        
    posts = Paginator(posts, 3)  # Show 3 contacts per page.
    
    try:
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)
    except EmptyPage:
        posts = posts.page(1)
    except EmptyPage:
        posts = posts.page(posts.num_pages)
    
    tags = Post.tags.all()
    
    
    context = {'posts': posts , 'tags': tags}
    return render(request, 'blog/blog-home.html', context)



def blog_single_view(request, pid):
    posts = Post.objects.filter(status=True)
    post = get_object_or_404(Post, id=pid, status=True)

    post_ids = [p.id for p in posts]

    current_post_index = post_ids.index(int(pid))

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

    comments = Comment.objects.filter(post = post, approved = True)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
        else:
            messages.error(request, 'Form submission successful')
            
    form = CommentForm()     
    
    context = {
        'post': post,
        'next_post': next_post,  
        'prev_post': prev_post,
        'comments' : comments,
        'form': form
           
    }

    return render(request, 'blog/blog-single.html', context)


def search_view(request):
    # فیلتر کردن تمام پست‌های فعال
    posts = Post.objects.filter(status=True)
    
    if request.method == 'GET':
        # درخواست جستجو از روی محتوای پست‌ها
        search_query = request.GET.get('s')  # دریافت متن جستجو شده، اگر وجود دارد
        if search_query:
            # فیلتر کردن پست‌ها بر اساس متن جستجوی وارد شده
            posts = posts.filter(content__contains=search_query)
    
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)
