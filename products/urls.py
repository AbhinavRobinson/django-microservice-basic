from django.urls import path

from .views import ProductViewSet, UserViewSet

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create',
        'options': 'count'
    })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('products/likes/<str:pk>', ProductViewSet.as_view({
        'get': 'more_than_likes'
    })),
    path('user', UserViewSet.as_view({
        'get': 'get',
        'post': 'create'
    }))
]
