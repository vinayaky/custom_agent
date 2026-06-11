import os
from langchain.tools import StructuredTool
from langchain import OpenAI, SerpAPIWrapper
from langchain.agents import initialize_agent, Tool,AgentType
from apikey import apikey
from langchain.memory import ConversationBufferMemory

import smtplib
from email.message import EmailMessage
import ssl



os.environ['OPENAI_API_KEY'] = apikey
os.environ['SERPAPI_API_KEY']=SERPAPI_API_KEY


prompt=input('Enter your prompt: ')




def send_email(info):
    # Create an instance of EmailMessage
    spldata=info.split()

    messagelist=[]
    recipient_email=''
    subjectlist=[]
    
    for i in spldata:
        subject=''.join(subjectlist)
        if not subject.endswith(','):
            if i.endswith('.com,'):
                recipient_email=i
                continue
            subjectlist.append(str(i))
            continue

        messagelist.append(str(i))
    print(messagelist)      
    message=''

    for word in messagelist:
        message += word + " "
    print(message,subject)
    es='vinayak2072005@gmail.com'
    email_password="odkqyjagrrflodev"
    er=recipient_email
    email_message=EmailMessage()
    email_message["From"]=es
    email_message["To"]=er
    email_message["Subject"]=subject
    email_message.set_content(message)
  

    print(email_message)
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
        smtp.login(es,email_password)
        smtp.send_message(email_message)
    
    return  'Email is send'



search = SerpAPIWrapper()
tools = [
    Tool(
        name = "Current Search",
        func=search.run,
        description="useful for when you need to answer questions about current events or the current state of the world"
    ),
    Tool.from_function(
        name="Email_sending_tool",
        func=lambda message: send_email( message),
        description="""useful for when you need to answer Email I need three parameter first is Emailaddress for which person to 
        send  second is subject of email and third is body of email is in profestional email type 
        and send this three parameter to one tuple type or good email or send this mail  or write a short email or write a mail of this topic 
        """,
    )
    
]


llm= OpenAI(temperature=0)


agent= initialize_agent(tools, llm , verbose=True)
if prompt:
   print(agent.run(prompt)) 
    

