# English Grammar Correction

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
