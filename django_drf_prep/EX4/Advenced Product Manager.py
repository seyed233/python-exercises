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
keyword = []

#جستجوی بین محصولات بر اساس ورودی
def search_products(products, keyword):
    result = []
    for i in range(len(products)):
        product_name = products[i]["name"]
        keyword.append(product_name.lower())
    for j in keyword:
        if name.lower() in j:
            result.append(j)
    else:
        print("not found")
    return result

#جستجوی کالا بر اساس فیلتر قیمت
def filter_by_price(products):
    result = []
    min_price = float(input("minimum price :  "))
    max_price = float(input("maximum price :  "))
    for i in range(len(products)):
        price_product = products[i]["price"]
        name_product = products[i]["name"]
        if min_price <= price_product <= max_price:
            result.append(name_product)
    return result

#جستجو بر  اساس مقدار موجودی
def filter_by_stock(products, min_stock):
    for product in products:
        if product["stock"] >= min_stock:
            print(product["name"])

#دسته بندی بر اساس خواسته کاربر مانند قیمت به صورت نزولی یا صعودی
def sort_products(products, descending):
    sorted_list = input("sort by 'price', 'name', 'stock' :  ")
    if descending == False:
        name = sorted(products, key = lambda product: product["name"])
        price = sorted(products, key = lambda product: product["price"])
        stock = sorted(products, key = lambda product: product["stock"])
    if descending == True:
        name = sorted(products, key = lambda product: product["name"], reverse= True)
        price = sorted(products, key = lambda product: product["price"], reverse= True)
        stock = sorted(products, key = lambda product: product["stock"], reverse= True)
    if "name" == sorted_list:
        for i in name:
            print(i)
    elif "price" == sorted_list:
        for i in price:
            print(i)
    elif "stock" == sorted_list:
        for i in stock:
            print(i)
    else:
        ValueError = "Uncategorized"
        print(ValueError)

#جستجو و فیلتر پیشرفته
def find_products(products, keyword=None, category=None, min_price=None, max_price=None, min_stock=None):
    result = []
    for product in products:
        matches = True
        if keyword is not None:
            if keyword.lower() not in product["name"].lower():
                matches = False
        if category is not None:
            if category.lower() != product["category"].lower():
                matches = False
        if min_price is not None:
            if product["price"] < min_price:
                matches = False
        if max_price is not None:
            if product["price"] > max_price:
                matches = False
        if min_stock is not None:
            if product["stock"] < min_stock:
                matches = False
        if matches:
            result.append(product)
    return result


#min_stock = int(input("enter a number : "))
name = input("search... :     ")
#print(search_products(products,keyword))
#print(filter_by_price(products))
#filter_by_stock(products, min_stock)
#sort_products(products, descending= True)
#found_product = find_products(products, keyword= "o", category= "accessory")
#for product in found_product:
#    print(product["name"])