from django.urls import path
from . import views


urlpatterns = [

    # MIXIN -> BLOCKS OF OTHERS
    #path('',views.vista_mixin_producto),
    #path('<int:pk>/', views.vista_mixin_producto), 

    # MORE FLEXIBLE WAY
    #path('',views.product_alt_view),
    #path('<int:pk>/', views.product_alt_view),
    #USING GENERICS
    path('',views.vista_lista_nuevo_producto, name = 'producto-lista'),
    path('<int:pk>/', views.vista_detalle_producto, name = 'producto-detalle'), 
    path('<int:pk>/update/', views.vista_actualizar_producto, name='producto-editar'), 
    path('<int:pk>/delete/', views.vista_eliminar_producto), 


]