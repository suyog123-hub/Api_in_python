from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CrudView
router=DefaultRouter()
router.register("view",CrudView)

urlpatterns = [
    path("",include(router.urls))
]
