# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import os

from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from ID import settings
from app.models import IMG
from utils.indentify import front_picture_identify, back_picture_identify


def index(request):
    return render(request, 'index.html')

def uploadFrontImg(request):
    if request.method == 'POST':
        if not os.path.exists('material'):
            os.makedirs('material')
        img = request.FILES.get('img')
        new_img = IMG(
            img=request.FILES.get('img')
        )
        new_img.save()
        filename=new_img.img.name
        print(filename)
        filedir=os.path.join(settings.BASE_DIR,'media')
        print(filedir)
        path=os.path.join(filedir,filename).replace("/","\\")
        print(path)
        data = front_picture_identify(path,False)
        return HttpResponse(data)
    context = {}
    context['flag'] = 'uploadFrontImg'
    return render(request, 'uploadimg.html',context)

def uploadBackImg(request):
    if request.method == 'POST':
        if not os.path.exists('material'):
            os.makedirs('material')
        img = request.FILES.get('img')
        new_img = IMG(
            img=request.FILES.get('img')
        )
        new_img.save()
        path = settings.BASE_DIR+"/media/material/"+img.name
        data = back_picture_identify(path,False)
        return HttpResponse(data)
    context = {}
    context['flag'] = 'uploadBackImg'
    return render(request, 'uploadimg.html', context)


