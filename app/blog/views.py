from django.http import HttpResponse


def index(request):
    # localhost:8000/blog/
    # 1. config.urls에서 blog.urls를 include, path는 'blog/'를 사용
    # 2. blog app내에 urls모듈을 생성하고 이 view를 위 URL과 연결되도록 설정
    # 3. localhost:8000/blog/에서 Blog index텍스트가 출력되는지 확인
    return HttpResponse('Blog index')
