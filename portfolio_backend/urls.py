from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

def root_redirect(request):
    return HttpResponseRedirect('/api/v1/')

urlpatterns = [
    path('', root_redirect),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
]
