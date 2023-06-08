from managing.manager_actions import *
from menu.models import generate_menu_from_dict
from menu.utils import UserLoginSignal
user_menu = {
    'name':'User Management Menu',
    'children':[
        {
            'name': 'Create A New Account',
            'action': create_new_account,
        },
        {
            'name': 'Authenticate An Existing Account',
            'action': authenticate_existing_account,
        },
        {
            'name': 'Modify An Account',
            'action': modify_account,
        },
    ]
}

contact_menu = {
    'name':'Contact Management System',
    'children':[
        {
            'name': 'Add a new Contact',
            'action': add_a_new_contact_action,
        },
        {
            'name': 'Edit an Existing Contact',
            'action': edit_an_existing_contact_action,
        },
        {
            'name': 'Search By Name In Contacts',
            'action': search_by_name_in_contacts,
        },
        {
            'name': 'Search By Email In Contacts',
            'action': search_by_email_in_contacts,
        },
        {
            'name': 'Delete a Contact',
            'action': delete_a_contact_action,
        },
        {
            'name': 'View All Contacts',
            'action': view_all_contacts_action,
        },
    ]
}

root_user_menu = generate_menu_from_dict(user_menu)
root_contact_menu = generate_menu_from_dict(contact_menu)

def main():
    try:
        root_user_menu()
    except UserLoginSignal:
        print("User Logged in Successfully.")
    root_contact_menu()

main()