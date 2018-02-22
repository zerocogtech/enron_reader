from .EmailMessage import EmailMessage
from .ContactList import ContactList
import os


class EmailFolder:
    """Represents an email folder in a mailbox.

    :ivar name: Name of the email folder
    :vartype name: str
    :ivar subfolders: The list of subfolders in the email folder
    :vartype subfolders: list[EmailFolder] 
    :ivar messages: The list of messages in the email folder.
    :vartype messages: list[EmailMessage]
    """

    def __init__(self, name):
        """

        :param type name: Name of the email folder
        """
        self.name = name
        self.subfolders = []
        self.messages = []
    
    def __add_subfolder(self, subfolder):
        self.subfolders.append(subfolder)
    
    def __add_message(self, message):
        self.messages.append(message)
        
    def read_from_path(self, path, contact_list, max_depth, cur_depth = 0):
        """Reads the mailbox folder's contents (messages and subfolders), and add emails' contacts to contact_list

        :param str path: Path of the folder
        :param ContactList contact_list: A ContactList container for the folder's messages' contacts.
        :param int max_depth: Maximum depth of read subfolders.
        :param int cur_depth: Depth of the folder (distance from the root folder). Default is 0.
        """

        contents = os.listdir(path)
        for item in contents:
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                if max_depth != None and cur_depth >= max_depth:
                    continue
                subfolder = EmailFolder(item)
                subfolder.read_from_path(item_path, contact_list, max_depth, cur_depth + 1)
                self.__add_subfolder(subfolder)
            else:
                try:
                    message = EmailMessage.message_from_eml(item_path)
                    self.__add_message(message)
                    message.add_recipients_to_contact_list(contact_list)
                except:
                    pass