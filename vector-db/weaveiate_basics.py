import requests
import json
import weaviate
import os
from dotenv import load_dotenv ,find_dotenv
from weaviate import EmbeddedOptions
WEAVE_CLIENT =None
def get_data():
    #resp = requests.get('https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json')
    # data = json.loads(resp.text)
    data=json.load(open("data/jeopardy_1k.json"))
    # print(json.dumps(data,indent=2))
    print(len(data))
    return data

def get_weaviate_client():
    global WEAVE_CLIENT
    if WEAVE_CLIENT is None:
        WEAVE_CLIENT=_get_weaviate_instance()
    return WEAVE_CLIENT
def _get_weaviate_instance():
    load_dotenv(find_dotenv())
    w_client=weaviate.Client(
        embedded_options=EmbeddedOptions(),
        additional_headers={
            "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
        }
    )
    return w_client

def load_text_data_into_weaviate():
    data=get_data()
    w_client=get_weaviate_client()
    with w_client.batch() as batch:
        
        for rec in data:
            print(rec)
            obj_body={
                'question':rec['Question'],
                'answer':rec['Answer'],
                'round':rec['Round']
            }
            print(obj_body)
            batch.add_data_object(
                data_object=obj_body,
                class_name="Question"
            )
            break
    print("Completed loading the data")

def create_question_class():
    w_client=get_weaviate_client()
    if w_client.schema.exists("Question"):
        w_client.schema.delete_class("Question")
    class_definition ={
        "class": "Question",
        "vectorizer":"text2vec-openai",
        "vectorIndexConfig": {
            "distance" : "cosine"
        },
        "properties":[
            {
                'name' :"question",
                "dataType" : ['text']
            },
            {
                "name": "answer",
                "dataType" : ['text']
            },
            {
                "name":"round",
                "dataType" : ['text']
            }
        ]
    }
    

    w_client.schema.create_class(class_definition)

if __name__=="__main__":
    create_question_class()
    load_text_data_into_weaviate()
    print("Test")