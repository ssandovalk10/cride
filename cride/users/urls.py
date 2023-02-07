# Django
from django.urls import path
# Django REST Framework
from rest_framework.routers import DefaultRouter


from cride.users.views import user as user_views

router = DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='users')


urlpatterns = [

    path('', include(routers.urls))

]
