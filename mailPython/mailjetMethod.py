# This call sends a message to one recipient.

from mailjet_rest import Client
import os
import json
from datetime import datetime

# api_key = os.environ['MJ_APIKEY_PUBLIC']
# api_key = '4732590812eaeba1d267dcb9f9656369'

# # api_secret = os.environ['MJ_APIKEY_PRIVATE']
# api_secret = '5cef5d7e0282c0cff0394ce1ac8392f1'
api_key = 'f38f6dc936c32b23a592f93e73a442a4'
api_secret = '8b739406f6fc2e06637d96dfa133e51e'

mailjet = Client(auth=(api_key, api_secret), version='v3.1')
email_from = 'noreply@fuse.ai'
email_subject_sucess = "[DEV] Automatic Backup Report "
email_subject_failure = "[DEV] [FAILURE] Automatic Backup Report "
# email_to = 'ruman@fusemachines.com'
# emails_list = [
#     # 'amrit@fusemachines.com',
#     'ruman@fusemachines.com',
#     # 'simran.manandhar@fusemachines.com',
#     # 'shirshak@fusemachines.com',
#     # 'sagar@fusemachines.com',
#     # 'karishma.shakya@fusemachines.com'
# ]
email_to = 'noreply@fuse.ai'
emails_list = [
    # 'amrit@fusemachines.com',
    'noreply@fuse.ai',
    # 'simran.manandhar@fusemachines.com',
    # 'shirshak@fusemachines.com',
    # 'sagar@fusemachines.com',
    # 'karishma.shakya@fusemachines.com'
]


def getSucessfullEmailHtmlData(startTime, folderSize, endTime):
    return '''
<!DOCTYPE html>\n  
				<html lang=\"en\">\n  
				<head>\n  
				 <meta charset=\"UTF-8\">\n  
				  <title>Fuse AI Welcome</title>\n  
				  <link href=\"https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,900\" rel=\"stylesheet\">
				  <style>\n  
				 * {\n  
				 margin: 0;\n  
				 padding: 0;\n  
				 -webkit-box-sizing: border-box;\n  
				 box-sizing: border-box;\n  
				 font-family: arial;\n  
				 }\n  
				 </style>\n  
				</head>\n  
				<body>\n  
				  <div style=\"background: #e3e5e7; padding: 30px 0; height: 100%;\">\n  
				 <center>\n  
				 <table style=\"width: 500px;-webkit-text-size-adjust: 100%;-ms-text-size-adjust: 100%;mso-table-lspace: 0pt;mso-table-rspace: 0pt;margin: 0;padding: 0;font-family: 'Roboto', sans-serif;border-collapse: collapse !important;height: 100% !important;\" align=\"center\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" height=\"100%\" width=\"100%\" id=\"bodyTable\">\n  
				   <thead>\n  
				     <tr>\n  
				        <th style=\"font-size: 32px;font-weight: 100; padding: 30px 10px 20px; background: #1897CB; color: #fff;\"><img src=\"https://classroom.fuse.ai/images/email-logo/logo_white.png\"  width=\"102\" /></th>\n  
				     </tr>\n  
				   </thead>\n  
				   <tbody>\n  
				     <tr style=\"background: #fff;\">\n  
				       <td>\n  
				         <h2 style=\"color: #1897CB; font-size: 26px; font-weight: 600; margin: 50px 50px 30px;\">

                             Backup Information

                        </h2>\n  

                         <div style=\"margin: 0 50px 30px; line-height: 26px; color: #4A4A4A; font-size: 16px\">\n  
                          <p> This is an automatically generated mail to notify about the <b> successful </b> completion of the Codehub files to the cloud which includes user assignments & projects along with database.
				         </div>

				       </td>\n  
				     </tr>\n  

                      <tr style=\"background: #fff;\">\n  
				       <td>\n  
                         <div style=\"margin: 0 50px 30px; line-height: 26px; color: #4A4A4A; font-size: 16px\">\n  
                          Start time : %startTime% (24hrs)
				         </div>
				       </td>\n  
                     </tr>
                     </tr> 
                      <tr style=\"background: #fff;\">\n  
				       <td>\n  
                         <div style=\"margin: 0 50px 30px; line-height: 26px; color: #4A4A4A; font-size: 16px\">\n  
                           End Time :  %endTime% (24hrs)
				         </div>
				       </td>\n  
                     </tr> 
                     <tr style=\"background: #fff;\">\n  
				       <td>\n  
                         <div style=\"margin: 0 50px 30px; line-height: 26px; color: #4A4A4A; font-size: 16px\">\n  
                           Total Folder Size : %folderSize% 
				         </div> 
				       </td>\n  
                     </tr> 



				<tr style=\"background: #fff;\">\n  
				       <td>\n  
				           <div style=\"margin: 0 50px 30px; line-height: 26px; color: #4A4A4A; font-size: 16px\">\n  
				               With Regards,<br/>\n  
				               <a style=\"color: #4A4A4A;\">Codehub Team</a> \n  
				           </div>\n  
				       </td>\n  
				     </tr>\n  

				 <tr>\n  
				       <td>\n  
				           <div>\n  
				               <p style=\"margin: 20px 50px 15px; line-height: 18px; color: #4A4A4A; font-size: 11px\">You’re receiving this email because your email have been added to backup report. </p>\n  
				               \n  
				               <p style=\"text-align:center; margin: 20px 50px 15px; line-height: 18px; color: #4A4A4A; font-size: 11px;\">\n  
				                   Powered by <a href=\"https://www.fusemachines.com/\" style=\"display: inline-block; margin-left: 5px; vertical-align: middle;\"><img src=\"https://classroom.fuse.ai/images/email-logo/fusemachines_logo.png\" width=\"98\" /></a>\n  
				               </p>\n  
				           </div>\n  
				       </td>\n  
				     </tr>\n  
				   </tbody>\n  
				 </table>\n  
				 </center>\n  
				  </div>\n  
				  <img class=\"abc\" src="  imageUri "/"applicationId  " width=\"0\" height=\"1\">

				</body>\n  
				</html>


'''.replace('%startTime%', startTime).replace('%folderSize%', folderSize).replace('%endTime%', endTime)


