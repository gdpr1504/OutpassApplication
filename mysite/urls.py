from django.contrib import admin
from django.urls import path, include

from mysite.core import views

admin.site.site_header = 'GPMS Administration'
admin.site.site_title = 'GPMS Admin'
admin.site.index_title = 'GPMS Administration'


urlpatterns = [
    path('', views.home, name='home'),
    path('home1',views.home1,name='home1'),
    path('signup/', views.signup, name='signup'),
 	path('help/', views.help, name='help'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('secret3/', views.SecretPage.as_view(), name='secret3'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('loggedin',views.login_successful,name='login_successful'),
    path('outpasses/',views.outpasses,name="outpasses"),
    path('outpasses/home2',views.home2,name='home2'),
    path('homepage',views.homepage,name='homepage'),
    path('outpasses/outpasses123/',views.set,name='outpasses/outpasses123'),
    path('outpasses/outpasses123/loggedin',views.login_successful,name="outpasses/outpasses123/loggedin"),
    path('outpasses/loggedin',views.login_successful,name="outpasses/loggedin"),
    path('outpasses/outpasses123/home2',views.home2,name="outpasses/outpasses123/home2"),
    path('outpasses/outpasses',views.outpasses,name="outpasses/outpasses"),
    path('outpasses/outpasses123/outpasses',views.outpasses,name="outpasses/outpasses123/outpasses"),
    path('outpasses/outpasses123/outpasses123',views.set,name="outpasses/outpasses123/outpasses123")
]