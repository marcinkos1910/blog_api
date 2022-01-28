from django.urls import path
from rest_framework.routers import SimpleRouter

from user import views


app_name = 'user'

router = SimpleRouter()
router.register('', views.UserViewSet, basename='users')
urlpatterns = router.urls

# urlpatterns = [
#     path('', views.UserApiList.as_view(), name='list'),
#     path('<int:pk>/', views.DetailUser.as_view(), name='detail'),
# ]
