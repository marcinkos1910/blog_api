from django.urls import path
from rest_framework.routers import SimpleRouter

from posts import views

app_name = 'posts'

router = SimpleRouter()
router.register('posts', views.PostViewSet, basename='posts')
router.register('comments', views.CommentViewSet, basename='comments')
urlpatterns = router.urls

# urlpatterns = [
#     path('', views.PostApiList.as_view(), name='list'),
#     path('<int:pk>/', views.DetailPost.as_view(), name='detail')
# ]
