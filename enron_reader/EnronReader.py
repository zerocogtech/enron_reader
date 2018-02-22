from .Mailbox import Mailbox
from typing import Set
import os
import sys
from urllib.request import urlretrieve
import tarfile


class EnronReader:
	"""Enron reader class. 
	"""

	enron_userlist_path = os.path.join(os.path.dirname(__file__), "data", "enron_users.txt")

	def __init__(self, enron_root):
		"""

		:param enron_root: Enron dataset root path (containing an email directory for each user). If enron_root=None, will try to download.
		:type enron_root: str or None
		"""

		with open(EnronReader.enron_userlist_path, "r") as f:
			self.user_ids = f.readlines()
			self.user_ids = [user_id.strip() for user_id in self.user_ids]

		self.user_id_to_mailbox = {}
		self.enron_root = enron_root
			

		# filter unavailable users
		items = os.listdir(self.enron_root)
		self.user_ids = set([user_id for user_id in items if user_id in self.user_ids])


	def get_mailbox_for_user(self, user_id, max_depth = None):
		"""Constructs and returns a `enron_reader.Mailbox` object for the specified user_id.

		:param str user_id: id of an enron user
		:param int max_depth: maximum depth of the folder structure. Default is None, meaning no maximum depth.
		:returns: A Mailbox object for the enron user with id user_id, with maximum depth max_depth
		:rtype: Mailbox
		:raises ValueError: If max_depth is negative
		:raises ValueError: If user_id is not found in the list of users.
		"""
		if user_id not in self.user_ids:
			raise ValueError("Invalid user id")

		if user_id in self.user_id_to_mailbox and self.user_id_to_mailbox[user_id].max_depth == max_depth:
			return self.user_id_to_mailbox[user_id]

		maildir = os.path.join(self.enron_root, user_id)
		mailbox = Mailbox(maildir, max_depth)

		self.user_id_to_mailbox[user_id] = mailbox

		return mailbox


	def get_user_ids(self):
		"""

		:returns: the set of enron user ids
		:rtype: set[str]
		"""
		return self.user_ids







