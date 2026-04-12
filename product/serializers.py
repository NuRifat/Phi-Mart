from rest_framework import serializers
from decimal import Decimal
from product.models import Category


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    unit_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, source='price')

    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')
    """This will show the category number"""
    # category = serializers.PrimaryKeyRelatedField(
    #     queryset=Category.objects.all()
    # )

    """This will show the category name"""
    # category = serializers.StringRelatedField()

    """This will show the CustomCategory"""
    # category = CategorySerializer()

    """This will show the category in link"""
    category = serializers.HyperlinkedRelatedField(
        queryset=Category.objects.all(),
        view_name='specific-category',
    )

    def calculate_tax(self, product):
        return round(product.price * Decimal(1.1), 2)