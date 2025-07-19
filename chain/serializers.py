from rest_framework import serializers
from .models import LinkChain


class LinkChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkChain
        fields = '__all__'

    def update(self, instance, validated_data):
        validated_data.pop('debt', None)  # ← Удаляем поле перед обновлением
        return super().update(instance, validated_data)
