# -*-coding: utf-8 -*-
#!/usr/bin/env python
from django.shortcuts import render_to_response,get_object_or_404,render
from django.template import RequestContext
from models import Book
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage
from django.db import connection

import sys
def index(request):
    booklist = Book.objects.select_related().order_by('-id')
    print connection.queries
    page = request.POST.get('page', 1)
    paginator = Paginator(booklist, 5)
    try:
        booklist = paginator.page(page)
    except PageNotAnInteger:
        booklist = paginator.page(1)
    except EmptyPage:
        booklist = paginator.page(paginator.num_pages)
    return render_to_response('index.html', {'booklist':booklist, 'currentPage':page, 'numPerPage':5})
