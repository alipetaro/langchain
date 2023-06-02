from demo.chains.oncall_agent.oncall_agent_chain import OncallChain
from demo.chains.oncall_agent.runbook_documents import create_index
from langchain.llms import OpenAI
from demo.chains.oncall_agent.runbook_documents import DOCS
from demo.chains.oncall_agent.oncall_agent_chain import OncallChain


llm = OpenAI(temperature=0)

index = create_index()
count = 1
error = input("Hi! I am Buddy, how may I help?\n")
while (count > 0):
  
  if (error != 'bye' and error != 'quit'):
    docs = index.similarity_search(error, k=1)
    inputs = [{"runbook": doc.page_content, "error": error} for doc in docs]
    chain = OncallChain.from_llm(llm)
    result = chain.apply(inputs)
    print("Run:" + result[0]['text'])
    error = input("How may I help?\n")
  else:
    count = 0

print('Bye for now!')
