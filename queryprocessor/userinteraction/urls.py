from django.conf.urls import include, url
from chatterbot.ext.django_chatterbot import urls as chatterbot_urls
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^result', views.get_results, name="result"),
    url(r'^user_query_input', views.get_query_form, name="user_query_input"),
    url(r'^$', views.get_chatterbot_view, name="chatterbot_view"),
    url(r'^chatterbot_train/', views.get_chatterbot_trainer, name="chatterbot_trainer"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/chatterbot/', include(chatterbot_urls, namespace='chatterbot')),
    url(r'^train', views.train_system, name="train"),
]
