from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key

import os
# Set the OpenAI API key environment variable
os.environ['OPENAI_API_KEY'] = openapi_key

# Initialize the OpenAI language model with a specific temperature setting
llm = OpenAI(temperature=0.7)

def generate_restaurant_name_and_items(cuisine):
    # Chain 1: Restaurant Name
    # Define a prompt template for generating a restaurant name based on the cuisine
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )

    # Create a language model chain for generating the restaurant name
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2: Menu Items
    # Define a prompt template for generating menu items based on the restaurant name
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}. Return it as a comma separated string"
    )

    # Create a language model chain for generating the menu items
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    # Combine the name chain and food items chain into a sequential chain
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', "menu_items"]
    )

    # Run the sequential chain with the given cuisine and return the response
    response = chain({'cuisine': cuisine})

    return response

if __name__ == "__main__":
    # Test the function by generating a restaurant name and menu items for Italian cuisine
    print(generate_restaurant_name_and_items("Italian"))