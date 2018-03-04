from django.conf.urls import include, url
from django.contrib import  admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^webpage1/', include('webpage1.url')),
]
