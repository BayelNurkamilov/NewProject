from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ProductSerialzer
from .models import Product
from permissions.permissions import IsOwnerrAdminUser

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerialzer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsOwnerrAdminUser]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()