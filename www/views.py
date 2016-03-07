# encoding:utf-8
from django.shortcuts import render
from www.models import User, News, Category
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from django.http import JsonResponse
# Create your views here.

def news(requests, id):
	try:
		news = News.objects.get(id=id)
		return render_to_response('news.html', locals())
	except:
		raise Http404()

def index(requests):
	try:
		categorys = Category.objects.all()
		newses = News.objects.all()
		scoops = Category.objects.get(name='要闻').news_set.all().order_by('-timestamp')
		finances = Category.objects.get(name='财经').news_set.all()
		societies = Category.objects.get(name='社会').news_set.all()
		return render_to_response('index.html', locals())
	except:
		raise Http404()

def about(requests):
	return render_to_response('about.html')

def api_news(requests):
	try:
		newses = News.objects.all()
		response_data = {}
		response_data['status'] = True
		
		return render_to_response('news.html', locals())
	except:
		raise Http404()