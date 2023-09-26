# ConstitutionAI

ConstitutionAI is a GPT-powered app that allows you to query the Indian constitution using OpenAI's GPT-3 model. It uses a combination of HuggingFace's transformers for embedding and OpenAI's language model for generating responses. The application is designed to provide quick and accurate responses to queries related to the Indian constitution.

## Features

- **Query the Indian Constitution**: Ask any question related to the Indian constitution and get a quick and accurate response.
- **Powered by GPT-3**: Leverages the power of OpenAI's GPT-3.5-turbo model for generating responses.
- **Open-source embedding model**: Uses `gte-base` for embedding the queries and the constitution articles.
- **ChromaDB**: Uses ChromaDB as a vector database.

## Installation

Before running the application, make sure you have installed the necessary dependencies. You can install them using poetry:

```
poetry install
```

## Usage

First, activate the virtual environment:

```
poetry shell
```

If you want to ingest the constitution data, use the `--ingest` flag:
    
```
python app.py --ingest
```

To run the application, simply run:

```
python app.py
```


Once the application is running, you can start asking questions:
    
```
> What is Article 1 of the Indian Constitution?

Article 1 of the Indian Constitution states that India, also known as Bharat, shall be a Union of States. It also specifies that the States and their territories are as mentioned in the First Schedule, and that the territory of India comprises the territories specified in the Constitution.
```

To exit the application, simply type `exit` or `quit`.

## Configuration

The application can be configured using the `config.yaml` file.

```yaml
embedding:
  model: "thenlper/gte-base"
openai:
  number_documents: 3
  temperature: 0.1
  stream: true
```