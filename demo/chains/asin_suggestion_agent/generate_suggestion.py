from typing import List
from langchain.chat_models import ChatOpenAI
import itertools
import streamlit as st

from evalagents.agents.sdr_agent.sdr_agent_chain import SalesDevelopmentRepresentativeChain

@st.cache_data
def get_inferences(inputs: List[str], _llm: LLM):
    """
    Generate inferences
    @param inputs: text to generate inferences from
    @param _llm: text to generate inferences from
    @return: inference set as JSON list
    """
    st.info("`Generating eval set ...`")
    chain = SalesDevelopmentRepresentativeChain.from_llm(_llm)
    inferences = []
    
    for text in inputs:
        inf = chain.run(str(text))
        inferences.append(inf)

    inferences_full = list(itertools.chain.from_iterable(inferences))
    return inferences_full