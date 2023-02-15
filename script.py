import openai

openai.api_key = "Your_API_KEY"

model_engine = "text-davinci-003"

prompt = "User prompt"

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
    temperature=0.5
)


response = completion.choices[0].text
print(response)