from django.apps import AppConfig


# ------ Django app설정파일인 SendListConfig 클래스를 정의
class SendListConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # 애플리케이션에서 사용할 기본 자동 필드 타입을 지정
    name = 'send_list'
    # name : 앱의 이름을 지정
