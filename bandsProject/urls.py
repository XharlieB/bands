
from django.conf.urls import url
from django.contrib import admin
from eventos import views
from eventos.views import Register
from eventos import urls as urlsEvent


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Register.as_view(), name='index'),
    url(r'^crear/', views.crear, name='crear'),
    url(r'^descubre/', views.descubre, name='descubre'),
    url(r'^detalle/', views.detalle, name='detalle'),    
   # url('', include('social.apps.django_app.urls', namespace='social')),
	#url(r'^users/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="user-logout"),
    #url(r'^eventos/', include(urlsEvent), namespace='eventos'),
]
