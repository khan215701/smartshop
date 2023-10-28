from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from backend.serializers.productSerializers import ProductSerializer
from backend.store.models import Product


class ProductModelViewSet(viewsets.ModelViewSet):
    http_method_names = ('get',)
    permission_classes = (AllowAny,)

    queryset = Product.objects.all().filter(is_available=True)
    serializer_class = ProductSerializer
