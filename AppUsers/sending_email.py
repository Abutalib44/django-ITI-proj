'''
pyhon script sending email to users
'''
import logging
import smtplib
from secrets import *
logging.getLogger().setLevel(logging.INFO)



"""def init_connection(host,username,password):
    '''

    :param host:
    :param username:
    :param password:
    :return:
    '''
    try:
        server = smtplib.SMTP(host)
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.ehlo()
        return server
    except:
        raise Exception('cant login')"""


def send_email(fromaddr, toaddrs, msg):
    '''
    send email to user
    input:connection
    input:user
    input:email address
    output:none
    '''

    try:
      #connection = init_connection(SERVICE, USERNAME, PASSWORD)
       
      server = smtplib.SMTP(SERVICE)
      server.ehlo()
      server.starttls()
      server.login(USERNAME,PASSWORD)
      server.ehlo()
      server.sendmail(fromaddr, toaddrs, msg) 
      server.quit()
    except:
        logging.critical("cant start connection")

def ahmed():
    return "hi from sending email"

if __name__=="__main__":
    send_email("ehabewies5@gmail.com","hassanrafat95@gmail.com","hii")

