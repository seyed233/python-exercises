#لیست محصولات با مشخصات
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
    }
]

#نشان دادن تمام محصولات به همراه قیمت
def get_all_products():
    for i in range(len(products)):
        print(f"{products[i]["id"]}_ {products[i]["name"]}; price = {products[i]["price"]}")

#پیدا کردن محصول بر اساس کد محصول
def get_product_by_id(products,product_id):
    for i in range(len(products)):
        Product = products[i]["name"]
        Product_id = products[i]["id"]
        if product_id == Product_id:
            print(f"your desired Product: {Product}")
            break
    else:
        print(f"NO product with this ID was found")

#نشان دادن فقط محصولاتی که موجود هستند
def get_available_products(products):
    available_product = []
    for i in range(len(products)):
        number_product = products[i]["stock"]
        name_product = products[i]["name"]
        if number_product != 0:
            available_product.append(name_product)
    for j in available_product:
        print(j)

#مجموع کل ارزش محصولات
def total_value(products):
    total_value = 0
    for i in range(len(products)):
        number_product = products[i]["stock"]
        price_product = products[i]["price"]
        inventory_value = number_product*price_product
        total_value += inventory_value
    print(f"{total_value:,}")

#پیدا کردن محصولات با قیمت پایین تر از مبلغ ورودی
def Filter(products):
    fliltered_list = []
    price = int(input("enter your price : "))
    for i in range(len(products)):
        price_product = products[i]["price"]
        if price >= price_product:
            name_product = products[i]["name"]
            fliltered_list.append(name_product)
    if not fliltered_list:
        print("No product cheaper than your target price was found.")
    else:
        for item in fliltered_list:
            print(item)

#مشخص کردن تعداد محصولات هر دسته بندی
def category(products):
    Cat = {}
    for i in range(len(products)):
        cat = products[i]["category"]
        number_product = products[i]["stock"]
#        Cat[cat] = Cat.get(cat,0) + number_product
        if cat in Cat:
            Cat[cat] = Cat[cat] + number_product
        else:
            Cat[cat] = number_product
    print(Cat)

# اعمال تخفیف روی محصولاتی که کاربر انتخاب کرده است وبررسی اینکه ایا خرید معتبر هست یا خیر
def reduction(products):
    Order = []
    flag = 1
    while flag == 1:
        orders = {"name_product":0 , "number_product":0 }
        order = input("please enter name of product : ")
        if order == "END":
            flag = 0
        else:
            num = int(input(f"enter number of {order} : "))
            orders["name_product"] = order
            orders["number_product"] = num
            Order.append(orders)
    return Order

def on_hand(products):
    Order = reduction(products)
    total_price = 0
    is_valid = True
    for i in range(len(products)):
        name = products[i]["name"]
        stock = products[i]["stock"]
        price = products[i]["price"]
        for j in range(len(Order)):
            ord = Order[j]["name_product"]
            num_ord = Order[j]["number_product"]
            if name == ord:
                if num_ord > stock:
                    print("The order quantity exceeds the available stock.")
                    is_valid = False
                    break
                else:
                    Price = price * num_ord
                    total_price += Price
    if is_valid:
        percent = int(input("Enter your discount percentage"))    
        final_price = total_price * ((100-percent)/100)
        return f"{Order} and <{final_price}>"
    else:
        return f"Purchase unsuccessful."



print("از بین محصولات زیر محصول خود را انتخاب کنید تا به سبد خرید اضافه شود و در انتها کلمه'END'را وارد کنید")
get_all_products()
#product_id = int(input("enter the id number of Product : "))
#get_product_by_id(products,product_id)
#get_available_products(products)
#total_value(products)
#Filter(products)
#category(products)
#print(reduction(products))
print(on_hand(products))