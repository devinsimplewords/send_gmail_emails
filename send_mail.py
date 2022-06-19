from src.csv_reader import CSVReader
from src.email_sender import EmailSender

# read from CSV file and get all the info to send emails
csv_reader = CSVReader()
email_info = csv_reader.get_email_info_from_csv()

# send emails
sender = EmailSender()
sender.send_email(email_info)
