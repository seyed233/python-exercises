"""محاسبه‌ی مبلغ سفارش بر اساس کد محصول و تعداد درخواستی."""

# فهرست محصولات و قیمت هرکدام به تومان
PRODUCTS = {
    "SW-01": {"name": "ساندویچ", "price": 85000},
    "COF-01": {"name": "قهوه", "price": 60000},
    "CK-01": {"name": "کیک", "price": 45000},
}


def calculate_order_total(product_code, quantity):
    """مبلغ کل سفارش را محاسبه می‌کند."""
    if product_code not in PRODUCTS:
        raise ValueError("کد محصول در فهرست محصولات وجود ندارد.")

    if quantity <= 0:
        raise ValueError("تعداد محصول باید بیشتر از صفر باشد.")

    unit_price = PRODUCTS[product_code]["price"]
    return unit_price * quantity


def main():
    """اطلاعات سفارش را از کاربر می‌گیرد و مبلغ کل را نمایش می‌دهد."""
    product_code = input("کد محصول را وارد کنید: ").strip().upper()

    try:
        quantity = int(input("تعداد محصول را وارد کنید: "))
        total_price = calculate_order_total(product_code, quantity)
    except ValueError as error:
        print(f"خطا: {error}")
        return

    product_name = PRODUCTS[product_code]["name"]
    print(f"مبلغ سفارش {quantity} عدد {product_name}: {total_price:,} تومان")


if __name__ == "__main__":
    main()
