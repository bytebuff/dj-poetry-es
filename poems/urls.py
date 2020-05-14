from poems.api import views
from poems.views import poem_list
from django.urls import path, include

app_name = 'poem'
urlpatterns = [
    path('', poem_list, name='poem'),
    path('api/v1/poems/', views.PoemList.as_view(), name='poemlist'),
]
