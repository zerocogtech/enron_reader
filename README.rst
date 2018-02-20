enron\_reader
=====================

Installation
------------

.. code:: shell

    pip3 install enron_reader

Prerequisites
-------------
For using this package, you must have the Enron email corpus locally. If you don't, either download and extract it using the link provided `here`_, or run

.. _here: https://www.cs.cmu.edu/~enron/

.. code:: shell

    download_enron /path/to/download/enron

in your terminal after installing this package.

Then, you should have a folder named 'maildir' in that directory. It should contain a directory for each user (Enron employee)

Usage example
-------------

.. code:: python
    
    from enron_reader import EnronReader
    reader = EnronReader("/path/to/enron/root")
    
    print(reader.get_user_ids())
    
    mailbox = reader.get_mailbox_for_user("keiser-k")

    main_folders = mailbox.root_folder.subfolders
    some_message = main_folders[0].messages[0]

    print(some_message.subject)
