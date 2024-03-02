from rest_framework import serializers

from products.models import Product, Lesson, ProductAccess, Group


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductAccessSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductAccess
        fields = '__all__'