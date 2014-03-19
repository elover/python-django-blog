#-*- coding:utf-8 -*-
# Create your views here.
import random
from django.core.mail import send_mail

from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.urlresolvers import reverse
import locale
from blog.models import Articles
from blog.models import Category
from blog.forms import ContactForm
from django.views.decorators.cache import cache_control


def pagination(request1, articles_list):
    '''
    分页
    '''
    # 分页 每页5骗
    pagination = {"perPageNumber": 5}
    # 每页文章篇数
    pagination['pageTotal'] = len(articles_list) / pagination["perPageNumber"]
    if len(articles_list) % pagination["perPageNumber"] > 0:
        pagination['pageTotal'] += 1
    pagination['pageTotal_list'] = range(1, pagination['pageTotal'] + 1)
    pagination['pageNumber'] = 0
    cur_articles_list = articles_list[0:pagination["perPageNumber"]]
    if "pageNumber" in request1.GET:
        pageNumber = int(request1.GET['pageNumber'])
        pagination['pageNumber'] = pageNumber
        # if request.GET['pageNumber'] != None:
        prePage = (pageNumber - 1) * pagination["perPageNumber"]
        nextPage = pageNumber * pagination["perPageNumber"]
        cur_articles_list = articles_list[prePage:nextPage]
    return [cur_articles_list, pagination]


@cache_control(must_revalidate=True, max_age=360)
def index(request):
    articles_list = Articles.objects.all()
    allCategory = Category.objects.all()
    respone_list = pagination(request, articles_list)
    randomStatus = random.choice([True, False])
    context = {'latest_articles_list': respone_list[0], "randomStatus": randomStatus, "pagination": respone_list[1],
               "allCategory": allCategory}
    return render(request, 'mainTem/index.html', context)


@cache_control(must_revalidate=True, max_age=360)
def article(request, article_id):
    content = get_object_or_404(Articles, pk=article_id)
    content.count += 1
    content.save()
    allCategory = Category.objects.all()
    context = {'content': content, "allCategory": allCategory}
    return render(request, 'mainTem/article.html', context)


@cache_control(must_revalidate=True, max_age=360)
def list(request):
    articles_list = Articles.objects.order_by('-pub_date').all()
    allCategory = Category.objects.all()
    randomStatus = random.choice([True, False])
    content = {'articles_list': articles_list, "randomStatus": randomStatus, "allCategory": allCategory}

    return render(request, 'mainTem/list.html', content)


@cache_control(must_revalidate=True, max_age=360)
def category(request, slug):
    category_list = get_object_or_404(Category, slug=slug)
    articles_list = category_list.articles_set.all()
    allCategory = Category.objects.all()
    respone_list = pagination(request, articles_list)
    randomStatus = random.choice([True, False])
    context = {'latest_articles_list': respone_list[0], "randomStatus": randomStatus, "pagination": respone_list[1], "allCategory": allCategory,
               "currentSlug": slug}
    return render(request, 'mainTem/index.html', context)


def info(request):
    t = str(locale.getdefaultlocale())
    return HttpResponse(str(request))


@cache_control(must_revalidate=True, max_age=360)
def music(request, article_id):
    content = get_object_or_404(Articles, pk=article_id)
    context = {"content": content}
    return render(request, 'mainTem/music.html', context)


def postArticle(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            p1 = Articles(h1=cd['h1'], content=cd['content'], author_id=cd['author'], category_id=cd['category'])
            p1.save()
            return HttpResponseRedirect('/postArticle/thanks')
    else:
        if request.META.get("HTTP_REFERER") and request.META.get("HTTP_REFERER").find("invite") != -1:
            form = ContactForm()
        else:
            return HttpResponseRedirect('/invite/')

    return render(request, 'mainTem/postArticle.html', {"form": form})


def invite(request):
    if request.method == "POST":
        if request.POST["invite"] == "thinkjoy":
            return HttpResponseRedirect('/postArticle/')
        else:
            return render(request, 'mainTem/invite.html', {"error": True})

    else:
        return render(request, 'mainTem/invite.html')


def changeLog(request):
    allCategory = Category.objects.all()
    context = {"allCategory": allCategory}
    return render(request, 'mainTem/changeLog.html', context)