def getFailureHTMLData(startTime, folderSize, message):
    return '''
<!DOCTYPE html>\n  
				<html lang=\"en\">\n  
				<head>\n  
				 <meta charset=\"UTF-8\">\n  
				  <title>Fuse AI Welcome</title>\n  
				  <link href=\"https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,900\" rel=\"stylesheet\">
				  <style>\n  
				 * {\n  
				 margin: 0;\n  
				 padding: 0;\n  
				 -webkit-box-sizing: border-box;\n  
				 box-sizing: border-box;\n  
				 font-family: arial;\n  
				 }\n  
				 </style>\n  
				</head>\n  
				<body>\n  
				  <div style=\"background: #e3e5e7; padding: 30px 0; height: 100%;\">\n  
				 <center>\n  
				 <table style=\"width: 500px;-webkit-text-size-adjust: 100%;-ms-text-size-adjust: 100%;mso-table-lspace: 0pt;mso-table-rspace: 0pt;margin: 0;padding: 0;font-family: 'Roboto', sans-serif;border-collapse: collapse !important;height: 100% !important;\" align=\"center\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" height=\"100%\" width=\"100%\" id=\"bodyTable\">\n  
				   <thead>\n  
				     <tr>\n  
				        <th style=\"font-size: 32px;font-weight: 100; padding: 30px 10px 20px; background: #1897CB; color: #fff;\"><img src=\"https://classroom.fuse.ai/images/email-logo/logo_white.png\"  width=\"102\" /></th>\n  
				     </tr>\n  
				   </thead>\n  
				   <tbody>\n  
				     <tr style=\"background: #fff;\">\n  
				       <td>\n  
				         <h2 style=\"color: #1897CB; font-size: 26px; font-weight: 600; margin: 50px 50px 30px;\">

                             Backup Error Information

                        </h2>\n  

                         <div style=\"margin: 0 50px 30px; line-height: 26px; color: #4A4A4A; font-size: 16px\">\n  
                          <p> 

                          This is an automatically generated mail to notify about the <b> failure </b> of the Codehub files to the cloud.

				         </div>

				       </td>\n  
				     </tr>\n  

                      <tr style=\"background: #fff;\">\n  
				       <td>\n  
                         <div style=\"margin: 0 50px 30px; line-height: 26px; color: #4A4A4A; font-size: 16px\">\n  
                          Start time : %startTime% (24hrs)
				         </div>
				       </td>\n  
                     </tr>

                     <tr style=\"background: #fff;\">\n  
				       <td>\n  
                         <div style=\"margin: 0 50px 30px; line-height: 26px; color: #4A4A4A; font-size: 16px\">\n  
                           Total Folder Size : %folderSize% 
				         </div> 
				       </td>\n  
                     </tr> 

                   </tr> 
                      <tr style=\"background: #fff;\">\n  
				       <td>\n  
                         <div style=\"margin: 0 50px 30px; line-height: 26px; color: #4A4A4A; font-size: 16px\">\n  
                           Message : %message%
				         </div>
				       </td>\n  
                     </tr>


				<tr style=\"background: #fff;\">\n  
				       <td>\n  
				           <div style=\"margin: 0 50px 30px; line-height: 26px; color: #4A4A4A; font-size: 16px\">\n  
				               With Regards,<br/>\n  
				               <a style=\"color: #4A4A4A;\">Codehub Team</a> \n  
				           </div>\n  
				       </td>\n  
				     </tr>\n  

				 <tr>\n  
				       <td>\n  
				           <div>\n  
				               <p style=\"margin: 20px 50px 15px; line-height: 18px; color: #4A4A4A; font-size: 11px\">You’re receiving this email because your email have been added to backup report. </p>\n  
				               \n  
				               <p style=\"text-align:center; margin: 20px 50px 15px; line-height: 18px; color: #4A4A4A; font-size: 11px;\">\n  
				                   Powered by <a href=\"https://www.fusemachines.com/\" style=\"display: inline-block; margin-left: 5px; vertical-align: middle;\"><img src=\"https://classroom.fuse.ai/images/email-logo/fusemachines_logo.png\" width=\"98\" /></a>\n  
				               </p>\n  
				           </div>\n  
				       </td>\n  
				     </tr>\n  
				   </tbody>\n  
				 </table>\n  
				 </center>\n  
				  </div>\n  
				  <img class=\"abc\" src="  imageUri "/"applicationId  " width=\"0\" height=\"1\">

				</body>\n  
				</html>


'''.replace('%startTime%', startTime).replace('%folderSize%', folderSize).replace('%message%', message)


