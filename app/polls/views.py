from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Question, Choice


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
    print('request.GET:', request.GET)
    print('request.POST:', request.POST)
    print('requestDIR:', dir(request.POST.get))

    # 선택한 Choice의 choice_text와 id값을 갖는 문자열 생성
    # 해당 문자열을 HttpResponse로 전달
    # ex)
    # question_text: 걸스데이 멤버중....
    # choice_text: 민아
    # choice.id: 4
    # 현재 Choice의 votes: 5

    choice_id = request.POST['choice']
    question = Question.objects.get(id=question_id)
    choice = Choice.objects.get(id=choice_id)

    # choice의 votes값을 증가시키고 DB에 저장하기
    choice.votes += 1
    choice.save()

    question_text = question.question_text
    choice_text = choice.choice_text
    choice_votes = choice.votes

    result = (
        'question_text: {}\n'
        'choice_text: {}\n'
        'choice.id: {}\n'
        'choice.votes: {}').format(
        question_text,
        choice_text,
        choice_id,
        choice_votes,
    )
    return HttpResponse(result)
