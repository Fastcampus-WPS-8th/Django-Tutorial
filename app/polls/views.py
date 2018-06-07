from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Question


def index(request):
    # DB에 있는 Question중, 가장 최근에 발행(pub_date)된 순서대로 최대 5개에 해당하는
    # QuerySet을 latest_question_list변수에 할당
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }

    # # Django의 TEMPLATES설정에 정의된 방법으로,
    # # 주어진 인자('polls/index.html')에 해당하는 템플릿 파일을 가지는 Template인스턴스를 생성, 리턴
    # template = loader.get_template('polls/index.html')
    #
    # # Template인스턴스의 render()함수를 실행, 인수로 context와 request를 전달
    # # 결과로 렌더링 된 HTML문자열이 리턴됨
    # html = template.render(context, request)
    #
    # # 결과 HTML문자열을 사용해 생성한 HttpResponse객체를 리턴
    # return HttpResponse(html)

    return render(request, 'polls/index.html', context)


def custom_get_object_or_404(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        raise Http404()


def detail(request, question_id):
    # try-except구문 없이
    # polls/detail.html에 해당하는 Question인스턴스를 전달해서
    # HTML에서는 해당 Question의 question_text를 출력
    try:
        question = Question.objects.get(id=question_id, pub_date__isnull=False)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')

    question = get_object_or_404(Question, id=question_id, pub_date__isnull=False)
    question = custom_get_object_or_404(Question, id=question_id)

    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
