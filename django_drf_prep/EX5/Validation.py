#لیست محصولات
products = [
    {
        "id": 1,
        "name": "Mouse",
        "price": 500_000,
        "stock": 10,
        "category": "accessory"
    },
    {
        "id": 2,
        "name": "Keyboard",
        "price": 1_200_000,
        "stock": 5,
        "category": "accessory"
    },
    {
        "id": 3,
        "name": "Monitor",
        "price": 5_000_000,
        "stock": 0,
        "category": "display"
    },
    {
        "id": 4,
        "name": "Headphone",
        "price": 2_000_000,
        "stock": 8,
        "category": "audio"
    },
    {
        "id": 5,
        "name": "Laptop",
        "price": 25_000_000,
        "stock": 3,
        "category": "computer"
    },
    {
        "id": 6,
        "name": "Webcam",
        "price": 1_500_000,
        "stock": 12,
        "category": "accessory"
    },
    {
        "id": 7,
        "name": "SSD",
        "price": 3_000_000,
        "stock": 6,
        "category": "storage"
    },
]

#پیدا کردن محصول بر اساس ایدی کالا
def get_product_by_id(products,product_id):
    for product in products:
        if product["id"] == product_id:
            print(product["name"])
            break
    else:
        print(None)

#تایید مقدار صحیح وارد شده برای کالا
def get_valid_quantity():
    flag = 1
    while flag == 1:
        try:
            quantity = int(input("Enter the quantity of the selected item  ->  "))
            if quantity <= 0:
                print("Please enter a valid value (greater than zero).")
            else:
                print("Ok")
                flag =0
        except ValueError:
            print("Please enter a valid number!")

product_list = {}
#اعتبارسنجی سفارش
def validate_order(product, quantity):
    if quantity > 0:
        for i in products:
            if i["name"].lower() == product:
                if i["stock"] < quantity:
                    raise ValueError("The entered quantity exceeds the available stock.")
                else:
                    print(f"your selected product:{product} has been added to the cart{quantity}.")
        else:
            raise ValueError("your selected name of product is not valid.")
    else:
        raise ValueError("Please enter a valid value (greater than zero).")

#ثبت سفارش و بازگرداندن فاکتور سفارش و بررسی سفارش های غیر مجاز
def create_order(products, product_id, quantity):
    order = {}
    for i in products:
        if i["id"] == product_id:
            product_n = i["name"].lower()
            price = i["price"]
            if quantity > 0:
                if i["stock"] < quantity:
                    raise ValueError("The entered quantity exceeds the available stock.")
                else:
                    total_price = quantity * price
                    order["product_id"] = product_id
                    order["product_name"] = product_n
                    order["quantity"] = quantity
                    order["unit_price"] = price
                    order["total_price"] = total_price
                return order
            else:
                print("Please enter a valid value (greater than zero).")
            break
    else:
        print("No product found")

for prct in products:
    print(f"{prct["id"]} - {prct["name"]} - {prct["stock"]}")
product_id = int(input("enter ID of product : "))
#product = input("Enter product name -> ").lower()
quantity = int(input("Enter the quantity of the selected item  ->  "))
#get_product_by_id(products,product_id)
#get_valid_quantity()
#try:
#    validate_order(product, quantity)
#except ValueError as a:
#    print(a)
try:
    print(create_order(products, product_id, quantity))
except ValueError as e:
    print(e)