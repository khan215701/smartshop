from django.urls import path

from rest_framework.routers import SimpleRouter


from backend.store.views import StoreViewSet

router = SimpleRouter()
router.register('store', StoreViewSet)

urlpatterns = [
    path(
        'store/', StoreViewSet.as_view({'get': 'render_html_template'}), name='store'),
]

urlpatterns += router.urls
