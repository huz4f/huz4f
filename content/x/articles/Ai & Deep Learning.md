---
cover:
  image: articles/Ai.png

tags: ["Artificial Intelligence","Deep Learning"]

date: 2024-02-26

author: "Huzaif"
hideSummary: true
draft: true
---
# Large Language Models
LLM can be thought as reeasoning engine rather than a knowledge store
Supervised learning is core building block of LLMs
There are 2 types of LLMs
- Base LLM
- Instruction Tuned LLM

Base LLM to Instuction tuned LLM:
- Train Base LLM on a lot of data 
- Fine tune on examples where output follows an input instuction
- Obtain human rating of the quality of different LLM outputs (if it's helpful,honest,harmless)
- Tune LLM to increase probability that it generates the more highly rated outputs (RLHF)

# Ai

>Here is what prompting in chatgpt does in the background:
>
Setting up programming environment to send prompts to OpenAI's cloudhosted service:
```python
import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY") 

def llm_response(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role':'user','content':prompt}],
        temperature=0
    )
    return response.choices[0].message['content']
```
Define a prompt that will classify the sentiment
```python
prompt = '''
    Classify the following review 
    as having either a positive or
    negative sentiment:
    I feel zesty
'''
response = llm_response(prompt)
print(response)
```
Retrieval Augmented Generation (RAG)
Fine tuning

LLMs are mostly used in ANI (arificial narrow intelligence)
