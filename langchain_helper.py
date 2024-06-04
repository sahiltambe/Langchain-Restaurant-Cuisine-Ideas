import os
from langchain.llms import GooglePalm
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import streamlit as st


# Set the OpenAI API key environment variable
# os.environ['OPENAI_API_KEY'] = openapi_key
# Initialize the OpenAI language model with a specific temperature setting
# llm = OpenAI(temperature=0.7)

# Set GooglePalm API key from Streamlit secrets
# os.environ['GOOGLE_API_KEY'] = st.secrets["GOOGLE_API_KEY"]
# Set GooglePalm API key
os.environ['GOOGLE_API_KEY'] = "AIzaSyCanJlw9nk4xGvIkDyNo7hMORMNhWxutak" #get your own api key from https://makersuite.google.com/

# Initialize GooglePalm LLM
llm = GooglePalm(temperature=0.5)

def generate_restaurant_name_and_items(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}. Return it as a comma separated string"
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    response = chain({'cuisine': cuisine})
    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))
