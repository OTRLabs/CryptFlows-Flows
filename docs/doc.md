Introduction:
What is CryptFlows?

CryptFlows, is a Langchain-style, LLM agent framework 

Why CryptFlows?

CryptFlows is designed to provide assistance to cyber security professionals during a wide variety of different types of offensive security situations. This includes but is not limited to:

Penetration tests
red team engagements
cyber range practicing


It is designed to act as a "second pair of hands". It is able to preform recon, research, & analyze the general state of the cyber world using threat intelligence feeds.






The plan is to create a system that begins as follows:
Development 

The project will be built using python 
Libraries & Dependencies:

python package manager: PDM
WebUI: Litestar + Vite
Langchain: LLM & Agent orchestration + data access & analysis!
container runtime: podman
Workflow orchestration: Apache airflow?
Database: SQlite for user auth, duckdb for the knowledge base 
ORM: advanced_alchemy, extension for SQLalchemy which allows use of DuckDB
Ollama + Ollama HTTP API : LLM runtime
Hugging face: specialized LLM runtime for more specific models
Outlines, structured text generation using hugging face LLMs & models. can be used for advanced decision making.
Techniques:

LLMRouting: using lighter models based on the question/prompt, allowing for computing power to be saved in the process. This can be done using Ollama as the platform supports many different models, and allows us to use the “right tool for the job”


The idea is: use python for the central “logic handler” or “main loop” of the system, and have it deploy containerized applications that can preform individual tasks as functions and return data to the main function for further processing and analysis 

For example: we will make heavy use of Project Discovery’s arsenal of network recon tools, each of which can be used as a docker (or in our case podman) container


These containers should be deployed using the podman/docker library for python. Ideally, we would have fairly generic tasks made into functions that can take many (optional as well as required) arguments that allow you to customize the containerized environment, the configuration settings for the actual test/action being preformed, and more.

The goal is to be able to use a single function to call the same program/test/whatever, but have maximum control & flexibility over how the tool is used. 

For example, ideally, we would only have one function which we use to create nmap containers, however that one function would accept the arguments for

- std nmap args

- proxychains config file to use for the scans

Milestones:
Stage 1: CTF & Hack the Box Labs

We intend to use simple, private CTF labs such as hack the box, TryHackMe, etc to train the system to perform basic vulnerability detection & analysis, and carry out basic exploits, as well as developing the most important part! The logging, and reporting systems

We will be using these CTFs as a way to establish the base capabilities of our agent framework without bothering anyone with unnecessary bullshit reports


The primary focus of this section will be achieving 

accurate scope assessment 
Accurate security research
Accurate vulnerability assessment & exploitation when relevant 

Stage 2: Open Bug bounty programs 

NOTICE: at no point should the system ever ever ever submit any type of report to any external service. We cannot guarantee 100% accuracy and the idea of wasting someone’s time with an unwarranted & unnecessary security issue is physically painful to think about. We do not want this thing to be submitting reports to hackerone without some human validation & verification 


Notice 2: the primary focus of these stages will be on demonstrating any potential vulnerabilities and issues found in systems. I would like to give the system some form of video manipulation abilities (pymovie?) and allow it to create demonstrations of the exploit, or whatever 

Stage 3: Penetration Testing 

Stage 4: TBD!


Moving forward I want to begin to develop the systems that are used to preform the actual cyber security tests, assessments, etc

We are going to want to make heavy use of containers to create isolated environments where we can preform these assessments 

These containers will essentially operate as “sub-scripts” in a way, as they are prewritten and predefined scripts. 

They may be simply running a tool & awaiting the output 

They may be running services like `metasploit`, the `sqlmap server`, etc which are regularly used 

If you are playing hack the box you can deploy a parrot os container that you proxy into and use openvpn to connect to the htb servers


——


We must keep in mind that the goal is to create a “reasoning” application, capable of doing research and assessing whether things are or are not the case

This goes beyond just running nmap scans, we will also need to use search engines, LLMs, maybe reinforcement learning

Some things we need to think about handling:

- context window / short term memory / information relevant to the current task should be, I guess json data with either text or URLs linking to media to be analyzed 

- media: this could be documents, probably stored in S3, using seaweed fs. All types of files. Most of it is markdown documents containing research & resources on cybersecurity 

- duckdb for indexing long term knowledge, ranging from text to URLs linking to media in the s3

- SQLite for basic information such as the projects we are working on, the scope of those projects, the tasks in the queue
