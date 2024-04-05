
from django import template
from blog.models import Post, Category, Comment

register = template.Library()


@register.simple_tag(name = 'comment_count') # run func with no arguments
def function(pid):
    return Comment.objects.filter(post = pid, approved = True).count()

@register.filter # filter functions by format string
def func():
    pass   

@register.inclusion_tag("blog/test.html") # تابع را زمانی فراخوانی کنیم اجرا میشود خروجی را به آن صفحه میدهد و بعد آن صفحه را جایگزین میکند
def func():
    pass

@register.inclusion_tag("blog/last_post.html")
def last_post(arg = 3):
    posts = Post.objects.filter(status=True)[:arg]
    return {'posts': posts}

@register.inclusion_tag("blog/post_category.html")
def post_category():
    category_count = {}
    categories = Category.objects.all()

    for category in categories:
        # بدست آوردن تعداد پست‌های هر دسته‌بندی
        post_count = Post.objects.filter(category=category, status=True).count()

        category_count[category] = post_count

    return {'category_count': category_count}

    