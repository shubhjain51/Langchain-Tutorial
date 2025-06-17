# llm_chain.py

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load API key
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", temperature=0.7, google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Prompt template
prompt = PromptTemplate(
    input_variables=["question"],
    template="Answer the following question clearly and helpfully:\n\n{question}"
)

qa_chain = LLMChain(llm=llm, prompt=prompt)

def ask_question(question: str) -> str:
    result= qa_chain.invoke({"question": question})
    return result['text'].strip()  # 👈 This extracts only the plain response
