from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import HomeViewSet

router = SimpleRouter()
router.register('api/home', HomeViewSet)

urlpatterns = [
    path(
        'home/', HomeViewSet.as_view({'get': 'render_html_template'}), name='home'),
]

urlpatterns += router.urls
