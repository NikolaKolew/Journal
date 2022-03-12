from django.urls import path

from Journal.web_posts.views import PostList, CreatePost, EditPost, DeletePost

urlpatterns = (
    path('', PostList.as_view(), name='posts'),
    path('create-posts/', CreatePost.as_view(), name='create-post'),
    path('update-posts/<int:pk>/', EditPost.as_view(), name='update-post'),
    path('delete-posts/<int:pk>/', DeletePost.as_view(), name='delete-post'),
)