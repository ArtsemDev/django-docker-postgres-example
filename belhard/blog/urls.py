from django.urls import path

from .views import PostListView, PostDetailView


urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('<slug:post_slug>/', PostDetailView.as_view(), name='post')
]
