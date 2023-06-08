import pickle
class Contact:

    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone

    def add(self):
         contacts = list(Contact.get_all())
         contacts.append(self)
         f1 = open("./data/contacts.pickle", 'wb')
         f1.seek(0)
         f1.truncate()
         for i in range(len(contacts)):
             pickle.dump(contacts[i], f1)
         else:
             f1.close()


    def edit(self,name, email, phone):
        contacts = list(Contact.get_all())
        for i,contact in enumerate(contacts):
            if contact.name == self.name:
                contacts[i].name = name
                contacts[i].email = email
                contacts[i].phone = phone
        f1 = open("./data/contacts.pickle",'wb')
        f1.seek(0)
        f1.truncate()
        for i in range(len(contacts)):
            pickle.dump(contacts[i], f1)
        else:
            f1.close()

    def delete(self, name):
        contacts = list(Contact.get_all())
        for i, contact in enumerate(contacts):
            if contact.name == self.name:
                contacts.pop(i)
        f1 = open("./data/contacts.pickle", 'wb')
        f1.seek(0)
        f1.truncate()
        for i in range(len(contacts)):
            pickle.dump(contacts[i], f1)
        else:
            f1.close()
    @classmethod
    def find_by_name(self, name):
        contacts = list(Contact.get_all())
        for contact in contacts:
            if name == contact.name:
                return contact
        raise AssertionError

    @classmethod
    def find_by_email(self, email):
        contacts = list(Contact.get_all())
        for contact in contacts:
            if email == contact.email:
                return contact
        raise AssertionError

    @classmethod
    def get_all(self):
        with open("./data/contacts.pickle", "rb") as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break

    def __str__(self):
        return f"Contact #{self.name} - {self.email} - {self.phone}"

class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create(self):
        users = list(User.get_all())
        users.append(self)
        f1 = open("./data/users.pickle", 'wb')
        f1.seek(0)
        f1.truncate()
        for i in range(len(users)):
            pickle.dump(users[i], f1)
        else:
            f1.close()

    @classmethod
    def authenticate(self, username, password):
        accounts = list(User.get_all())
        for acc in accounts:
            if acc.username == username and acc.password == password:
                return True
        return False

    def modify(self,username, password):
        users = list(User.get_all())
        for i, user in enumerate(users):
            if user.username == self.username:
                users[i].username = username
                users[i].password = password
        f1 = open("./data/users.pickle", 'wb')
        f1.seek(0)
        f1.truncate()
        for i in range(len(users)):
            pickle.dump(users[i], f1)
        else:
            f1.close()

    @classmethod
    def get_all(self):
        with open("./data/users.pickle", "rb") as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break

    def __str__(self):
        return f"User: {self.username}"

    @classmethod
    def find_by_name(self, name):
        users = list(User.get_all())
        for user in users:
            if name == user.username:
                return user
        raise AssertionError

