from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


""" Start office view """

@api_view(['GET'])
def get_office(request):
    office = Ofice.objects.all()
    ser = OficeSerializer(office, many=True)
    return Response(ser.data)

""" End office view """

""" Start get color view """

@api_view(['GET'])
def get_color(request):
    color = Color.objects.all()
    ser = ColorSerializer(color, many=True)
    return Response(ser.data)

""" End color view """

""" Start brend view """
@api_view(['GET'])
def get_brend(request):
    brend = Brend.objects.all()
    ser = BrendSerializer(brend, many=True)
    return Response(ser.data)

""" End brend view """

""" Start category view """

@api_view(['GET'])
def get_category(request):
    catory = Category.objects.all()
    ser = CategorySerializer(catory, many=True)
    return Response(ser.data)

""" End category view """

""" Start sub_category view """

@api_view(['GET'])
def get_sub_category(request):
    category = Sub_Category.objects.all()
    ser = Sub_CategorySerializer(category, many=True)
    return Response(ser.data)

""" End sub_category view """

""" Start Filter """

""" Start sub_category_by_category view """

@api_view(['GET'])
def sub_category_by_category(request, pk):
    category = Category.objects.get(pk=pk)
    sub_categories = Sub_Category.objects.filter(category=category)
    ser = Sub_CategorySerializer(sub_categories, many=True )
    return Response(ser.data)

""" End sub_category_by_category view """

""" Start card by user view """

@api_view(['GET'])
def card_by_user(request):
    user = request.GET.get('user')
    cards = Card.objects.filter(user = user)
    ser = CardSerializer(cards, many=True)
    return Response(ser.data)

""" End card by user view """

""" Start brand by name view """

@api_view(['GET'])
def brand_by_name(request, pk):
    brend = Brend.objects.get(pk=pk)
    name = Brend.objects.filter(name = brend)
    ser = BrendSerializer(name, many=True)
    return Response(ser.data)

""" End brand by name view """

""" Start saved by user view """

@api_view(['GET'])
def saved_by_user(request):
    user = request.GET.get('user')
    saved = Saved.objects.filter(user = user)
    ser = SavedSerializer(saved, many=True)
    return Response(ser.data)

""" End saved by user view """


""" Start order by user view """

@api_view(['GET'])
def order_by_user(request):
    user = request.GET.get('user')
    order = Order.objects.filter(user_id = user)
    ser = OrderSerializer(order, many=True)
    return Response(ser.data)

""" End order by user view """

""" Start product by user view """

@api_view(['GET'])
def product_by_user(request):
    user = request.GET.get('user')
    product = Product.objects.filter(user = user)
    ser = ProductSerializer(product, many=True)
    return Response(ser.data)

""" End product by user view """

""" Start product by sub_subcategory view """

@api_view(['GET'])
def product_by_sub_subcategory(request, pk):
    product = Product.objects.get(pk=pk)
    sub_categories = Sub_Category.objects.filter(prduct = product)
    ser = Sub_CategorySerializer(sub_categories, many=True)
    return Response(ser.data)

""" End product by sub_subcategory view """

""" Start office by adress view """

@api_view(['GET'])
def office_by_adress(request, pk):
    office = Ofice.objects.get(pk=pk)
    off = Ofice.objects.filter(office = office)
    ser = OficeSerializer(off, many=True)
    return Response(ser.data)

""" End office by adress view """

""" Start product by brand view """

@api_view(['GET'])
def product_by_brand(request, pk):
    brend = Brend.objects.get(pk=pk)
    name = Brend.objects.filter(brend = brend)
    ser = BrendSerializer(name)
    return Response(ser.data)

""" End brand by name view """

""" Start product by rating view """

@api_view(['GET'])
def product_by_rating(request):
    product = Product.objects.all().order_by('-reting')[:10]
    ser = BrendSerializer(product, many=True)
    return Response(ser.data)

""" End product by rating view """

""" Start product sale view """

@api_view(['GET'])
def product_sale(request):
    start_price = request.GET.get('s_price')
    end_price = request.GET.get('e_price')
    products = Product.objects.filter(price__gte = start_price, price__lte = end_price)
    ser = ProductSerializer(products, many=True)
    return Response(ser.data)

""" End product sale view """

