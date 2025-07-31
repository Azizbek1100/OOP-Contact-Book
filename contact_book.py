import json
from contact import Contact

class ContactBook:
    def __init__(self, file_path="contacts.json"):
        self.file_path = file_path
        self.contacts = []
        self.load_from_file()

    def add_contact(self, contact):
        if any(c.name == contact.name for c in self.contacts):
            print("❌ Dublikat ismga yo‘l qo‘yilmaydi.")
            return
        self.contacts.append(contact)
        self.save_to_file()

    def remove_contact(self, name):
        self.contacts = [c for c in self.contacts if c.name != name]
        self.save_to_file()

    def update_contact(self, name, new_contact):
        self.remove_contact(name)
        self.add_contact(new_contact)

    def list_contacts(self):
        return [c.to_dict() for c in self.contacts]

    def search_contact(self, query):
        return [
            c.to_dict()
            for c in self.contacts
            if query.lower() in c.name.lower() or query in c.phone
        ]

    def save_to_file(self):
        with open(self.file_path, "w") as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=4)

    def load_from_file(self):
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                self.contacts = [Contact.from_dict(d) for d in data]
        except FileNotFoundError:
            self.contacts = []