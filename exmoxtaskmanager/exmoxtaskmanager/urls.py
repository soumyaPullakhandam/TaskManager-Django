from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('task.apis.urls')),  # for apis
    path('', include('task.forms.urls')),  # for forms forms
    path('auth/', include('rest_auth.urls')),  # for login
    path('accounts/', include('django.contrib.auth.urls'))
]
urlpatterns += staticfiles_urlpatterns()
