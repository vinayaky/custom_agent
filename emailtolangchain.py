import os
from langchain.tools import StructuredTool
from langchain import OpenAI, SerpAPIWrapper
from langchain.agents import initialize_agent, Tool,AgentType
from apikey import apikey
from langchain.memory import ConversationBufferMemory

import smtplib
from email.message import EmailMessage
import ssl

def send(email='email' , body='body' , sub='subject' , file='file'):
   es='vinayak2072005@gmail.com'
   email_password="odkqyjagrrflodev"
   er=email
   email_message=EmailMessage()
   email_message["From"]=es
   email_message["To"]=er
   email_message["Subject"]=sub
   email_message.set_content(body)
   if not file=='file':
        for files in file:
            with open(file, 'rb') as fp:
                file_data = fp.read()
                email_message.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=files)
        
       

   print(email,body,sub,file)
   print(email_message)
   context=ssl.create_default_context()
   with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
       smtp.login(es,email_password)
       smtp.send_message(email_message)
   
   return  'Email is send',email

def send_email(info=[]):
    # Create an instance of EmailMessage
    subject=info[0]
    recipient_email=info[1]
    message=info[2]
    print(subject,message,recipient_email)
    sender_email='vinayak2072005@gmail.com'
    sender_password="odkqyjagrrflodev"
    email = EmailMessage()
    email['Subject'] = subject
    email['From'] = sender_email
    email['To'] = recipient_email
    email.set_content(message)

    try:
        # Connect to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            # Start TLS encryption
            smtp.starttls()
            # Login to the sender's email acco
  # Login to the sender's email account
            smtp.login(sender_email, sender_password)
            # Send the email
            smtp.send_message(email)
        return "Email sent successfully"
    except Exception as e:
        return f"Failed to send email: {str(e)}"




    # Tool(name='search',
     #            description='search(query: str) -> str - Searches the API for the query.',
      #            args_schema=<class 'pydantic.main.SearchApi'>, return_direct=True,
       #          verbose=False, callback_manager=<langchain.callbacks.shared.SharedCallbackManager object at 0x12748c4c0>, func=<function search_api at 0x16bd66310>, coroutine=None)
#
 #                   name="Email_sending_tool",
  #                  func=send_email,
   #                 description="""recipient_email: str, subject: str, message: str, sender_email: str, sender_password: str) -> str-
    #                send a email for recipient_email
     #               """
   