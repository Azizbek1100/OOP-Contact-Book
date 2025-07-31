from contact import Contact
from contact_book import ContactBook

book = ContactBook()

while True:
    print("\n📞 Contact Book\n1. Qo‘shish\n2. Ro‘yxat\n3. Qidirish\n4. Yangilash\n5. O‘chirish\n6. Chiqish")
    choice = input("Tanlovingiz: ")

    if choice == "1":
        name = input("Ism: ")
        phone = input("Telefon: ")
        email = input("Email: ")
        address = input("Manzil: ")
        contact = Contact(name, phone, email, address)
        book.add_contact(contact)

    elif choice == "2":
        for c in book.list_contacts():
            print(c)

    elif choice == "3":
        query = input("Ism yoki telefon bo‘yicha qidiruv: ")
        for result in book.search_contact(query):
            print(result)

    elif choice == "4":
        name = input("Yangilanadigan ism: ")
        new_name = input("Yangi ism: ")
        new_phone = input("Yangi telefon: ")
        new_email = input("Yangi email: ")
        new_address = input("Yangi manzil: ")
        updated = Contact(new_name, new_phone, new_email, new_address)
        book.update_contact(name, updated)

    elif choice == "5":
        name = input("O‘chiriladigan ism: ")
        book.remove_contact(name)

    elif choice == "6":
        break
    else:
        print("❗ Noto‘g‘ri tanlov.")