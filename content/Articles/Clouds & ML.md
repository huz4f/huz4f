---
cover:
  image: articles/mlc.png

tags: ["Machine Learning","Cloud Computing","DevOps", "Quantum computers"]

date: 2024-02-02

author: "Huzaif"
hideSummary: true
draft: false
---
# Cloud Computing & Modern day ML
>From being able to run tensorflow on collab to training models on sagemaker, \
By using cloud, complicated tasks of installing and managing dependencies on your local computer are taken care of. Not to mention worring about the limiting factors of your hardware.
Cloud computing makes practice of ML accessible to everyone and implementation readily availabe.


## Evolvement and need of Machine Learning:
We know, Machine Learning has evolved tremendously over the past decade and now has applications in nearly every field. There is a need for mastery of a wider toolset to move ML experiments from resource phase to more practical applications. \
But the work of building ML projects is really complex and tedious with a lot of manual workflows.We know we are still at the beginning of AI and ML although incredible amount of progress is being made and it holds the future of various industries from business, education, fintech to even healthcare. \
So far most of the development and testing of models have been done locally but the downside is you need multiple virtual environments for different models and frameworks, Also there is a limit to the amount of data you can load into the memory. \
The next common way to develop and run ML models is on a set of powerful servers which may seem less expensive up front, but either they are underutilized or need time and money.
## SageMaker & DevOps:
From not having to download large amount of data to having updated ml frameworks and algorithms at your finger tips,
SageMaker studio makes Machine Learning much convenient, scalable and fast. You can directly put training data from S3 to your customized EC2 instance,
Want to add new features? \
You dont have to go through the whole process of data prep, model training and deployment. You can use jenkins or [CodePipeLine](https://aws.amazon.com/codepipeline/features/) ;)

>SageMaker takes away most of your complex tasks and lets you focus on experimentation and training your models by its wide range toolkit. You can learn Amazon SageMaker even if you don't know much about ML, i also had trained only few regression and clustering models before starting SageMaker. (it's fun)
>
New features for convenience are created every day, \
You can read more about [SageMaker]( https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-mlconcepts.html) 
updates at their website: [here](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/sagemaker/)

## AWS & GPUs:
**From  having a relatively small neural network to waiting for many days of training** \
-There are various EC2 instances available with different GPU configurations that you can pick from, depending upon your budget and need of training model. 
>Now if you don't know why we use GPU. \
CPU are used for handling single complex tasks sequentially while GPU are great at handeling parellel tasks. Vectorization is core operation in ML (eg: bias and weight)
>
To utilize the computational power of GPUs we need strong software, \
Companies like NVIDIA are also working towards ML | AI as toolkits like TensorFlow need well designed acceleration libraries like 
[Cuda X](https://developer.nvidia.com/gpu-accelerated-libraries#:~:text=NVIDIA%20CUDA%2DX™%2C%20built,AI%20and%20high%2Dperformance%20computing.), everyone knows Ai Ml is a growing market with bright future, NVIDIA also has invested in [containers](https://catalog.ngc.nvidia.com/containers) that can help avoid dependencies hell.


Updated: 

Gordon Moore, co-founder of Intel, in 1965 observed that the number of transistors that could be packed onto an integrated circuit (IC) was doubling roughly every year. He later revised this to a doubling every two years.
![](/articles/Moore.png)
The pace of doubling has slowed significantly in recent years. We are still seeing improvements, not strictly at the same rate as before. But new possibilities we have today from 10 years ago are reshaping the boundaries of what is possible. Also quantum computers might be the future and after 10 years we will look at Integrated Circuits as vaccum tubes, who knows.
![](/articles/quantum.png)
**NVIDIA's capitalisation increased by the whole value of Coca-Cola in a single day**. 
>Why? 
>
It is the focus on AI that is pushing forward the requirement for increasing computing level. However, NVIDIA knows that they need to build on their base and advance into other areas. And, here is the move into [quantum computing](https://www.nvidia.com/en-us/solutions/quantum-computing/)

As advancement in internet and Quantum computers, All the power will be accessed through cloud.
As quantum computers need cold environment to work, it is hard to imagine to bring all the setup home.

---