from menu.utils import *
from .models import User, Contact

def add_a_new_contact_action():
    print("Enter event's detail below:")
    name = get_input("Name: ", target_type=str) # regex with target type
    email = get_input("Email: ", target_type=str)
    phone = get_input("Phone: ", target_type=str)
    contact = Contact(name, email, phone)
    contact.add() #need to defined in add function
    print("Contact's created.\n")

def edit_an_existing_contact_action():
    name = get_input("Enter the Contact Name: ", target_type=str)
    try:
        contact = Contact.find_by_name(name)
    except:
        print("Contact not found.")
        return
    name = get_input("Enter the Name: ", target_type=str)  # regex with target type
    email = get_input("Email: ", target_type=email_validation)
    phone = get_input("Phone: ", target_type=phone_validation)
    contact.edit(name, email, phone)
    print("Contact's edited.\n")

def delete_a_contact_action():
    name = get_input("Enter the Contact Name: ", target_type=str)
    try:
        contact = Contact.find_by_name(name)
    except:
        print("Contact not found.")
        return
    contact.delete(name)
    print("Contact's deleted.\n")

def view_all_contacts_action():
    all_contacts = list(Contact.get_all())  # list or generator
    for i, event in enumerate(all_contacts):
        print(i + 1, event)  # __str__

def create_new_account():
    username = get_input("Enter the Username: ", target_type=username_validation)
    password = get_input("Enter the Password: ", target_type=password_validation)
    user = User(username, password)
    user.create()
    print("User's created.\n")

def authenticate_existing_account():
    username = get_input("Username: ")
    password = get_input("Password: ")
    if User.authenticate(username, password):
        raise UserLoginSignal
        return

    print("Account with this info was not found.")
    return

def modify_account():
    name = get_input("Enter the username: ", target_type=str)
    try:
        user = User.find_by_name(name)
    except:
        print("Contact not found.")
        return
    username = get_input("Enter the New Username: ", target_type=username_validation)
    password = get_input("Enter the New Password: ", target_type=password_validation)
    user.modify(username, password)
    print("User was Modified.")

def search_by_name_in_contacts():
    name = get_input("Enter the Name: ", target_type=str)
    try:
        contact = Contact.find_by_name(name)
    except:
        print("Contact not found.")
        return
    print(contact)

def search_by_email_in_contacts():
    email = get_input("Enter the Email: ", target_type=str)
    try:
        contact = Contact.find_by_email(email)
    except:
        print("Contact not found.")
        return
    print(contact)