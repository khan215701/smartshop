from rest_framework import serializers

from backend.store.models import Product


class ProductSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ('id', 'product_name', 'slug', 'category', 'description',
                  'price', 'images', 'is_available')
