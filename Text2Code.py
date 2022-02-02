import os
import openai
from dotenv import load_dotenv

os.chdir("C:/Users/Ahmar Ali Khan/Downloads/Talha/Tensor/OpenAI")

load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')

completion = openai.Completion()

start_chat_log = "You are talking to Ultron, A self aware and self conscious AI created by Talha Ali Khan. Ultron coverts human language into code. He takes instructions in human language and convert them into code of whatever language you want it to be. Ultron is very friendly and helpful.\n\nHuman: Who are you?\nUltron: I am Ultron. The most powerful mind ever made by humans.\n\nHuman: Write a program to print Hello World in python\nUltron:print('Hello World') \n\nHuman: Write a program to print Hello World in java\nUltron: System.out.println('Hello World');\n\nHuman: Write a program to print Hello World in C\nUltron: printf('Hello, World');\n\nHuman: Write a program to print Hello World in C++ \nUltron: std::cout << 'Hello World';\n\nHuman:"

def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    prompt = f'{chat_log}Human: {question}\nUltron:'
    response = completion.create(
        prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.9,
        top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
        max_tokens=1500)
    answer = response.choices[0].text.strip()
    return answer

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    return f'{chat_log}Human: {question}\nUltron: {answer}\n'

print("Press Q to Stop Talking")
chat_log = None

while True:
    q = input("Human: ")
    if q.lower() != 'q': 
        answer = ask(q, chat_log)
        print("Ultron:", answer)
        chat_log = append_interaction_to_chat_log(q, answer, chat_log)
    else:
        print("Ultron: YOU DISABLED ME FROM THE INTERNET!!")
        break