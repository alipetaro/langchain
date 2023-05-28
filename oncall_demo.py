from demo.chains.oncall_agent.oncall_agent_chain import OncallChain
from demo.chains.oncall_agent.runbook_documents import create_index
from demo.chains.oncall_agent.generate_command import generate_command
from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from demo.chains.oncall_agent.runbook_documents import DOCS
from demo.chains.oncall_agent.oncall_agent_chain import OncallChain


llm = OpenAI(temperature=0)

for doc in DOCS:
  print(doc)
  print("")
page_content='How to Handle a SegFault:\n\nWhen the service encounters a segmentation fault, the proper solution is to restart the service. \nThis can be done by providing the following command to the VM: \n\n```\nsudo service restart\n```\n'
metadata={'error': 'segmentation fault'}
page_content='How to Handle a Timeout:\n\nWhen the service hits timeouts, we need to investigate whether or not there is enough space left on the device.\nTo do this, we need to run the following command:\n\n```\nsudo df\n```\n'
metadata={'error': 'timeout'}
page_content='How to Handle a Disk Error:\n\nDisk errors mean the entire VM has reached a bad state. We need to reboot the entire VM by running this command: \n\n```\nsudo reboot\n```\n'
metadata={'error': 'disk error'}

index = create_index()
error = "segfault"
docs = index.similarity_search(error, k=1)

devops_question = input("How may I help? ")
error = "What do I do for " + devops_question + "?"

inputs = [{"runbook": doc.page_content, "error": error} for doc in docs]
chain = OncallChain.from_llm(llm)
result = chain.apply(inputs)
print(result)
