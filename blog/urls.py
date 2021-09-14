from django.urls import path
from .views import (
		PostListView,
		PostDetailView,
		PostCreateView,
		PostUpdateView,
		PostDeleteView)
from . import views

urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-created'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-Update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-Delete'),
    path('about/',views.about,name='blog-about'),
]