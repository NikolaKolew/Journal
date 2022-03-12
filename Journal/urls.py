from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Journal.web_app.urls')),
    path('account/', include('Journal.auth_accounts.urls')),
    path('post/', include('Journal.web_posts.urls')),
]
