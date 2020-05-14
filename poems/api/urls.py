from django.urls import path
from poems.api.views import PoemList

urlpatterns = [
    path('api/v1/talks/', PoemList.as_view()),
]