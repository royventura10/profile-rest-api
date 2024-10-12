from django.urls import path,include
from profiles_api import views


# Para los view set necesito utilizar un enrutador.
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')


# Le agrego include para que envie las rutas a la lista de URL
urlpatterns=[
    path('hello-view/',views.HelloApiView.as_view()),
    path('',include(router.urls))
]
