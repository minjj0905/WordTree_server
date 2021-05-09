from django.urls import path
from wordquiz import views
from django.conf.urls import include, url

app_name = 'wordquiz'


urlpatterns =[
    url(r'^index', views.index, name = 'index'),
    url(r'^three/(?P<tag>\d+)', views.quiz_three),
]
