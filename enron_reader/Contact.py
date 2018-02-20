class Contact:
    """Represents a contact object.

    :ivar int id: id of the contact
    :ivar str address: the email address of the contact
    :ivar str display_name: the display name of the contact
    """
    def __init__(self, id, address, display_name):
        if display_name == None:
            display_name = ""
        self.address = address
        self.display_name = display_name
        self.id = id

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.address == other.address

        return False

    def __hash__(self):
        return hash(self.address)