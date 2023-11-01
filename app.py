from dotenv import load_dotenv
import os
from langchain import LLMChain, PromptTemplate
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

class App:

    prompt = PromptTemplate(
        input_variables=["message"],
        template="""
            I want you to act as a storyteller. You will come up with entertaining stories that are 
            engaging, imaginative and captivating for the audience. It can be fairy tales, educational 
            stories or any other type of stories which has the potential to capture people's attention 
            and imagination. Depending on the target audience, you may choose specific themes or topics 
            for your storytelling session e.g., if it’s children then you can talk about animals; 
            If it’s adults then history-based tales might engage them better etc. 
            My first request is: 
            ---
            {message}
            ---

        """,
    )
    
    @classmethod
    def run(cls):
        st.title("Kid Story teller")
        query = st.text_input("Enter the type of story you want")
        cancel_button = st.button('Cancel')
        
        if cancel_button:
            st.stop()

        if query:
            llm = OpenAI()
            chain = LLMChain(llm=llm, prompt=cls.prompt)
            with get_openai_callback() as cost:
                response = chain.run(query)
                print(cost)
            
            st.write(response)

if __name__ == '__main__':
    load_dotenv()
    App.run()