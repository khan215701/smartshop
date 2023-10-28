from django.shortcuts import render

from backend.context_processor import ProductModelViewSet
# Create your views here.


class StoreViewSet(ProductModelViewSet):

    def render_html_template(self, request):
        products = self.get_queryset()
        count = products.count()
        context = {'products': products, 'count': count}
        return render(request, 'store/store.html', context)
