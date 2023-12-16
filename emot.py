# import pprint
import google.generativeai as palm
from random import randint as r
from googletrans import Translator
import json
from json import dumps as json_dumps
import os
import permissions
# Configuration
palm.configure(api_key="AIzaSyDH2zCYkM1UWxJeJ9KniUdHY337CdHOJ1k")
translator = Translator()
lang='en'
DEFAULT="Hi, I want to tell you how I'm feeling."
# # Reading history


# Initial setup

context= "Empathize and listen without offering unsolicited advice or tips. Support them in expressing feelings. If asked, assist in understanding their emotions."

def main():
    # permissions.request_admin_permissions()
    # os.system('cls' if os.name == 'nt' else 'clear')
    global starter
    starter=""

    
    # Generate initial response
    global response
    try:
        with open('hist.json', 'r') as f:
            # Try to load the JSON data
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        # If an error occurs, set data to None
        data = None


    starter=DEFAULT if data is None else translate(input("Continue Chatting:\n"))
    if starter.lower().strip()=="exit()":
        exit()
    if starter.lower() =="reset()" or starter.lower().strip()=="clear()":
            reset()
            print("Cleared")
            main()
    if data is not None:
        data.append({"author": "user", "content": f"{starter}"})
        starter=data
    print("\n")
    response = palm.chat(messages=starter, context=context, candidate_count=5, temperature=1)
    response.last = response.candidates[r(0,len(response.candidates)-1)]
    print(translate(response.last))

    # Chat loop
    for i in range(50):
        
        user_message = get_input()
        if user_message.lower() == "exit()":
            break
        if user_message.lower() =="reset()" or user_message.lower()=="clear()":
            reset()
            print("Cleared")
            main()
            break
    
        bot_message = reply(user_message)
        print(bot_message)


    # Your history list
    history = response.messages
    for item in history:
        if item['author'] == '0':
            item['author'] = 'user'
        elif item['author'] == '1':
            item['author'] = 'assistant'



    # Write the history list into hist.json
    with open('hist.json', 'w') as f:
        json.dump(history, f,indent=4)


    input("Press any key to exit...")
def reset():
    with open('hist.json', 'w') as f:
        pass
    
def translate(phr):
    global lang
    return translator.translate(phr, dest=lang).text

def translate_en(phr):
    return translator.translate(phr, dest="en").text
    
def get_input():
    while True:
        user_input = input("\nEnter your response:\n").strip()
        if user_input:
            return translate_en(user_input)
        else:
            print(f"Make sure to write something")

    

def reply(user_input):
    global response
    try:
        response = response.reply(user_input)
        
    except Exception as e:
        print(f"Error:{e}")
        exit()
    else:
        return (f"\nReply:\n{str(translate(response.last))}")

if __name__ == "__main__":
    main()
