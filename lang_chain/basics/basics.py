from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser

chat=ChatOpenAI(temperature=0.0)

customer_messages=prompt_template.format_messages(style="sytle1",text="customer input")

customer_response=chat(customer_messages)
customer_response.content

''' ReAct Framework '''