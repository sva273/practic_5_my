import os
import django
import random
from decimal import Decimal
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "store_8_09_25.settings")
django.setup()

from products.models import Category, Supplier, Product, ProductDetail, Address, Customer, Order, OrderItem

fake = Faker()

def run():
    print("Seeding data...")

    categories = []
    for _ in range(5):
        category, _ = Category.objects.get_or_create(
            name=fake.word().capitalize()
        )
        categories.append(category)


    suppliers = []
    for _ in range(5):
        supplier, _ = Supplier.objects.get_or_create(
            name=fake.company(),
            contact_email=fake.unique.company_email(),
            phone_number=fake.unique.phone_number()
        )
        suppliers.append(supplier)


    products = []
    for _ in range(20):
        product = Product.objects.create(
            name=fake.word().capitalize() + " " + fake.word(),
            category=random.choice(categories),
            supplier=random.choice(suppliers),
            price=Decimal(random.uniform(5, 500)).quantize(Decimal("0.01")),
            quantity=random.randint(1, 100),
            article=fake.unique.uuid4(),
            is_available=random.choice([True, False])
        )
        products.append(product)


        ProductDetail.objects.create(
            product=product,
            description=fake.text(max_nb_chars=200),
            manufacturing_date=fake.date_between(start_date="-2y", end_date="today"),
            expiration_date=fake.date_between(start_date="today", end_date="+2y"),
            weight=Decimal(random.uniform(0.1, 10)).quantize(Decimal("0.01"))
        )


    addresses = []
    for _ in range(10):
        address = Address.objects.create(
            country=fake.country(),
            city=fake.city(),
            street=fake.street_name(),
            house_number=str(random.randint(1, 200))
        )
        addresses.append(address)


    customers = []
    for _ in range(15):
        customer = Customer.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.unique.email(),
            phone_number=fake.phone_number(),
            address=random.choice(addresses),
            is_deleted=random.choice([False, False, False, True]),
            deleted_at=fake.date_time_this_year() if random.choice([True, False]) else None
        )
        customers.append(customer)


    for _ in range(30):
        order = Order.objects.create(
            customer=random.choice(customers)
        )

        for _ in range(random.randint(1, 5)):
            product = random.choice(products)
            qty = random.randint(1, 5)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=qty,
                price=product.price
            )

    print("✅ Seeding completed!")


if __name__ == "__main__":
    run()
