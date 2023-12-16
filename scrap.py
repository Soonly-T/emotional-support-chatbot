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