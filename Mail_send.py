import smtplib




class Mail():

    def __init__(self):

        self.gmail_user = "bot.trackerreport@gmail.com"
        self.gmail_password = "dasvierte"


        self.mail = {

        "from"   :"bot.trackerreport@gmail.com",
        "to"     :"sommer.silvan3@gmail.com",
        "subject":"Report",
        "body"   : None

        }


    def send_mail(self):


        try:
            self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            self.server.ehlo()
            self.server.login(self.gmail_user, self.gmail_password)

            self.message = 'Subject: {}\n\n{}'.format(self.mail["subject"], self.mail["body"])
            self.server.sendmail(from_addr=self.mail["from"],to_addrs=self.mail["to"],msg=self.message)

        except:
            print('Something went wrong...')




