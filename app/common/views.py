from django.shortcuts import render


def index(request):
    # URL: 'http://localhost:8000/'
    # 1. common app내에 templates/common/index.html파일 생성
    # 2. 해당 파일에서 /blog/로의 링크, /polls/로의 링크(a태그)를 두개 생성
    # 3. INSTALLED_APPS에 common을 추가
    # 4. config.urls에서 이 view를 바로 연결 (include를 사용하지 않음)
    return render(request, 'common/index.html')
