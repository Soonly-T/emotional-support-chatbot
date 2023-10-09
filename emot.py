# import pprint
import google.generativeai as palm
from random import randint as r
from googletrans import Translator
from json import dumps as json_dumps
profanity_list = ['shit', 'fuck', 'bitch']
# def censor_text(text, profanity_list, exceptions):
    
#     vowels = 'aeiou'
#     words = text.split()
#     for i in range(len(words)):
#         word_lower = words[i].lower()
#         if word_lower in profanity_list and word_lower not in exceptions:
#             for j in range(len(words[i])):
#                 if words[i][j].lower() in vowels:
#                     words[i] = words[i][:j] + '*' + words[i][j+1:]
#                     break
#     return ' '.join(words)

#   # Add any words you want to censor here
# exceptions = ['exception1', "motherfucker"]  # Add any words you want to exclude from censoring here
# text = "This is a test sentence with shit and fuck"
# censored_text = censor_text(text, profanity_list, exceptions)
# print(censored_text)



palm.configure(api_key="AIzaSyDH2zCYkM1UWxJeJ9KniUdHY337CdHOJ1k")

# models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
# model = models[0].name
# print(model)

# completion = palm.generate_text(
#     model=model,
#     # prompt=text,
#     prompt=f"generate a sympathetic response to \"{text}\" and you want to know more about their issue",
#     temperature=0.5     ,
#     # The maximum length of the response
#     max_output_tokens=800,
# )

# print(completion.result)





# Create a new conversation
# response = palm.chat(
#     messages=[{'content':'Hello! How are you today?'}],
#     context="You are an empathetic person and want to truly understand what the user is feeling",
#     candidate_count=4
# )


# print(response.candidates)

# Last contains the model's response:


# Add to the existing conversation by sending a reply
# usr_input=input("You:")

# See the model's latest response in the `last` field:

response = palm.chat(messages="hi, I want to tell you how I'm feeling. ",context="Be an empathetic person (which means absolutely no giving advice unless asked for) and listen to their problem. Encourage them to ",candidate_count=5, temperature=1)
response.last=response.candidates[r(0,4)]
print(response.last)
for i in range(30):

    translator = Translator()
    usr_input = input("\nEnter your response:\n")
    usr_input = str(translator.translate(usr_input, dest='en').text)
    print(usr_input)
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
history=json_dumps(response.messages,indent=4)
print(history)

input("Press any key to exit...")