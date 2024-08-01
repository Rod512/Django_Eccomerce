from django.contrib import admin
from .models import Payment, Order, OrderProduct

admin.site.register(Payment)
admin.site.register(OrderProduct)

@admin.register(Order)

class OrderAdmin(admin.ModelAdmin):
    class OrderProductInline(admin.TabularInline):
        model = OrderProduct
        extra = 0
        readonly_fields = ('payment', 'user', 'product', 'quantity','product_price','ordered')
    list_display = ('full_name', 'order_number', 'phone', 'email', 'city', 'order_total', 'tax', 'status', 'is_ordered', 'created_at')
    list_filter = ('status', 'is_ordered')
    search_fields = ('order_number', 'first_name', 'last_name', 'email', 'phone', 'city')
    list_per_page = 20
    inlines = [OrderProductInline]

    