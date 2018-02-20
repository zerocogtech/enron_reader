from .ContactList import ContactList
from .EmailFolder import EmailFolder


class Mailbox:
    """Represents a mailbox of a single user.

    :ivar ContactList contact_list: The contact list of the mailbox owner.
    :ivar EmailFolder root_folder: The root folder of the mailbox. Contains all other folders.
    :ivar int max_depth: Maximum depth of the folder structure. Folders deeper than max_depth will be discarded.
    """

    def __init__(self, root_path: str, max_depth: int = 1):
        """

        :param str root_path: The root directory path of the maildir.
        :param int max_depth: Value for max_depth. Default value is 1.
        """

        if max_depth is not None and max_depth < 0:
            raise ValueError("max_depth should be non-negative")

        self.contact_list = ContactList()
        self.max_depth = max_depth
        self.root_folder = EmailFolder("root_folder")
        self.root_folder.read_from_path(root_path, self.contact_list, max_depth)