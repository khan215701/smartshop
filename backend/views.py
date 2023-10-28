from django.shortcuts import render

from backend.context_processor import ProductModelViewSet

# Create your views here.


class HomeViewSet(ProductModelViewSet):

    def render_html_template(self, request):
        products = self.get_queryset()
        context = {'products': products}
        return render(request, 'home.html', context)
