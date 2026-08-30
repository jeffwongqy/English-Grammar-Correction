import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnablePassthrough

st.title("✍️ English Grammar Correction Pipeline")
st.write("Grammar correction using Langchain RunnableSequence")


llm  = ChatOllama(model = "llama3.2", temperature = 0, num_ctx = 1024)


analysis_prompt = ChatPromptTemplate.from_template(
    
    """
    You are an English grammar expert.
    
    Analyze this sentence:
    {sentence}
    
    Identify the important grammar, spelling, word-choice, and punctuation errors.
    
    Provide brief explanation for each error. 
    
    Do not rewrite the sentence yet.
    """
)

correction_prompt = ChatPromptTemplate.from_template(
    
    """
    You are an English grammar correction expert. 
    
    Original sentence:
    {sentence}
    
    Grammar analysis:
    {analysis}
    
    Correct the sentence.
    
    Rules:
    - Preserve the original meaning.
    - Use only standard English.
    - Do not add unnecessary information.
    - Return only the corrected sentence. 
    """
)

explanation_prompt = ChatPromptTemplate.from_template(
    
    """
    You are an English language teacher.
    
    Original sentence:
    {sentence}
    
    Corrected sentence: 
    {correction}
    
    Explain the main changes made.
    
    Keep the explanation concise and easy to understand. 
    """
)

analysis_chain = analysis_prompt | llm | StrOutputParser()
correction_chain = correction_prompt | llm | StrOutputParser()
explanation_chain = explanation_prompt | llm | StrOutputParser()

grammar_pipeline = RunnableSequence(
    
    RunnablePassthrough.assign(
        analysis = analysis_chain
    ), 
    
    RunnablePassthrough.assign(
        correction = correction_chain
    ), 
    
    RunnablePassthrough.assign(
        explanation = explanation_chain
    )
)

sentence = st.text_area("Enter an English sentence", 
                        height = 120, 
                        placeholder = ("Example: She don't like to go school yesterday"))

if st.button("Correct Grammar"):
    if not sentence.strip():
        st.warning("Please enter a sentence.")
    else:
        with st.spinner("Analyzing and correcting ..."):
            result = grammar_pipeline.invoke({'sentence': sentence})
    
        st.subheader("Original Sentence")
        st.write(result["sentence"])
        
        st.subheader("Grammar Analysis")
        st.write(result["analysis"])
        
        st.subheader("Corrected Sentence")
        st.write(result["correction"])
        
        st.subheader("Explanation")
        st.write(result["explanation"])