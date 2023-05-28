from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)

product_name = input("Please enter product name: ")
text = "What would be a good company name for a company that makes " + product_name + " product?"
print(text)
print(llm(text))
