import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "store_8_09_25.settings")
django.setup()

from products.models import Product, Order, Supplier, ProductDetail, Address
from django.db.models import F, Sum, Avg, Max, Min, Count, ExpressionWrapper, fields, DecimalField
from django.utils import timezone

total_value = Product.objects.aggregate(total_value=Sum(F('price') * F('quantity')))['total_value']
print(total_value)

average_price_by_category =Product.objects.values('category__name').annotate(average_price=Avg('price')).order_by('category__name')
for entry in average_price_by_category:
    print(f"Категория: {entry['category__name']}, Средняя цена:{entry['average_price']}")

cheapest_product = Product.objects.aggregate(min_price=Min('price'))['min_price']
most_expensive_product = Product.objects.aggregate(
 max_price=Max('price')
)['max_price']
print(f"Самый дешевый продукт: {cheapest_product}")
print(f"Самый дорогой продукт: {most_expensive_product}")

order_summary_by_customer = Order.objects.values(
    'customer__first_name',
    'customer__last_name'
).annotate(
    order_count=Count('id'),
    total_spent=Sum(F('items__price') * F('items__quantity'))
).order_by('customer__last_name')

for entry in order_summary_by_customer:
    print(
        f"Клиент: {entry['customer__first_name']} {entry['customer__last_name']}, "
        f"Заказов: {entry['order_count']}, "
        f"Общая сумма: {entry['total_spent']}"
    )


total_weight_by_category = (
    Product.objects
    .values('category__name')
    .annotate(
        total_weight=Sum(F('details__weight') * F('quantity'))
    )
    .order_by('category__name')
)

for entry in total_weight_by_category:
    print(f"Категория: {entry['category__name']}, Общий вес: {entry['total_weight']}")


suppliers_stats = (
    Supplier.objects
    .annotate(product_count=Count('products'))
    .order_by('name')
)

for supplier in suppliers_stats:
    print(f"Поставщик: {supplier.name}, Количество продуктов: {supplier.product_count}")


average_lifetime_by_category = (
    ProductDetail.objects
    .filter(manufacturing_date__isnull=False, expiration_date__isnull=False)
    .values('product__category__name')
    .annotate(
        average_lifetime=Avg(
            ExpressionWrapper(
                F('expiration_date') - F('manufacturing_date'),
                output_field=fields.DurationField()
            )
        )
    )
    .order_by('product__category__name')
)

for entry in average_lifetime_by_category:
    print(f"Категория: {entry['product__category__name']}, "
          f"Средняя продолжительность: {entry['average_lifetime'].days} дней")

total_spent_by_customer = (
    Order.objects
    .values('customer__first_name', 'customer__last_name')
    .annotate(
        total_spent=Sum(
            ExpressionWrapper(
                F('items__price') * F('items__quantity'),
                output_field=DecimalField(max_digits=12, decimal_places=2)
            )
        )
    )
    .order_by('customer__last_name')
)

for entry in total_spent_by_customer:
    print(
        f"Клиент: {entry['customer__first_name']} {entry['customer__last_name']}, "
        f"Общая сумма заказов: {entry['total_spent']}"
    )

products_descending = Product.objects.order_by('-price')

print("Продукты по убыванию цены:")
for product in products_descending:
    print(f"{product.name}: {product.price}")


orders_by_total = Order.objects.annotate(
    total=Sum(
        ExpressionWrapper(
            F('items__price') * F('items__quantity'),  # если related_name="items"
            output_field=DecimalField(max_digits=12, decimal_places=2)
        )
    )
).order_by('-total')

print("Заказы по общей стоимости:")
for order in orders_by_total:
    print(f"Заказ {order.id}, Общая стоимость: {order.total}")

addresses_sorted = Address.objects.order_by('country', 'city')
print("Адреса по стране и городу:")
for address in addresses_sorted:
    print(f"{address.country}, {address.city}, {address.street}")


first_five_products = Product.objects.all()[:5]

print("Первые 5 продуктов:")
for product in first_five_products:
    print(f"{product.name}: {product.price}")

top_ten_expensive_products = Product.objects.order_by('-price')[:10]

print("10 самых дорогих продуктов:")
for product in top_ten_expensive_products:
    print(f"{product.name}: {product.price}")









