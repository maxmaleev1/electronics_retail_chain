from django.contrib import admin
from django.utils.html import format_html

from .models import LinkChain, Product


@admin.action(description='Очистить задолженность')
def clear_debt(modeladmin, request, queryset):
    '''Обнуляет задолженность у выбранных звеньев'''
    queryset.update(debt=0)


@admin.register(LinkChain)
class LinkChainAdmin(admin.ModelAdmin):
    '''Админка модели LinkChain'''
    list_display = (
        'name',
        'email',
        'country',
        'city',
        'street',
        'house_number',
        'supplier_link',
        'debt',
        'created_at',
    )
    list_filter = ('city',)
    search_fields = ('name', 'email')
    list_select_related = ('supplier',)
    actions = [clear_debt]

    @admin.display(description='Поставщик')
    def supplier_link(self, obj):
        '''Возвращает HTML-ссылку на поставщика'''
        if obj.supplier:
            url = f'/admin/chain/linkchain/{obj.supplier.id}/change/'
            return format_html('<a href="{}">{}</a>', url, obj.supplier.name)
        return '—'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Админка модели Product'''
    list_display = (
        'name',
        'model',
        'release_date',
        'link_chain',
    )
    list_filter = ('release_date', 'link_chain')
    search_fields = ('name', 'model')
