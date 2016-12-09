from django.conf.urls import url
import views

urlpatterns = [
    url(r'^result', views.get_results, name="result"),
    url(r'^user_query_input', views.get_query_form, name="user_query_input"),
    url(r'^train', views.train_system, name="train"),
]
