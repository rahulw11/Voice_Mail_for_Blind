import smtplib
import speech_recognition as sr
import pyttsx3
from password import emailPassword, emailName
from email.message import EmailMessage
listener= sr.Recognizer()
engine=pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice=listener.listen(source)
            info=listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(reciever,subject,message):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    #put your email address and password
    emailName = 'your_email@gmail.com'
    emailPassword = 'your_email_password'
    server.login(emailName,emailPassword)
    email=EmailMessage()
    email['From']='Sender_Email'
    email['TO']=receiver
    email['Subject']=subject
    email.set_content(message)
    server.send_message(email)
email_list= {
    'name': 'sender_mail-id@gmail.com'   #add sender's email-id here
}

def get_email_info():
    talk('Who do you want to send this email too')
    name=get_info()
    receiver=email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject=get_info()
    talk('Tell me the message you what to send in your email')
    message=get_info()
    send_email(receiver,subject,message)
    print ("sending email...")
    talk('Dear user your message send successfully!')
    talk('Do you want to send more emails?')
    send_more=get_info()
    if 'yes' in send_more:
        get_email_info()

    talk('have good day')

get_email_info()