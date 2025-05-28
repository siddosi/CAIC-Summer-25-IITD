''' Week 1 submisssion  - chatbot, chatbot with 2 LLMS'''

'''client = Groq(api_key = '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' )


#Normal llama two way communication, the next one includes 2 LLMs taliking


for i in range(2):


  question  = input()


  if question == "end" or question == "quit":
    break




  completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
       {
        "role": "assistant",
        "content": (

                    question

                    )
         }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
           )



  for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")'''




#chatbot with 2 LLMS

'''client = Groq(api_key = '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' )


#Normal llama two way communication, the next one includes 2 LLMs taliking


for i in range(2):


  question  = input()


  if question == "end" or question == "quit":
    break




  completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
       {
        "role": "assistant",
        "content": (

                    question

                    )
         }
    ],
    temperature=2,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
           )


  ans = ""
  for chunk in completion:
    if chunk.choices[0].delta.content != None:
       ans = ans +  chunk.choices[0].delta.content
    else:
      ans += ""

  completion = client.chat.completions.create(
    #model="deepseek-r1-distill-llama-70b",
    model = "qwen-qwq-32b",
    messages=[
       {
        "role": "system",
        "content": (

                    "Your role is to check the ans given by the previous model, refine it and give the final answer, just print the final output and not your thinking and not </think> or <think>"

                    "Question: " + question + "Answer: " + ans

                    )
         }
    ],
    temperature=2,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
           )


  for chunk in completion:
      print(chunk.choices[0].delta.content or "", end="")
'''


