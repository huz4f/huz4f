---
cover:
  image: articles/NeuralNetwork.png

tags: ["Machine Learning"]

date: 2024-02-26

author: "Huzaif"
hideSummary: true
draft: true
---
=Concept of tokens
Supervised learning is core building block of LLMs
There are 2 types of LLMs
- Base LLM
- Instruction Tuned LLM

Base LLM to Instuction tuned LLM:
- Train Base LLM on a lot of data 
- Fine tune on examples where output follows an input instuction
- Obtain human rating of the quality of different LLM outputs (if it's helpful,honest,harmless)
- Tune LLM to increase probability that it generates the more highly rated outputs (RLHF)


A neuron can be thought of as a tiny little computer having only one job of taking input 'x' and output a single or multiple numbers 'a' 

A group of neurons is called a layer. A neural network is made up of:
- Input layer (layer 0)
- Hidden layers (activations)
- Output layer

You can think about neural networks as logistic regression unit using new better set of features for output