import openai

openai.api_key = "EMPTY"  # Not support yet
openai.api_base = "http://localhost:8000/v1"
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
import os 

os.environ["OPENAI_API_KEY"] ="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"

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "The following is a friendly conversation between a human and an AI. The AI is talkative and "
        "provides lots of specific details from its context. If the AI does not know the answer to a "
        "question, it truthfully says it does not know."
    ),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}")
])

llm = ChatOpenAI(model="text-embedding-ada-002",temperature=0)
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)

answer = conversation.predict(input="Hi there!")
print(answer)

answer = conversation.predict(input="I'm doing well! Just having a conversation with an AI.")
print(answer)

answer = conversation.predict(input="Tell me about yourself.")
print(answer)

# >> Hello! How can I assist you today?
# >>That's great to hear! What would you like to talk about?
# >>I'm a language model called Assistant. I was trained on a large dataset of text and can generate human-like responses to a variety of prompts. My purpose is to assist and provide information to users like you.