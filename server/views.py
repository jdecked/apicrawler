from django.shortcuts import render
from .models import APIDefinition, APICrawler

def index(request):
    crawler = APICrawler("https://apis-guru.github.io/api-models/")
    crawler.crawl()
    results = APIDefinition.objects.all()

    context = {'results': results}    

    return render(request, 'index.html', context)
