

import pprint
import google.generativeai as palm
from random import randint as r
from json import dumps as json_dumps
palm.configure(api_key="AIzaSyDH2zCYkM1UWxJeJ9KniUdHY337CdHOJ1k")

# Initialize the Palm client
# client = palm.PalmClient()

# Set the model
# model = "text-davinci-002"

# Set the prompt
# prompt = "Once upon a time..."

# Set the safety settings to BLOCK_NONE for all categories
safety_settings = [
    {
        "category": palm.HarmCategory.HARM_CATEGORY_DEROGATORY,
        "threshold": palm.HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": palm.HarmCategory.HARM_CATEGORY_TOXIC,
        "threshold": palm.HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": palm.HarmCategory.HARM_CATEGORY_SEXUAL,
        "threshold": palm.HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": palm.HarmCategory.HARM_CATEGORY_VIOLENT,
        "threshold": palm.HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": palm.HarmCategory.HARM_CATEGORY_MEDICAL,
        "threshold": palm.HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": palm.HarmCategory.HARM_CATEGORY_DANGEROUS,
        "threshold": palm.HarmBlockThreshold.BLOCK_NONE,
    },
]

# Generate text
# completion = client.chat(
#     model=model,
#     prompt=prompt,
#     safety_settings=safety_settings
# )
response = palm.chat(messages="hi, I want to tell you how I'm feeling. ",context="Be an empathetic person (which means absolutely no giving advice unless asked for) and listen to their problem. Encourage them to ",candidate_count=5, temperature=1,safety_settings=safety_settings)
response.last=response.candidates[r(0,4)]
print(response.last)
for i in range(30):

    usr_input=input("\nEnter your response:\n")
    
    if usr_input=="exit()":
        break
    if not usr_input.strip():
        usr_input = "Tell me more."
        
    try:
        response = response.reply(usr_input)
    except Exception as e:
        print(f"Error:{e}")
    else:
        print(f"\nReply:\n{response.last}")
    

    
    
print("Sorry, due to limits, our conversation has to be cut short for now, this is an alpha version")

history=json_dumps(response.messages,indent=4)
print(history)

input("Press any key to exit...")
# pprint.pprint(completion)