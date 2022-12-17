import os

from employees_manager import print_all, add_new_emp, update_emp_info, delete_emp

text = """

Quyidagi komandalardan birini tanlang:

1 - Hodimlar ro'yhatini ko'rish
2 - Yangi hodim qo'shish
3 - Hodim ma'lumotlarini yangilash
4 - Hodimni ro'yhatdan o'chirish
# - Dasturdan chiqish

"""

while True:
    print(text)
    q = input(">>> ").strip()

    match q:
        case "#":
            break
        case "1":
            print_all()
        case "2":
            add_new_emp()
        case "3":
            update_emp_info()
        case "4":
            delete_emp()
        case other:
            print("Noto'g'ri buyruq kiritdingiz!!!")

    input("\nDavom etish uchun enter tugmasini bosing.")
    os.system('cls')
