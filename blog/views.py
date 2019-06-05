from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from django.core.paginator import Paginator
# Create your views here.
# request 为http请求参数
def HelloWorld(request):
    return HttpResponse("Hello World")

def content(request):
    article=Article.objects.all()[0]
    title=article.title
    abstract=article.abstract
    content=article.content
    articleId=article.articleId
    publishData=article.publishData
    return_str='title:%s,abstract:%s,content:%s,articleId:%s,publishData:%s' % (title,abstract,content,articleId,publishData)
    return HttpResponse(return_str)

def getIndexPage(request):
    page=request.GET.get('page')
    if page:
        page=int(page)
    else:
        page=1
    print('page pram:',page)
    allArticles=Article.objects.all()
    top_atricles_list=Article.objects.order_by('-publishData')[:5]
    paginator=Paginator(allArticles,3)
    page_num=paginator.num_pages
    page_articles=paginator.page(page)
    if page_articles.has_next():
        next_page=page+1
    else:
        next_page=page
    if page_articles.has_previous():
        previous_page=page-1
    else:
        previous_page=1

    return render(request,'blog/index.html',{
        'articleList':page_articles,
        'page_num':range(1,page_num+1),
        'cur_page':page,
        'next_page':next_page,
        'previous_page':previous_page,
        'top_articles_list':top_atricles_list
    })

def getDetailPage(request,articleId):
    allArticles=Article.objects.all()
    curr_article=None
    previousIndex=0
    nextIndex=0
    for index,article in enumerate(allArticles):
        if (index==0):
            previousIndex=0
            nextIndex=index+1
        elif(index==len(allArticles)-1):
            previousIndex=index-1
            nextIndex=index
        else:
            previousIndex=index-1
            nextIndex=index+1
        if article.articleId==articleId:
            curr_article=article
            previousArticle=allArticles[previousIndex]
            nextArticle=allArticles[nextIndex]
            break
    sectionList=curr_article.content.split('\n')
    return render(request,'blog/detail.html',{
        'curr_article':curr_article,
        'sectionList':sectionList,
        'previousArticle':previousArticle,
        'nextArticle':nextArticle
    })
