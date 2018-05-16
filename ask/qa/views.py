from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage

from django.contrib.auth import login, logout
from qa.models import Question


# Create your views here.
from django.http import HttpResponse 
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    paginator = Paginator(qs, limit)

    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page, paginator



def new_q(request):
    qs=Question.object.all()
    qs=qs.order_by('-added_at')
    limit=request.GET.get('limit', 10)
    page=request.GET.get('page', 1)
    paginator=Paginator(qs, limit)
    page=paginator.page(page)
    paginator.baseurl = reverse('question_list') + '?page='

    return render(request, 'q.html', {
           'questions': page.object_list,
           'page': page,
           'paginator':paginator,
    })


def popular(request):
    qs=Question.object.all()
    qs=qs.order_by('-raiting')
    limit=request.GET.get('limit', 10)
    page=request.GET.get('page', 1)
    paginator=Paginator(posts, limit)
    page=paginator.page(page)
    paginator.baseurl = reverse('question_list') + '?page='

    return render(request, 'raiting.html', {
           'questions': page.object_list,
           'page': page,
           'paginator':paginator,
    })

def single(request, pk):
    question = get_object_or_404(Question, id=pk)
    answers = question.answer_set.all()
    form = AnswerForm(initial={'question': str(pk)})
    return render(request, 'detail.html', {
        'question': question,
        'answers': answers,
        'form': form,
    })



