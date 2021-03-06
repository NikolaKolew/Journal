from django.contrib.auth.views import LogoutView
from django.urls import path

from Journal.web_app.views import ProfileList, CreateJornal, JournalDetail, \
    JournalUpdate, JournalDelete, IndexView, HomeView, AboutView, ContactView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('home/', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('journals/', ProfileList.as_view(), name='journals'),
    path('create-journal/', CreateJornal.as_view(), name='create-journal'),
    path('journal/<int:pk>/', JournalDetail.as_view(), name='details'),
    path('journal-update/<int:pk>/', JournalUpdate.as_view(), name='journal-update'),
    path('journal-delete/<int:pk>/', JournalDelete.as_view(), name='journal-delete'),
)