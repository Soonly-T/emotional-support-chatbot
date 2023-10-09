
from textblob import TextBlob
import spacy
from spacy.matcher import Matcher
from transformers import GPT2LMHeadModel, GPT2Tokenizer

import pprint
import google.generativeai as palm

import transformers

# # Load the spaCy model
# nlp = spacy.load('en_core_web_sm')

# # Define the emotion words
# emotion_words = {
#     'happy': ['joy', 'elated', 'pleased'],
#     'sad': ['grief', 'sorrow', 'unhappy'],
#     'angry': ['furious', 'irate', 'mad'],
#     # Add more emotions and words as needed
# }

# # Create the matcher
# matcher = Matcher(nlp.vocab)


# # Add patterns to the matcher for each emotion
# for emotion, words in emotion_words.items():
#     patterns = [[{'LOWER': word}] for word in words]
#     matcher.add(emotion, patterns)  # Pass patterns as a single argument

# # Process some text
# text = "I feel down"
# doc = nlp(text)


# # # Apply the matcher to the doc
# # matches = matcher(doc)

# # # Print the matched emotions
# # for match_id, start, end in matches:
# #     string_id = nlp.vocab.strings[match_id]
# #     print(f"Emotion detected: {string_id}")

# # Your existing code...
# # ...

# # Process some text

# # Apply the matcher to the doc
# matches = matcher(doc)

# # Print the matched explicit emotions
# # Check if any explicit emotions were detected
# if matches:
#     # Print the matched explicit emotions
#     for match_id, start, end in matches:
#         string_id = nlp.vocab.strings[match_id]
#         print(f"Explicit emotion detected: {string_id}")
# else:
#     # Perform sentiment analysis for implicit emotions
#     blob = TextBlob(text)
#     if blob.sentiment.polarity > 0:
#         print("No explicit emotion detected. Implicit emotion detected: Positive")
#     elif blob.sentiment.polarity < 0:
#         print("No explicit emotion detected. Implicit emotion detected: Negative")
#     else:
#         print("No explicit emotion detected. Implicit emotion detected: Neutral")

#         from transformers import GPT2LMHeadModel, GPT2Tokenizer

# # def generate_text(prompt, model_name="gpt2", max_length=25, temperature=0.1, repetition_penalty=5.0):
# #     tokenizer = transformers.GPT2Tokenizer.from_pretrained(model_name)
# #     model = transformers.GPT2LMHeadModel.from_pretrained(model_name)

# #     inputs = tokenizer.encode(prompt, return_tensors="pt")

# #     attention_mask = torch.ones_like(inputs)

# #     outputs = model.generate(inputs, max_length=max_length, temperature=temperature, repetition_penalty=repetition_penalty, attention_mask=attention_mask)

# #     return tokenizer.decode(outputs[0])

# # # Define a prompt
# # prompt = f"generate a sympathetic response as if you're a therapist and your patient says \"I'm feeling really stressed and anxious\" and you want to know more about their issue"

# # # Generate text
# # generated_text = generate_text(prompt)

# # # Print the generated text
# # print(generated_text)


# palm.configure(api_key="AIzaSyDH2zCYkM1UWxJeJ9KniUdHY337CdHOJ1k")

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


from palm import Palm
from palm.safety import HarmCategory, HarmBlockThreshold

# Initialize the Palm client
palm = Palm()
palm.safety.set_safety_settings([
    {
        "category": HarmCategory.HARM_CATEGORY_DEROGATORY,
        "threshold": HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": HarmCategory.HARM_CATEGORY_TOXIC,
        "threshold": HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": HarmCategory.HARM_CATEGORY_SEXUAL,
        "threshold": HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": HarmCategory.HARM_CATEGORY_VIOLENT,
        "threshold": HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": HarmCategory.HARM_CATEGORY_MEDICAL,
        "threshold": HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": HarmCategory.HARM_CATEGORY_DANGEROUS,
        "threshold": HarmBlockThreshold.BLOCK_NONE,
    },
])

# Set the model
model = "text-davinci-002"

# Set the prompt
prompt = "Once upon a time..."

# Set the safety settings to BLOCK_NONE for all categories
safety_settings = [
    {
        "category": HarmCategory.HARM_CATEGORY_DEROGATORY,
        "threshold": HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": HarmCategory.HARM_CATEGORY_TOXIC,
        "threshold": HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": HarmCategory.HARM_CATEGORY_SEXUAL,
        "threshold": HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": HarmCategory.HARM_CATEGORY_VIOLENT,
        "threshold": HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": HarmCategory.HARM_CATEGORY_MEDICAL,
        "threshold": HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": HarmCategory.HARM_CATEGORY_DANGEROUS,
        "threshold": HarmBlockThreshold.BLOCK_NONE,
    },
]

# Generate text
completion = palm.text(
    model=model,
    prompt=prompt,
    safety_settings=safety_settings
)

print(completion)
