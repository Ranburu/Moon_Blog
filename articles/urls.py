from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.article_list),
    re_path('<slug>/', views.article_detail)
]