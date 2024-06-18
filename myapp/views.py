from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from myapp.models import Posts, Category  # Ensure Category is imported

# Create your views here.

menu = [{'title': 'Добавить новость', 'url_name': 'index'}, {'title': "О нас", 'url_name': 'about'}]

def category(request, catid):
    return HttpResponse(f"Вы на странице категории {catid}")

def index(request):
    all_posts = Posts.objects.all()
    categ = Category.objects.all()  # Corrected usage of Category
    return render(request, 'app/home.html', {'title': 'Главная страница', 'menu': menu, 'all': all_posts, 'categ': categ})

def PageNotFound(request, exception):
    return HttpResponseBadRequest("Вы ошиблись")

def about(request):
    return render(request, 'app/about.html', {'title': 'О сайте'})


from django.shortcuts import render, get_object_or_404
from .models import Posts, Category

def show_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    categ = Category.objects.all()
    return render(request, 'app/post.html', {
        'title': post.title,
        'menu': menu, 
        'post': post,  
        'categ': categ
    })


def show_category(request, category_id):
    # return HttpResponse(f"Категория под номером {category_id}")

    all_posts = Posts.objects.filter(category_id=category_id)
    categ = Category.objects.all()
    return render(request, 'app/home.html', {'title': 'Главная страница', 'menu': menu, 'all': all_posts, 'categ': categ})



































