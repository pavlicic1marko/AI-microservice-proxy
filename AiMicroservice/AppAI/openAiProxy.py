import json
import openai

with open('config.json') as config_file:
    config = json.load(config_file)
    api_key = config['API_KEY']

openai.api_key = api_key

# model options
gpt_4 = "gpt-4"
gpt_3x5_turbo = "gpt-3.5-turbo"
model_id = gpt_4


def get_answer_from_ai(question:str):
    # Initial message to ask the first question
    messages = [{"role": "user", "content": question}]

    completion = openai.chat.completions.create(model=model_id, messages=messages)

    # Print the answer we received for the 1st question
    return completion.choices[0].message.content

