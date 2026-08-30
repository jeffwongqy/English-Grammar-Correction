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
