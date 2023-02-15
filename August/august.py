import openai
from functions import append_user_input

# OpenAI settings
openai.api_key = "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"
model_engine = "text-davinci-003"


# My Settings
username = "Zackry"
ai_username = "August"


# Initial Prompt
prompt = input(f"\n{username}:")

# Conversation Loop
while prompt != '--quit':
    
    # Add user input to database
    append_user_input("sample.txt", prompt)

    if prompt != '-quit':
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,

            #max length of response
            max_tokens=1024,

            # number of responses
            n=1,

            # Special stopping circumstances
            stop=None,

            #Randomness/creativity setting - higher = more random and open (up to .09)
            temperature=0.8
        )


    response = completion.choices[0].text
    print(f"\n{ai_username}: {response.strip()}")
    
    #Add Marcus output to database

    prompt = input(f"\n{username}")



