from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .models import LinkChain
from .serializers import LinkChainSerializer


class IsActiveUser(permissions.BasePermission):
    '''Доступ только для активных пользователей'''

    def has_permission(self, request, view):
        return request.user.is_active  # Проверка is_active


class LinkChainViewSet(viewsets.ModelViewSet):
    queryset = LinkChain.objects.all()  # Все звенья сети
    serializer_class = LinkChainSerializer  # Сериализатор звена
    permission_classes = [IsActiveUser]  # Только активные пользователи
    filter_backends = [DjangoFilterBackend]  # Подключаем фильтрацию
    filterset_fields = ['country']  # Фильтрация по стране
