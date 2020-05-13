from django.urls import path
from . import views
from articles.views import PostDetailView, PostUpdateView, PostDeleteView, UserPostListView

app_name = 'articles'

urlpatterns = [
    path('create/', views.article_create, name='create'),
    path('post-<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('post-<int:pk>/edit', PostUpdateView.as_view(), name='edit'),
    path('post-<int:pk>/delete', PostDeleteView.as_view(), name='delete'),
]