def sendEmail(subject, mail):
    format_email_cc = []
    for email in emails_list:
        format_email_cc.append(Client(email, email.split("@")[0]))

    data = {
        "Globals": {
            "From": {
                "Email": email_from,
                "Name": email_from.split("@")[0]
            },
            "Cc": format_email_cc,
            "Subject": subject,
            "HTMLPart": mail
        },
        "Messages": [
            {
                "To": [
                    {
                        "Email": email_to,
                        "Name": email_to.split("@")[0]
                    }
                ]
            }
        ]
    }
    result = mailjet.send.create(data=data)
    return result


class Client(dict):
    def __init__(self, Email, Name):
        dict.__init__(self, Email=Email, Name=Name)
        self.Email = Email
        self.Name = Name

    def getClient(self):
        return {"Email": self.Email, "Name": self.Name}

    def __str__(self):
        return str(self.__dict__)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


format_email_cc = []
for email in emails_list:
    format_email_cc.append(Client(email, email.split("@")[0]))

# data = {
#   "Globals": {
#       "From": {
#           "Email": email_from,
#           "Name": email_from.split("@")[0]
#       },
# 	  "Cc": format_email_cc,
#       "Subject": email_subject,
#       "HTMLPart": getSucessfullEmailHtmlData(startTime= '2010-01-02', folderSize = '105.6 MB', endTime = '2020-01-03')
#   },
#   "Messages": [
# 	  {
# 		  "To": [
#               {
#                 	"Email": email_to,
#           			"Name": email_to.split("@")[0]
#               }
#           ]
# 	  }
#   ]
# }
# result = mailjet.send.create(data=data)
# print(result.status_code)
# print(result.json())

try:
    date_time = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
    mail_data = getSucessfullEmailHtmlData(startTime=date_time, folderSize='105.6 MB', endTime=date_time)
    raise Exception('testing')
    email_result = sendEmail(email_subject_sucess, mail_data)
except Exception as e:
    mail_data = getFailureHTMLData(startTime=date_time, folderSize='105.6 MB', message='Error while sending email')
    email_result = sendEmail(email_subject_failure, mail_data)
