PRODUCTS = {
    "SW-01": {"name": "ساندویچ", "price": 85000},
    "COF-01": {"name": "قهوه", "price": 60000},
    "CK-01": {"name": "کیک", "price": 45000},
}


def calculator_order_total(item):
    total = 0
    items = []
    order = {}
    order["product-key"] = item
    order["number"] = quantity
    print(order)
    items.append(order)
    print(items)
    for item in items:
        code = item["product-key"]
        Quantity = item["number"]
        if code in PRODUCTS:
            price = PRODUCTS[code]["price"]
            total += price*Quantity
    return total


item = input("enter your order : ")
quantity = int(input("enter the number : "))
print(calculator_order_total(item))
    
