"""CoB URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from user.views import register,login,index,bikes,bookride
from user import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('bikes/',bikes,name='bikes'),
    path('logout/',views.userlogout,name='logout'),
    path('bookride/',views.bookride,name='bookride'),
    path('<int:pk>/',views.fare,name='fare'),
    path('',include('user.urls')),
     # path('hello',views.a),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# path('logout/', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'),   