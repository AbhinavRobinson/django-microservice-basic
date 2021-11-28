from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Product, User
from .serializers import ProductSerializer, UserSerializer

import random


class ProductViewSet(viewsets.ViewSet):

    # /api/products GET
    @staticmethod
    def list(_: Request) -> Response:
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # /api/products POST
    @staticmethod
    def create(request: Request) -> Response:
        print(request.data)
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # /api/products/ OPTIONS
    @staticmethod
    def count(_: Request) -> Response:
        return Response(Product.objects.count())

    # /api/products/<str:id> GET
    @staticmethod
    def retrieve(_: Request, pk: str = None) -> Response:
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    # /api/products/<str:id> PUT
    @staticmethod
    def update(request: Request, pk: str = None) -> Response:
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    # /api/products/<str:id> DELETE
    @staticmethod
    def destroy(_: Request, pk: str = None) -> Response:
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # /api/products/likes/<str:id> GET
    @staticmethod
    def more_than_likes(_: Request, pk: str = None) -> Response:
        try:
            products = Product.objects.filter(likes__gt=int(pk)-1)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ViewSet):
    @staticmethod
    def get(_: Request) -> Response:
        users = User.objects.all()
        if not users:
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
        user = random.choice(users)
        return Response({
            'id': user.id,
            'username': user.name,
            'email': user.email
        })

    @staticmethod
    def create(request: Request) -> Response:
        if request.data.get('name') in [None, ''] or request.data.get('email') in [None, '']:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
