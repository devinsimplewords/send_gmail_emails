# send_gmail_emails
This repository contains a Python script to send emails from a Gmail account.  
In [this post](https://devinsimplewords.com/send-email-using-python/) you can find how to set up your Google account, what to install and how the script works.  

In simple words, the script reads from a CSV file stored in data directory and send an email for each row in the file.

In the CSV file must be present the following information:  
- target_email
- email_text
- email_subject

The script collects all this information and then send the emails.

It is mandatory to have enabled the two steps authentication on the Google account.

Steps to run the script:
- prepare a virtualenv and install what it is present in requirements.txt file using the following command:
  ```
  pip install -r requirements.txt
  ```
  If you don't know how to create and activate a virtualenv, please check [this post](https://devinsimplewords.com/python-virtual-environment/)
- Rename the `.env.sample` file in `.env` and set your email and your password for this app.  
  Please note that you should insert the email and the password without quotes (single or double)
- Rename the `email_info.csv.sample` in `email_info.csv` and fill up the information
- Run the script using the following command:
  ```commandline
  python send_mail.py
  ```
