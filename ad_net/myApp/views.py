from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Article
import json
# Create your views here.

def index(request):
    return JsonResponse({"page":"index"},safe=False)

def getArticle(request):
    try:
        al = Article.objects.filter(status = True)
        als = [{"id":i.id,"title":i.title,"description":i.description,"auteur":i.source,"date_add":i.date_add,"date_update":i.date_update} for i in al]
        return JsonResponse({"status":True,"result":als},safe=False)
    except Exception as e:
        print("Erro to gt all article ",e)

@csrf_exempt 
def addArticle(request):
    if request.method == "POST":
        try:
            pars_data = json.loads(request.body.decode("utf-8"))
            newArticle = Article(title = pars_data["title"],url_image = pars_data["urlImage"],description = pars_data["description"],source = pars_data["source"])
            newArticle.save()
            return JsonResponse({"status":True,"reponse":"enregitrement ok "})


        except Exception as e:
            print("Error post metho",e)
            return JsonResponse({"status":False,"reponse":str(e)},safe=False)
       
       



