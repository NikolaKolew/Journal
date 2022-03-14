from django.urls import path

from Journal.web_posts.views import PostList, CreatePost, EditPost, DeletePost, PostDetail, CreateComment, EditComment, DeleteComment, like_view

urlpatterns = (
    path('', PostList.as_view(), name='posts'),
    path('create-posts/', CreatePost.as_view(), name='create-post'),
    path('update-posts/<int:pk>/', EditPost.as_view(), name='update-post'),
    path('delete-posts/<int:pk>/', DeletePost.as_view(), name='delete-post'),
    path('detail-post/<int:pk>/', PostDetail.as_view(), name='detail-post'),
    path('detail-post/<int:pk>/comment/', CreateComment.as_view(), name='create-comment'),
    path('edit-comment/<int:pk>/', EditComment.as_view(), name='edit-comment'),
    path('delete-comment/<int:pk>/', DeleteComment.as_view(), name='delete-comment'),
    path('like/<int:pk>/', like_view, name='like_post'),
)