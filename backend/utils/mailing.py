from mailjet_rest import Client
from config import Config

class Mailer:
	def __init__(self):
		self.api_key = Config.MAIL_API_KEY
		self.api_secret = Config.MAIL_SECRET_KEY
		self.app_email = "lucasnimes30000@gmail.com"
		self.app_name = "Lucas SSH Transfer"
		self.mailjet = Client(auth=(self.api_key, self.api_secret), version='v3.1')

	def send_email(self, target_email, username, message, subject, text_part=None, html_part=None):
		data = {
		'Messages': [
				{
					"From": {
							"Email": self.app_email,
							"Name": self.app_name
					},
					"To": [
							{
									"Email": target_email,
									"Name": username
							}
					],
					"Subject": "Welcome to Our Service!",
					"TextPart": text_part,
					"HTMLPart": html_part,
				}
			]
		};

		try:
			self.mailjet.send.create(data=data);
			print(f"Email sent to {target_email} successfully.")
		except Exception as e:
			print(f"Failed to send email to {target_email}. Error: {str(e)}")
			raise e