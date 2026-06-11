import os
from langchain.tools import StructuredTool
from langchain import OpenAI, SerpAPIWrapper
from langchain.agents import initialize_agent, Tool,AgentType





os.environ['OPENAI_API_KEY'] = apikey
os.environ['SERPAPI_API_KEY']=serpapi


prompt=input('Enter your prompt: ')

def get_dimmension(s):
   print(s)





 


search = SerpAPIWrapper()
tools = [
    Tool(
        name = "Current Search",
        func=search.run,
        description="useful for when you need to answer questions about current events or the current state of the world"
    ),
     Tool(
        name = "line chart_dimmention",
        func=get_dimmension,
        description="""useful for when you need to give a dimen
          """
    ),
 
    
]


llm= OpenAI(temperature=0)


agent= initialize_agent(tools, llm , verbose=True)
if prompt:
   print(agent.run(prompt)) 
    

