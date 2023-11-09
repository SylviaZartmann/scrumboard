
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from projects.views import ClientViewSet, ContactViewSet, ContractViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r'client', ClientViewSet, basename='client')
router.register(r'contact', ContactViewSet, basename='contact')
router.register(r'contract', ContractViewSet, basename='contract')
router.register(r'project', ProjectViewSet, basename='project')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include(router.urls)),
]
