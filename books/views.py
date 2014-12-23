# -*-coding: utf-8 -*-
#!/usr/bin/env python
from django.http import HttpResponse
from django.shortcuts import render_to_response,get_object_or_404,render
from django.template import RequestContext
from books.models import Book,Author,Publisher
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.views.decorators.csrf import ensure_csrf_cookie
import json
import sys
import math
reload(sys)  #重新加载sys
sys.setdefaultencoding('utf8')  ##调用setdefaultencoding函数
def index(request):
    booklist = Book.objects.select_related()


def index(request):
    booklist = Book.objects.select_related()
    page = request.GET.get('page', 1)
    print "dddd" + str(page)
    paginator = Paginator(booklist, 5)
    try:
        booklist = paginator.page(page)
    except PageNotAnInteger:
        booklist = paginator.page(1)
    except EmptyPage:
        booklist = paginator.page(paginator.num_pages)
    return render_to_response('index.html', {'booklist':booklist, 'currentPage':page, 'numPerPage':5})


def add_book(request):
    if request.method == 'POST':
        title = request.POST['book_name']
        publisher = request.POST['publisher']
        publish_date = request.POST['publish_date']

        authors = request.POST['authorIDs[]']
        print authors
        book = Book(title=title, publication_date = publish_date, publisher_id = authors)

        for item in authors:
            author = Book.objects.get_or_create(name=item)
            Book.authors.add(author)
        book.save()
    else:
        authors = Author.objects.all()
        publishers = Publisher.objects.all()
        return render_to_response('add_book.html', locals())


    '''
     if request.method == 'POST':

        #logger = logging.getLogger('mylogger')
        #记录log
        atodo = request.POST['todo']
        priority = request.POST['priority']
        user = User.objects.get(id='1')
        todo = Todo(user=user, todo=atodo, priority=priority, flag='1')

        todo.save()
        todolist = Todo.objects.filter(flag='1')
        finishtodos = Todo.objects.filter(flag=0)
        return render_to_response('showtodo.html',
            {'todolist': todolist, 'finishtodos': finishtodos},
            context_instance=RequestContext(request))
    else:
        todolist = Todo.objects.filter(flag=1)
        finishtodos = Todo.objects.filter(flag=0)
        return render_to_response('simpleTodo.html',
            {'todolist': todolist, 'finishtodos': finishtodos})
    '''


@ensure_csrf_cookie
def list_book(request):
    return render_to_response('list_book.html', {})

@ensure_csrf_cookie
def list_book_data(request):
    bookData = Book.objects.all()
    num = bookData.count()
    page = request.REQUEST.get('page', 1)
    perpage = 3
    paginator = Paginator(bookData, perpage)
    try:
        bookData = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.num_pages;
        bookData = paginator.page(page)
    except EmptyPage:
        page = 1;
        bookData = paginator.page(page)
    data = {}
    data['rows'] = []
    '''
    if int(page) != 1:
        prevHtml = "<a id=\"prev\" rel=\"%s\" >Prev</a>" % bookData.previous_page_number()
    else:
        prevHtml = ""

    if int(page) < paginator.num_pages:
        nextHtml = "<a id=\"next\" rel=\"%s\">Next</a>" %  bookData.next_page_number()
    else:
        nextHtml = ""
    #data['pagehtml'] = prevHtml + nextHtml
    '''
    data['pagehtml'] = ajax_pages(num, int(page), perpage)
    for item in bookData:
        row = {}
        row['title'] = item.title
        row['name'] = item.publisher.name
        row['address'] = item.publisher.address
        authorsData = item.authors.all()
        authorName = ""
        for author in authorsData:
            authorName = author.name + ',' + authorName
        row['authorName'] = authorName
        data['rows'].append(row)
    return HttpResponse(json.dumps(data), content_type="application/json")

def ajax_pages(num, current_page, perpage = 5, setpages = 10):
    if int(num) < 0:
        return ''
    multipage = ""
    if num > perpage:
        page = setpages + 1
        offset = int(math.ceil(setpages))
        pageNumbers = float(num/float(perpage))
        pages = int(math.ceil(pageNumbers))
        print "page = " + str(pages) + 'current_page=' + str(current_page) + 'perpage' + str(perpage)
        froms = int(current_page) - int(offset)
        to = int(current_page) + int(offset)
        more = 0
        if page >= pages:
            froms = 2
            to = pages-1
        else:
            if froms <= 1:
                to = page-1
                froms = 2
            elif to >= pages:
                froms = pages-(page - 2)
                to = pages - 1
            more = 1
        multipage += "<span class=\"a1\" href=\"javascript:void(0);\" >sum %s </span>" % num
        if current_page > 0 :
            multipage += ' <a href="javascript:void(0);" class="a1" rel="%s">Prev</a>' % (current_page - 1)
            if current_page == 1:

                multipage += ' <span class="current">1</span>'
            elif current_page > 6 and more == 1:
                multipage += ' <a rel="1" href="javascript:void(0);">1</a>..'
            else:
                multipage += ' <a rel="1" href="javascript:void(0);">1</a>'
        for i in range(int(froms), int(to) + 1):
            print "i ====" + str(i)
            if i != current_page:
                multipage += ' <a rel="%s" href="javascript:void(0);">%s</a>' % (i, i)
            else:
                multipage += ' <span class="current">%s</span>' % i
        if current_page < pages:
            if current_page < pages - 5 and more == 1:
                multipage += '..<a  rel="%s" href="javascript:void(0);">%s</a> <a rel="%s" href="javascript:void(0);" class="a1">Next</a>' % (pages, pages, int(current_page) + 1)
            else:
                multipage += ' <a rel="%s" href="javascript:void(0);">%s</a> <a rel="%s" href="javascript:void(0);" class="a1">Next</a>'% (pages, pages, int(current_page) + 1)
        elif current_page == pages:
            multipage += '<span class="current">%s</span> <a href="javascript:void(0);" class="a1">Next</a>' % pages
        else:
            multipage += '<a tt href="javascript:void(0);">%s</a> <a href="javascript:void(0);" class="a1">Next</a>' % pages
    return multipage