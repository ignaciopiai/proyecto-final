"""proyect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path




from django.contrib.admin.views.decorators import staff_member_required

from blog.views import  ( index, PostDetalle, PostListar, PostCrear, PostBorrar, PostActualizar, UserSignUp, 
                                UserLogin, UserLogout, AvatarActualizar, UserActualizar,  MensajeCrear,
                                 MensajeListar, MensajeDetalle, about, MensajeBorrar  )



urlpatterns = [
    path('admin/', admin.site.urls),


    path('blog/', index, name="blog-index"),
    path('blog/<int:pk>/detalle/', PostDetalle.as_view(), name="blog-detalle"),
    path('blog/listar/', PostListar.as_view(), name="blog-listar"),
    path('blog/crear/', PostCrear.as_view(), name="blog-crear"),
    path('blog/<int:pk>/borrar/',  staff_member_required(PostBorrar.as_view()), name="blog-borrar"),
    path('blog/<int:pk>/actualizar/',PostActualizar.as_view(), name="blog-actualizar"),
    path('blog/signup/', UserSignUp.as_view(), name="blog-signup"),
    path('blog/login/', UserLogin.as_view(), name="blog-login"),
    path('blog/logout/', UserLogout.as_view(), name="blog-logout"),
    path('blog/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="blog-avatars-actualizar"),
    path('blog/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="blog-users-actualizar"),
    path('blog/mensajes/crear/', MensajeCrear.as_view(), name="blog-mensajes-crear"),
    path('blog/mensajes/listar/', MensajeListar.as_view(), name="blog-mensajes-listar"),
    path('blog/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="blog-mensajes-detalle"),
    path('blog/about', about, name="blog-about"),
    path('blog/mensajes/<int:pk>/borrar/',  staff_member_required(MensajeBorrar.as_view()), name="blog-mensajes-borrar"),
   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

