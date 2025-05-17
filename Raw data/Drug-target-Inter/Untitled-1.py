input_file = 'D://TEZ//DATA//data2//Drug-target-Inter/GPCR.txt'  # نام فایل متنی ورودی که داده‌ها در آن با تب از هم جدا شده‌اند
output_file = 'D://TEZ//DATA//data2//Drug-target-Inter/GPCR1.txt'  # نام فایل متنی خروجی که داده‌ها در آن با خط تیره از هم جدا شده‌اند

# باز کردن فایل ورودی و خواندن محتوا
with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# باز کردن فایل خروجی و نوشتن داده‌های تغییر یافته
with open(output_file, 'w', encoding='utf-8') as file:
    for line in lines:
        # جایگزینی تب با خط تیره
        modified_line = line.replace('\t', '-')
        file.write(modified_line)

print(f"Data has been converted and saved to {output_file}")