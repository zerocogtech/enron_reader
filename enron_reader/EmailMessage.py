import email
from .ContactList import ContactList
from typing import List, Tuple
from email import parser
from email import policy
import time
from email.utils import parsedate


class EmailMessage:
    """Represents an email message.

    :ivar email_from: (email_address, display_name) of the sender of the email
    :vartype email_from: tuple[str, str]
    :ivar email_to: A list of (email_address, display_name) tuples of contacts in the 'to' field
    :vartype email_to: list[tuple[str, str]]
    :ivar email_cc: A list of (email_address, display_name) tuples of contacts in the 'cc' field
    :vartype email_cc: list[tuple[str, str]] 
    :ivar email_bcc: A list of (email_address, display_name) tuples of contacts in the 'bcc' field
    :vartype email_bcc: list[tuple[str, str]] 
    :ivar subject: Subject of the email
    :vartype subject: str
    :ivar email_id: Globally unique internet-message-id
    :vartype email_id: str
    :ivar email_date: Seconds since epoch when the email was sent
    :vartype email_date: int
    :ivar plaintext: Email body as plain text
    :vartype plaintext: str
    """

    email_parser = parser.BytesParser(policy=policy.default)

    def __init__(self):
        pass
    
    def get_all_recipients(self):
        """

        :returns: a list of (display_name, address) tuples of all contacts in 'to', 'from', 'cc', 'bcc' fields
        :rtype: list[tuple[str, str]]
        """
        res = [self.email_from]
        res += self.email_to
        res += self.email_cc
        res += self.email_bcc
        
        return res
    
    def add_recipients_to_contact_list(self, contact_list):
        """adds all the recipients of this EmailMessage to the given ContactList

        :param ContactList contact_list: a ContactList object
        """
        recipients = self.get_all_recipients()
        for r in recipients:
            contact_list.add_contact(r[1], r[0])
        
    
    @staticmethod
    def message_from_eml(eml_path):
        """

        :param str eml_path: path to the eml file
        :returns: an EmailMessage object constructed from the file
        :rtype: EmailMessage
        """
        with open(eml_path, "rb") as f:
            msg_object = EmailMessage.email_parser.parse(f)
        
        res = EmailMessage()
        
        tos, ccs, bccs, froms = [msg_object.get_all(x, []) for x in ['to', 'cc', 'bcc', 'from']]

        res.email_from, res.email_to, res.email_cc, res.email_bcc = [EmailMessage.__parse_address_parts(x) for x in  [froms, tos, ccs, bccs]]
        res.email_from = res.email_from[0]
        
        res.subject = msg_object["Subject"]
        res.email_date = EmailMessage.__email_date_to_timestamp(msg_object["Date"])
        res.email_id = msg_object["Message-ID"]
        res.plaintext = EmailMessage.__find_plaintext(msg_object)
                
        return res


    @staticmethod
    def __email_date_to_timestamp(datefield):
        """
        
        :param str datefield: The 'date' field of the email message
        :returns: Seconds since epoch corresponding to the date
        :rtype: int
        """
        return int(time.mktime(parsedate(datefield)))

    @staticmethod
    def __find_plaintext(msg):
        """Extracts and returns email content in plain text

        :param msg: An :class:`email.message.EmailMessage` object
        :type msg: :class:`email.message.EmailMessage`
        :returns: The content of msg in plain text
        :rtype: str
        """
        if msg.get_content_type() == "text/plain":
            return msg.get_content()
        
        for part in msg.iter_parts():
            cur = find_plaintext(part)
            if cur is not None:
                return cur
            
        return None
        
    
    @staticmethod
    def __parse_address_parts(field_values):
        """

        :param list[str] field_values: list of values of an email address field (like 'to', 'from', ...)
        :returns: a list of (display_name, address) tuples of all contacts in this address field
        :rtype: list[tuple[str, str]]
        """
        recipients = email.utils.getaddresses(field_values)
        recipients = [r for r in recipients if r[1] != ""]
        
        return recipients
