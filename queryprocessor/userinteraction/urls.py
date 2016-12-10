from django.conf.urls import include, url
from chatterbot.ext.django_chatterbot import urls as chatterbot_urls
from django.contrib import admin
from views import ChatterBotAppView
from . import views

urlpatterns = [
    url(r'^result', views.get_results, name="result"),
    url(r'^user_query_input', views.get_query_form, name="user_query_input"),
<<<<<<< HEAD
    url(r'^$', ChatterBotAppView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/chatterbot/', include(chatterbot_urls, namespace='chatterbot')),
=======
    url(r'^train', views.train_system, name="train"),
>>>>>>> refs/remotes/origin/master
]
