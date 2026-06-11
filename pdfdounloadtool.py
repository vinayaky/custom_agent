import os
from langchain.tools import StructuredTool
from langchain import OpenAI, SerpAPIWrapper
from langchain.agents import initialize_agent, Tool,AgentType
from apikey import apikey
from langchain.memory import ConversationBufferMemory
import requests





os.environ['OPENAI_API_KEY'] = apikey
os.environ['SERPAPI_API_KEY']='2c0b2505e505644a2c43da7a76055c48344c7cf4078f5f09b34fb1e6a60555e8'


prompt=input('Enter your prompt: ')

from bs4 import BeautifulSoup
import urllib.parse


def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory created: {directory_path}")
    else:
        print("Directory already exists.")

def download_pdf(url):
   
    response = requests.get(url)
    print(url)
    if response.status_code==200:
        filename = url.split("/")[-1]

        directory_path =os.path.join(os.path.expanduser("~"), "Downloads")

        # Create the directory if it doesn't exist
        create_directory(directory_path)
        save_path = os.path.join(directory_path, filename)
        with open(save_path, "wb") as file:
            file.write(response.content)
    return "PDF downloaded successfully!"

def search_and_download_pdf(topic):
    # Encode the search topic for the URL

    encoded_topic = urllib.parse.quote_plus(topic)
    name=topic

    # Make a search query on a specific website
    search_url = f"https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q={encoded_topic}&btnG="
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the URLs of PDF files from the search results
    pdf_links = soup.select("a[href$='.pdf']")
    print(response)
    if not pdf_links:
        print("No PDFs found for the given topic.")
        return

    # Download the first PDF file
    pdf_url = pdf_links[0]["href"]
    full_pdf_url = urllib.parse.urljoin(search_url, pdf_url)
    download_pdf(full_pdf_url)
    return 'PDF downloaded successfully'

# Example usage:



def pdftool(url):
   output_dir='.\dounloadpdf'
   response=requests.get(url)
   if response.status_code==200:
      file_path=os.path.join(output_dir,os.path.basename(url))
      with open(file_path,'wb') as pdf:
        ans=pdf.write(response.context)




search = SerpAPIWrapper()
tools = [
   
    Tool.from_function(
        name="Pdf_dounload_tool",
        func=search_and_download_pdf,
        description="""useful for when you need to download a pdf file i need the topic of pdf
        that user wanted to download or dounload document on this topic
        """,
    )
    
]


llm= OpenAI(temperature=0)


agent= initialize_agent(tools, llm ,AgentType=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
if prompt:
   print(agent.run(prompt)) 
