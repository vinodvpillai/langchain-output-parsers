from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

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
    """
    
    # Using the LangChain Prompt 
    chat_prompt = ChatPromptTemplate.from_template(review_template)
    customer_message = chat_prompt.format_messages(text=customer_review)
    
    # Calling the LLM
    response = get_completion(customer_message)
    
    # Expected output is the below format:
    '''
    {
        "gift": False,
        "delivery_days": 5,
        "price_value": "pretty affordable!"
    }
    '''
    
    print(response)
    
    # Note: The below operation won't work we need to convert the result into JSON
    # print(response.get('gift')) # type: ignore