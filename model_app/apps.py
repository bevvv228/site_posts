from django.apps import AppConfig
import os

def after_startup():
    pass
    # from model_app.models import User,Message

    # if User.objects.count() == 0:
    #     user = User(username = "oleg90",name="Олег",age = 36)
    #     user.save()
    #     msg = Message(msg = "Привет первый пост на сайте",user = user)
    #     msg.save()
    #     msg = Message(msg = "Второй пост, классный день!",user = user)
    #     msg.save()
    #     msg = Message(msg = "Третий пост, все хорошо!",user = user)
    #     msg.save()
    #
    #     user = User(username="nikita80", name="Никита", age=46)
    #     user.save()
    #     msg = Message(msg="первый пост!", user=user)
    #     msg.save()
    #     msg = Message(msg="Второй пост, ура!", user=user)
    #     msg.save()
    #     msg = Message(msg="Третий пост,да!", user=user)
    #     msg.save()
    #
    #
    #     user = User(username="vlad85", name="Владислав", age=41)
    #     user.save()
    #     msg = Message(msg="Первый пост))))", user=user)
    #     msg.save()
    #     msg = Message(msg="Второй пост))))", user=user)
    #     msg.save()
    #     msg = Message(msg="Третий пост))))", user=user)
    #     msg.save()
    #
    # for u in User.objects.all():
    #     print(f"{u.username} {u.name} {u.age}")
    #
    # for m in Message.objects.all():
    #     print(f"{m.msg} {m.dt} {m.user.username}")
    #
    # oleg = User.objects.first()
    # query = Message.objects.filter(user = oleg)
    # for m in query:
    #     print(f"{m.msg} {m.dt}")


class ModelAppConfig(AppConfig):
    name = 'model_app'
    def ready(self):
        if os.environ.get('RUN_MAIN')  or not os.environ.get('DJANGO_SETTINGS_MODULE'):
            after_startup()




