#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
import os
import subprocess
from functools import partial
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

log_path = "/var/backup/logs/"
source_path = '/exports/'
designation_path = 'gs://codehub-dev-backup/data/'
key_path = "/var/backup/key/codehub-backup-bucket-access.json"


SENDGRID_API_KEY='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'

# api_key = os.environ['MJ_APIKEY_PUBLIC']
api_key = '4732590812eaeba1d267dcb9f9656369'

# api_secret = os.environ['MJ_APIKEY_PRIVATE']
api_secret = '5cef5d7e0282c0cff0394ce1ac8392f1'


# mailjet = Client(auth=(api_key, api_secret), version='v3.1')

email_from = 'no_reply@fusemachines.com'
email_subject_sucess = "[DEV] Automatic Backup Report "
email_subject_failure = "[DEV] [FAILURE] Automatic Backup Report "
email_to = 'ruman@fusemachines.com'
emails_list = [
    'rumancha12@gmail.com',

]


def convert_bytes(size):
    # convert the file bytes to readable format
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0
    return size


def getFolderSize(p):
    # get the folder size in bytes
    prepend = partial(os.path.join, p)
    return sum([(os.path.getsize(f) if os.path.isfile(f) else getFolderSize(f)) for f in map(prepend, os.listdir(p))])


def getSucessfullEmailHtmlData(startTime, folderSize, endTime):
    # creates html data to send mail incase of sucess
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
    # creates html data to send mail incase of failure
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


class Client(dict):
    # create a client to send email
    def __init__(self, email, name):
        dict.__init__(self, email=email, name=name)
        self.email = email
        self.name = name

    def getClient(self):
        return {"emai": self.email, "name": self.name}

    def __str__(self):
        return str(self.__dict__)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


def sendEmail(subject, mail):
    # sends email to the given email list with mailjet api
    format_email_cc = []
    for email in emails_list:
        format_email_cc.append(Client(email, email.split("@")[0]))

    data = {
        "from": {
            "email": email_from,
            "name": email_from.split("@")[0]
        },
        "personalizations": [
            {
                "cc": format_email_cc,
                "subject": subject,
                "to": [
                    {
                        "email": email_to,
                        "name": email_to.split("@")[0]
                    }
                ]
            }
        ],
        "content": [
            {
                "type": "text/html",
                "value": mail
            }
        ]


    }
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    result = sg.client.mail.send.post(request_body=data)
    return result


def installGloudPackage():
    os.system("gcloud auth activate-service-account --key-file " + key_path)


date_time = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
year_month_time = datetime.today().strftime("%Y-%m")


def main():
    # filename = log_path + year_month_time + ".txt"
    #
    # if os.path.exists(filename):
    #     append_write = 'a'  # append if already exists
    # else:
    #     append_write = 'w'  # create if already not exists
    #
    # folder_size = convert_bytes(getFolderSize(source_path))
    # f = open(filename, append_write)  # open file to write log
    # f.write('\nstart : ' + date_time + '\nfolder size : ' + folder_size)

    try:
        # installGloudPackage()
        # os.system("gsutil -m rsync -r " + source_path + " " + designation_path)
        end_date_time = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")

        try:
            mail_data = getSucessfullEmailHtmlData(startTime=date_time, folderSize="100MB", endTime=end_date_time)
            sendEmail(email_subject_sucess, mail_data)
        except Exception as e:
            mail_data = getFailureHTMLData(startTime=date_time, folderSize="100MB",
                                           message='Error while sending email')
            sendEmail(email_subject_failure, mail_data)
            # f.write('Error while sending email \n')
            pass

        # f.write('\nFinish\n')
    except Exception as e:
        mail_data = getFailureHTMLData(startTime=date_time, folderSize="100MB", message='Error while taking backup')
        email_result = sendEmail(email_subject_failure, mail_data)
        # f.write('Error while taking backup \n')
        pass

    # f.close()  # close file


if __name__ == '__main__':
    main()

