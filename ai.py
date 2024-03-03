from openai import OpenAI
import time

def input_func():
    prompt = input("What's on your mind today?\n")
    return prompt

def ai_user_io(user_input):
    client = OpenAI(api_key='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')
    while True:
        # user_input = input_func()

        """
        if prompt == 'exit' or prompt == 'quit':
            print('Exiting Elaini - Have a great day!')
            break
        """

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            model="gpt-3.5-turbo"
        )

        elaini_answer = chat_completion.choices[0].message.content

        return elaini_answer

        # print(elaini_answer + "\n")
        # time.sleep(2)

# ai_user_io()
