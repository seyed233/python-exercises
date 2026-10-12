#جمع کل
def total_price(price,quanty):
    sum_total = (price*quanty)
    return sum_total
#اعمال تخفیف و مبلغ با احتساب تخفیف
def apply_discount(total,percent):
    resault = total*((100-percent)/100)
    if percent >100 or percent<0:
        return None
    else:
        return resault
#جداسازی برای خوانایی بهتر
def format_price(amount):
    return f"{amount:,} تومان"

#دریافت مشخصات از کاربر
price = int(input("enter a price = "))
quanty = int(input("enter quanty = "))
percent = int(input("enter the percent = "))
total = total_price(price,quanty)
print(f"مبلغ کل : {total}")
#print(apply_discount(total,percent))
amount = apply_discount(total,percent)
print(f"مبلغ با احتساب تخفیف : {format_price(amount)}")