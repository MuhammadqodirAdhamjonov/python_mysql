from db_api import DBHelper

db = DBHelper()


def print_all():
    for emp in db.fetch_all():
        print(f"Hodim kodi:     {emp[0]}")
        print(f"F.I.O:          {emp[1]}")
        print(f"Telefon raqami: {emp[2]}")
        print()


def add_new_emp():
    id = int(input("Hodim uchun maxsus raqam kiriting: "))
    full_name = input("Hodimning ism familiyasini kiriting: ")
    phone_number = input("Hodim telefon raqamini kiriting: ")

    db.create(id, full_name, phone_number)
    print("\nHodim ro'yhatga qo'shildi")
    print(f"Hodim kodi:     {id}")
    print(f"F.I.O:          {full_name}")
    print(f"Telefon raqami: {phone_number}")


def update_emp_info():
    id = int(input("Hodimning maxsus raqamini kiriting: "))
    if db.fetch(id) is not None:
        full_name = input("Hodimning ism familiyasini kiriting: ")
        phone_number = input("Hodim telefon raqamini kiriting: ")
        db.update(id, full_name, phone_number)
        print("\nHodim ma'lumotlari yangilandi.")
        print(f"Hodim kodi:     {id}")
        print(f"F.I.O:          {full_name}")
        print(f"Telefon raqami: {phone_number}")
    else:
        print("\nBunday maxsus raqamdagi hodim topilmadi")
        update_emp_info()


def delete_emp():
    id = int(input("Hodimning maxsus raqamini kiriting: "))
    if db.fetch(id) is not None:
        db.delete(id)
        print("Hodim ro'yhatdan o'chirildi")
    else:
        print("\nBunday maxsus raqamdagi hodim topilmadi")
        delete_emp()
