import openai


openai.api_key = 'YOUR API KEY'

delimiter = "####"
prompt = f'''YOUR PROMPT HERE
    '''
messages = [{"role":"system", "content":prompt}]

def get_completion(prompt, model="gpt-3.5-turbo"):

  #messages = [{"role":"system", "content":prompt}]
  messages.append({"role":"user", "content":prompt_input},)
  chat = openai.ChatCompletion.create(model=model, messages=messages, temperature=0)
  response = chat.choices[0].message["content"]
  return response

while True:
  prompt_input = input("Enter a prompt to the AI:   ")
  print(get_completion(prompt_input) )
