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
from ejemplo.views import( index, saludar_a, sumar, buscar, monstrar_familiares,
                             BuscarFamiliar, AltaFamiliar, ActualizarFamiliar,
                             BorrarFamiliar, mostrar_mascota, AltaMascota, BuscarMascota,
                             BorrarMascota, ActualizarMascota, mostrar_vehiculo, AltaVehiculo,
                             BorrarVehiculo, ActualizarVehiculo, FamiliarList, FamiliarCrear, FamiliarBorrar,
                             FamiliarActualizar )


from ejemplo_dos.views import( index, PostDetalle, PostListar, PostCrear,
                                 PostBorrar, PostActualizar, UserSignUp, UserLogin, UserLogout,
                                  AvatarActualizar )
from django.contrib.admin.views.decorators import staff_member_required

from blog.views import  ( index, PostDetalle, PostListar, PostCrear, PostBorrar, PostActualizar, UserSignUp, 
                                UserLogin, UserLogout )



urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index), # ESTA ES LA NUEVA FUNCTION
    path('saludar-a/<nombre>/', saludar_a),
    path('sumar/<int:a>/<int:b>/', sumar),
    path('buscar/',buscar),
    path('mi-familia/', monstrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('mis-mascotas/', mostrar_mascota),
    path('mis-mascotas/alta', AltaMascota.as_view()),
    path('mis-mascotas/buscar', BuscarMascota.as_view()),
    path('mis-mascotas/borrar/<int:pk>', BorrarMascota.as_view()),
    path('mis-mascotas/actualizar/<int:pk>', ActualizarMascota.as_view()),
    path('mis-vehiculos/', mostrar_vehiculo),
    path('mis-vehiculos/alta', AltaVehiculo.as_view()),
    path('mis-vehiculos/borrar/<int:pk>', BorrarVehiculo.as_view()),
    path('mis-vehiculos/actualizar/<int:pk>', ActualizarVehiculo.as_view()),
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/crear', FamiliarCrear.as_view()),
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),

    path('ejemplo-dos/', index, name="ejemplo-dos-index"),
    path('ejemplo-dos/<int:pk>/detalle/', PostDetalle.as_view(), name="ejemplo-dos-detalle"),
    path('ejemplo-dos/listar/', PostListar.as_view(), name="ejemplo-dos-listar"),
    path('ejemplo-dos/crear/', staff_member_required(PostCrear.as_view()), name="ejemplo-dos-crear"),
    path('ejemplo-dos/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="ejemplo-dos-borrar"),
    path('ejemplo-dos/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="ejemplo-dos-actualizar"),
    path('ejemplo-dos/signup/', UserSignUp.as_view(), name="ejemplo-dos-signup"),
    path('ejemplo-dos/login/', UserLogin.as_view(), name="ejemplo-dos-login"),
    path('ejemplo-dos/logout/', UserLogout.as_view(), name="ejemplo-dos-logout"),
    path('ejemplo-dos/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="ejemplo-dos-avatars-actualizar"),

    path('blog/', index, name="blog-index"),
    path('blog/<int:pk>/detalle/', PostDetalle.as_view(), name="blog-detalle"),
    path('blog/listar/', PostListar.as_view(), name="blog-listar"),
    path('blog/crear/', PostCrear.as_view(), name="blog-crear"),
    path('blog/<int:pk>/borrar/',  staff_member_required(PostBorrar.as_view()), name="blog-borrar"),
    path('blog/<int:pk>/actualizar/',PostActualizar.as_view(), name="blog-actualizar"),
    path('blog/signup/', UserSignUp.as_view(), name="blog-signup"),
    path('blog/login/', UserLogin.as_view(), name="blog-login"),
    path('blog/logout/', UserLogout.as_view(), name="blog-logout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

