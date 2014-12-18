# -*-coding: utf-8 -*-
#!/usr/bin/env python
from django.http import HttpResponse
from django.shortcuts import render_to_response,get_object_or_404,render
from django.template import RequestContext
from models import Book
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
import sys
def index(request):
    booklist = Book.objects.select_related()
    print booklist
    page = request.POST.get('page', 1)
    paginator = Paginator(booklist, 5)
    try:
        booklist = paginator.page(page)
    except PageNotAnInteger:
        booklist = paginator.page(1)
    except EmptyPage:
        booklist = paginator.page(paginator.num_pages)
    return render_to_response('index.html', {'booklist':booklist, 'currentPage':page, 'numPerPage':5})

def list_book(request):

    return render_to_response('list_book.html', locals())

def list_book_data(request):
    #response = HttpResponse()
    #response['Content-type'] = "text/javascript"

    bookData = Book.objects.select_related()
    #response.write(serializers.serialize("json", bookData))
    #return response
    #response_data = {}
    #response_data['result'] = 'failed'
    #response_data['message'] = 'You messed up'
    return HttpResponse(json.dumps(bookData,ensure_ascii = False), content_type="application/json")
    #return render_to_response('simpleTodo.html', {'todolist': todolist},
    #    context_instance=RequestContext(request))