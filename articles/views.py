from django.http.response import Http404
from articles.models import Article
from django.shortcuts import redirect, render
from django.http import Http404,HttpResponseRedirect
from .forms import ArticleForm
from django.urls import reverse
# Create your views here.

def article_view(request):
    articles = Article.objects.all()
    contex = {'articles':articles}
    return render(request,'articles/articles.html',contex)

# def show_article(request, slug):
#     try:
#         article = Article.objects.get(slug)
#         return render(request,'articles/show_article.html')
#     except Article.DoesNotExist:
#         raise Http404("L'article n'existe pas")
def create_view(request):
    form = ArticleForm()
    if request.method=='POST':
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            #return redirect('/')
            # return HttpResponseRedirect('/articles/')
            return HttpResponseRedirect(reverse('blog'))
    form = ArticleForm()
    contex = {'form':form}
    return render(request,'articles/create.html',contex)


def show_view(request,id):
    article = Article.objects.get(id=id)
    context = {'article':article}
    return render(request,'articles/show.html',context)