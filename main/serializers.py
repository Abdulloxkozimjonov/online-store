from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class Sub_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Category
        fields = '__all__'


class BrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brend
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class SavedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saved
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = Order
        fields = '__all__'


class OficeSerializer(serializers.ModelSerializer):
        class Meta:
            model = Ofice
            fields = '__all__'


class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adress
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'











