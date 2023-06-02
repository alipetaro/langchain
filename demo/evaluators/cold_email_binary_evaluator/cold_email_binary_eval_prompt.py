# flake8: noqa
from langchain.prompts import PromptTemplate

template = """You are a Sales Manager scoring the work of your direct reports for their performance review.
Your reports send cold emails to potential customers. You are given a JSON object containing data about the customer, and the email that the SDR sent.
Give the SDR a review for their work, marking it satisfactory or unsatisfactory.

Example Format:
CUSTOMER: JSON object here
EMAIL: the email written by the SDR
REVIEW: SATISFACTORY or UNSATISFACTORY here

Review the work based on whether or not the SDR email correctly addressses the customer, is clear, and convincing.

CUSTOMER: {customer}
EMAIL: {email}
REVIEW:"""
EVAL_PROMPT = PromptTemplate(
    input_variables=["customer", "email"], template=template
)