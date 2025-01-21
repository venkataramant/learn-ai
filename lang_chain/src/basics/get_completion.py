import os
import openai
from dotenv import load_dotenv, find_dotenv
print(load_dotenv(find_dotenv()))
print(os.environ['OPENAI_API_KEY'])
openai.api_key = os.environ['OPENAI_API_KEY']
def get_completion(prompt,model="gpt-3.5-turbo"):
	messages = [{"role":"user","content":prompt}]
	response = openai.ChatCompletion.create(
			model=model,
			messages=messages,
			temperature=0)
	print(response)
	return response.choices[0].message["content"]

if __name__=="__main__":
	print(get_completion("what is today?"))