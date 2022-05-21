
from django.contrib import admin
from django.forms import DateField
from django.urls import path,include
from account import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('api',views.StudentModelViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
]
