from django.shortcuts import render

# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models.mongoengine_models import Product
from .models.pymongo_client import products_collection
import requests

def product_list(request):
    products = Product.objects()
    # Convert QuerySet to list of dictionaries, handling ObjectId
    products_list = []
    for p in products:
        product_dict = p.to_mongo().to_dict()
        product_dict['_id'] = str(product_dict['_id'])  # Convert ObjectId to string
        products_list.append(product_dict)
    return render(request, "products.html", {"products": products_list})

@api_view(['GET'])
def get_products(request):
    category = request.GET.get('category')
    query = Product.objects(category=category) if category else Product.objects()
    products = []
    for p in query:
        product_dict = p.to_mongo().to_dict()
        product_dict['_id'] = str(product_dict['_id'])  # Convert ObjectId to string
        products.append(product_dict)

    return Response(products)

@api_view(['POST'])
def add_product(request):
    barcode = request.data.get('barcode')
    # barcode = "1234567890142"
    external_url = f"https://products-test-aci.onrender.com/product/{barcode}"
    resp = requests.get(external_url).json()
    print(f'resp-> {resp}')
    if resp.get('status') == True:
        product_data = resp['product']
    product = Product.objects(barcode=barcode).first()
    if not product:
        product = Product(
            barcode=barcode,
            name=' '.join(product_data.get('description').split()[:3]),
            description=product_data.get('description'),
            material=product_data.get('material'),
        )
        product.save()
    return Response({
        **product.to_mongo().to_dict(),
        "_id": str(product.id)
    })

@api_view(['PATCH'])
def update_category(request, barcode):
    new_cat = request.data.get('category')
    product = Product.objects(barcode=barcode).first()
    if product:
        product.category = new_cat
        product.save()
        return Response({'status': 'updated'})
    return Response({'error': 'Not found'}, status=404)


def board_page(request):
    return render(request, 'board.html')
