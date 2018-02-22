from typing import List
from .Contact import Contact

class ContactList: 
    """Represents the address book of a mailbox. Acts as a container for :py:class:`Contact` objects.
    """

    def __init__(self):
        self.id_counter = 0
        self.contacts = {}


    def add_contact(self, address, display_name):
        """
        adds a contact with address and display_name. If address already exists, updates the display name if it was empty.

        :param str address: address of the new contact
        :param str display_name: display name of the new contact
        """
        if address not in self.contacts:
            new_contact = Contact(self.id_counter, address, display_name)
            self.id_counter += 1
            self.contacts[address] = new_contact
        else:
            old_contact = self.contacts[address]
            if old_contact.display_name == "":
                old_contact.display_name = display_name
    
    def get_contacts(self):
        """

        :returns: the contact objects in this contact list as a list
        :rtype: List[Contact]
        """
        return list(self.contacts.values())

    def get_contact_by_address(self, address):
        """
        
        :param str address: An email address
        :returns: The :class:`Contact` object associated with the given address, or None if address is not in this contact list.
        :rtype: Contact
        """
        if address not in self.contacts:
            return None

        return self.contacts[address]