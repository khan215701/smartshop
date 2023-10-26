from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from backend.serializers.productSerializers import ProductSerializer
from backend.store.models import Product
# Create your views here.


class HomeViewSet(viewsets.ModelViewSet):
    http_method_names = ('get', 'post')
    permission_classes = (AllowAny,)

    queryset = Product.objects.all().filter(is_available=True)
    serializer_class = ProductSerializer

    def render_html_template(self, request):
        products = self.get_queryset()
        context = {'products': products}
        return render(request, 'home.html', context)
