from django.shortcuts import render
from .models import *
from django import forms

from django.http import HttpResponse
# Create your views here.
HTTP ='http://'



class client:
    def index(request):
        slides      = Slide.objects.filter(status=1)
        category    = Category.objects.filter(status=1)
            

        news  = New.objects.filter(status=1).order_by('-id')[:4:1]
        
        return render(request,'index.html',{'slides':slides,'news':news,'categories':category})


    def new_detail(request,id,path):
        if(request.method =="POST"):
            form = request.POST
            model = Comment()
            model.name =form['email']
            model.content =form['content']
            model.sub_comment =0
            model.new_id_id =id
            model.save()

            return HttpResponse(True)
            
        else:
    
            new     =   New.objects.get(id=id,status=1)
            base_url=   HTTP+request.META['HTTP_HOST']
            date    =   new.updated_at.strftime('%d')
            month    =   new.updated_at.strftime('%b')
            return render(request,'news/detail.html',{'new':new,'base_url':base_url,'date':date,'month':month})
