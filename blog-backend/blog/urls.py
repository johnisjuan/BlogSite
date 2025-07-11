from django.urls import path
from .views import BlogPostListCreateView,BlogPostDetailView

urlpatterns = [
    path('posts/',BlogPostListCreateView.as_view(),name = 'post_list'),
    path('posts/<int:pk>',BlogPostDetailView.as_view(),name= 'post-detail'),
]