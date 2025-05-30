'''client = Groq(api_key = 'secret' )


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





#with 2 LLMS


'''client = Groq(api_key = 'secret' )


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





# Normal llama two way communication with previous question summary , the next one includes 2 LLMs taliking
'''question_string = " "
question_summary = " ."

for i in range(2):
    question = input()
    question_string = question_string + question + "\n"

    if question == "end" or question == "quit":
        break

    # Combine the content elements into a single string
    assistant_content = (
        "You are given two strings, 1st contains the summary of the previous questions asked by the user and the next string contains the question asked by the user prevously refer to it for context if only if needed\n\n"
        f"Previous Questions Summary:\n{question_string}\n"
        f"Current Question:\n{question}"
    )

    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "assistant",
                # Use the combined string for content
                "content": assistant_content
            }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    for chunk in completion:
        print(chunk.choices[0].delta.content or "", end="")

    # CODE FOR STORING MEMORY AS SUMMARY

    # if question == "end" or question == "quit":
    # break

    # Combine the content elements into a single string for the summarization request as well
    summarization_content = (
        "Your role to to take  3 keywords from the questions asked previously and output just the 3 keywords and nothing else "
        f"Question String:\n{question_string}"
    )


    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "assistant",
                # Use the combined string for content
                "content": summarization_content
            }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    for chunk in completion:
        # Check if content is not None before concatenating
        if chunk.choices[0].delta.content is not None:
            question_summary = question_summary + chunk.choices[0].delta.content
    print(question_summary,question_string)'''
