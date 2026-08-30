# English Grammar Correction

<img width="850" height="430" alt="istockphoto-1134880364-612x612" src="https://github.com/user-attachments/assets/654814e0-5c61-458f-a0dd-4504e8c819be" />


## 1. Introduction 
English grammar correction is an important application of Natural Language Processing (NLP) that aims to identify and correct errors in written English. Traditional grammar-checking systems often rely on predefined linguistic rules, while modern Large Language Models (LLMs) can understand sentence context and provide more flexible corrections.

This project develops an English Grammar Correction Pipeline using **LangChain RunnableSequence** and **Ollama**. The system processes a user's sentence through a series of sequential stages. First, the LLM analyzes the sentence and identifies grammar, spelling, punctuation, and word-choice errors. Next, the identified errors are used to generate a corrected sentence. Finally, the system provides a brief explanation of the corrections.

The application is implemented using Streamlit to provide an interactive user interface, while LangChain RunnableSequence manages the sequential workflow. Ollama is used to run the LLM locally, allowing the project to demonstrate how LLM-based linguistic analysis can be integrated into a simple NLP application.

## 2. Aim 
To develop a simple LLM-based English grammar correction application that uses LangChain RunnableSequence and Ollama to analyze grammatical errors, generate corrected sentences, and provide explanations through a Streamlit interface.

## 3. Objectives
- Develop an English grammar analysis pipeline using an open-source LLM running through Ollama.
- Implement LangChain RunnableSequence to process grammar correction tasks sequentially: grammar analysis, sentence correction, correction explanation
- Design effective prompt templates for identifying grammar, spelling, punctuation, and word-choice errors.
- Build an interactive Streamlit application that allows users to enter English sentences and view the analysis and corrected output.
- Evaluate the quality of the corrections by testing the pipeline with sentences containing different types of grammatical errors.
- Demonstrate the application of LLMs to computational linguistics, particularly automated grammar analysis and language correction.

## 4. Langchain RunnableSequence 

```python
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnablePassthrough
```

### 4.1 Ollama LLM
Configures the local llama3.2 model to perform the linguistic analysis and correction tasks.

```python
llm  = ChatOllama(model = "llama3.2", temperature = 0, num_ctx = 1024)
```

### 4.2 Analysis Prompt
Instructs the LLM to identify grammar, spelling, word-choice, and punctuation errors without correcting the sentence.

```python
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
```

### 4.3 Correction Prompt 
Uses the original sentence and grammar analysis to generate a grammatically corrected sentence while preserving its meaning.

```python
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
```

### 4.4 Explanation Prompt
Instructs the LLM to explain the main grammatical changes in a concise and understandable manner.

```python
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
```

### 4.5 Langchain Chains
Connects each prompt to the LLM and StrOutputParser to convert the model response into readable text.

```python
analysis_chain = analysis_prompt | llm | StrOutputParser()
correction_chain = correction_prompt | llm | StrOutputParser()
explanation_chain = explanation_prompt | llm | StrOutputParser()
```

### 4.6 RunnableSequence Pipelines
Executes the analysis, correction, and explanation stages sequentially while preserving the information generated at each stage.

```python
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
```

### 4.7 User Input
Allows users to enter an English sentence for grammatical analysis and correction.

```python
sentence = st.text_area("Enter an English sentence", 
                        height = 120, 
                        placeholder = ("Example: She don't like to go school yesterday"))
```

### 4.8 Validation 
Checks whether the user has entered a sentence before executing the pipeline.

### 4.9 Pipeline Execution 
Invokes the complete RunnableSequence and processes the submitted sentence through all three stages.

### 4.10 Output Display
Presents the original sentence, identified errors, corrected sentence, and explanation separately in the Streamlit interface.

```python
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

```

## 5. Testing Common English Grammatical Errors
1. She go to the store every morning.
2. I have two cat at my house.
3. Me and him like playing soccer.
4. She sings very good during the show.
5. Yesterday, I walk to the park and buy ice cream.
6. He is married with a wonderful doctor.
7. Walking down the street, the tall buildings looked amazing.
8. The scientist whom discovered the cure won an award.
9. If I would have known the truth, I would tell you.
10. The box of old letters and photos that were found in the attic are valuable.
11. Although exhausted from the long shift, the patient's chart was forgotten by the nurse.
12. The list of rare books that we found in the attic are very valuable.
13. Because the prize was given to Sarah and I, we felt very honored.
14. By the time the rescue team arrived at the mountain, the heavy snowstorm buried the cabin.
15. The accountant whom managed the company finances suddenly resigned yesterday.
16. The director insisted that every actor arrives on time for rehearsals.
17. Since Mark wanted to reduce his stress and traveling less, he changed jobs.
18. If she would have studied harder for the final exam, she passed with an A.
19. Because he was afraid of to fail the test, he studied all night.
20. While she was the smartest of the two sisters, she struggled with geometry.

## 6. Demo Working Implementation
