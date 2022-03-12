from django.contrib.auth.views import LogoutView
from django.urls import path

from Journal.web_app.views import index_view, ProfileList, CreateJornal, JournalDetail, \
    JournalUpdate, JournalDelete




urlpatterns = (
    path('', index_view, name='index'),
    path('journals/', ProfileList.as_view(), name='journals'),
    path('create-journal/', CreateJornal.as_view(), name='create-journal'),
    path('journal/<int:pk>/', JournalDetail.as_view(), name='details'),
    path('journal-update/<int:pk>/', JournalUpdate.as_view(), name='journal-update'),
    path('journal-delete/<int:pk>/', JournalDelete.as_view(), name='journal-delete'),
)