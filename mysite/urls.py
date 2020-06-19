from django.contrib import admin
from django.urls import path, include

from mysite.core import views

admin.site.site_header = 'GPMS Administration'
admin.site.site_title = 'GPMS Admin'
admin.site.index_title = 'GPMS Administration'


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
 	path('help/', views.help, name='help'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('secret3/', views.SecretPage.as_view(), name='secret3'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('loggedin',views.login_successful,name='loggedinsuccessfully'),
    path('outpasses/',views.outpasses,name="outpasses")
]