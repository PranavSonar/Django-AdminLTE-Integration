from django.conf.urls import include,url
from . import views

urlpatterns = [
   # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
]
