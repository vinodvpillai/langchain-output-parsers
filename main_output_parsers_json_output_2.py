from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# OutputParser
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser

import os
from os.path import join, dirname
from dotenv import load_dotenv

# Loading the environment variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# LLM
llm = ChatOpenAI(temperature=0, model=os.environ.get('OPENAI_MODEL'), api_key=os.environ.get('OPENAI_API_KEY'), base_url=os.environ.get('OPENAI_API_HOST'))  # type: ignore

# Completion Method 
"""
Passing the query directly to the LLM
"""
def get_completion(prompt):
    ai_msg = llm.invoke(prompt)
    return ai_msg.content

# Main Method
if __name__ == "__main__":
    
    # Prompt using ChatPromptTemplate - from_template:
    customer_review = """\
    I bought the Bose QuietComfort 45 Noise Cancelling Headphones as a birthday gift for my husband, and he absolutely loves them! \
    The sound quality is phenomenal, and the noise cancellation is top-notch, making it perfect for his daily train commute and work-from-home days. \
    The headphones arrived exactly on the expected delivery in 3 days, which was just in time for his birthday. \
    I was a little worried about shipping delays, but everything went smoothly.
    The headphones feel really comfortable, even after hours of use, and the battery life is impressive. \
    My husband says it’s a game-changer for both focus and relaxation. Couldn’t be happier with this purchase—it was the perfect gift!
    """
    
    # Output: Need to specify each and every JSON attribute informaiton and pass to the LLM
    gift_schema = ResponseSchema(name="gift",
                             description="Was the item purchased as a gift for someone else? Answer True if yes, False if not or unknown.")
    delivery_days_schema = ResponseSchema(name="delivery_days",
                                        description="How many days did it take for the product to arrive? If this information is not found, output -1.")
    price_value_schema = ResponseSchema(name="price_value",
                                        description="Extract any sentences about the value or price, and output them as a comma separated Python list.")
    # Specify the response schema all the attribute we are expecting
    response_schemas = [gift_schema, 
                        delivery_days_schema,
                        price_value_schema]
    
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    format_instructions = output_parser.get_format_instructions()

    review_template = """\
    For the following text, extract the following information:

    gift: Was the item purchased as a gift for someone else? \
    Answer True if yes, False if not or unknown.

    delivery_days: How many days did it take for the product to arrive? If this information is not found, output -1.

    price_value: Extract any sentences about the value or price, and output them as a comma separated Python list.

    Format the output as JSON with the following keys:
    gift
    delivery_days
    price_value

    text: {text}
    
    {format_instructions}
    """
    
    # Using the LangChain Prompt 
    chat_prompt = ChatPromptTemplate.from_template(review_template)
    chat_prompt_message = chat_prompt.format_messages(text=customer_review, format_instructions=format_instructions)
    
    # Calling the LLM
    response = get_completion(chat_prompt_message)
    
    # Expected output is the below format:
    '''
    {
        "gift": False,
        "delivery_days": 5,
        "price_value": "pretty affordable!"
    }
    '''
    
    # Convert the result into the expected output format
    output_dict = output_parser.parse(response) # type: ignore
    print("Expected delivery in days: ",output_dict.get('delivery_days'))