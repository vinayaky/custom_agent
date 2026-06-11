import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.utilities import WikipediaAPIWrapper

from apikey import apikey
import streamlit as st

os.environ['OPENAI_API_KEY'] = apikey

st.title('GPT')
prompt=st.text_input('write your question here')

#promttemplate
story_template=PromptTemplate(input_variables=['topic','wikipedia_research'],
                              template='write a store on {topic} while leveraging with this wikipedia research: {wikipedia_research}')

llm= OpenAI(temperature=0)

story_chain=LLMChain(llm=llm,prompt=story_template)

wiki =WikipediaAPIWrapper()
if prompt:
  #  response=llm(prompt)
    story=story_template.run(prompt)
    wiki_reseaech=wiki.run(prompt)
    response=story_chain.run(topic=story,wikipedia_research=wiki,verbose=True)
    st.write(response)
