from django.shortcuts import render
from .models import Products
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products
from .serializers import ProductsSerializer

@api_view(['GET'])
def product_list(request):
    products = Products.objects.all()
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)



def product_items(request,slug):
    # فقط به درخواست‌های GET پاسخ می‌دهد
    if request.method == 'GET':
        # دریافت شیء محصول با استفاده از product_id
        product = get_object_or_404(Products, slug=slug)
        image_url = product.image_url.url

        # تبدیل داده‌های محصول به دیکشنری
        product_data = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'img': image_url,
        }

        # بازگرداندن پاسخ JSON
        return JsonResponse(product_data, status=200)

    # اگر متد درخواست GET نباشد
    return JsonResponse({'error': 'Invalid request method. Only GET is allowed.'}, status=405)