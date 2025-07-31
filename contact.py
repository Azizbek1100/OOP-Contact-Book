from datetime import datetime

class Contact:
    def __init__(self, name, phone, email=None, address=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.created_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        contact = Contact(
            data["name"],
            data["phone"],
            data.get("email"),
            data.get("address")
        )
        contact.created_at = data.get("created_at", datetime.now().isoformat())
        return contact