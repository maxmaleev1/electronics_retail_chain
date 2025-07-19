from django.contrib import admin
from django.utils.html import format_html

from .models import LinkChain, Product


@admin.action(description='Очистить задолженность')
def clear_debt(modeladmin, request, queryset):
  queryset.update(debt=0)


@admin.register(LinkChain)
class LinkChainAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'country',
        'city',
        'supplier_link',
        'debt',
        'created_at',
    )
    list_filter = ('city',)  # Фильтр по названию города
    search_fields = ('name', 'email')  # Поиск по названию и email
    list_select_related = ('supplier',)
    # Оптимизация: заранее загружает поставщика (ForeignKey)
    actions = [clear_debt]
    # Добавляет в админку действие "Очистить задолженность"


    @admin.display(description='Поставщик')  # Заголовок колонки
    def supplier_link(self, obj):
        if obj.supplier:
            url = f'/admin/chain/linkchain/{obj.supplier.id}/change/'
            return format_html('<a href="{}">{}</a>', url, obj.supplier.name)
        return '—'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'model',
        'release_date',
        'link_chain',
    )
    list_filter = ('release_date', 'link_chain')
    search_fields = ('name', 'model')


