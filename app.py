import os
from dotenv import load_dotenv

load_dotenv()

from embedchain import CustomApp
from embedchain.config import BaseLlmConfig
from embedchain.embedder.huggingface import (
    BaseEmbedderConfig,
    HuggingFaceEmbedder,
)
from embedchain.llm.openai import OpenAILlm
from embedchain.vectordb.chroma import ChromaDB
import yaml
import pandas as pd


os.environ["TOKENIZERS_PARALLELISM"] = "false"

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

embed_config = BaseEmbedderConfig(model=config["embedding"]["model"])
llm_config = BaseLlmConfig(
    number_documents=config["openai"]["number_documents"],
    temperature=config["openai"]["temperature"],
    stream=config["openai"]["stream"],
)
hf_embedder = HuggingFaceEmbedder(config=embed_config)

app = CustomApp(
    llm=OpenAILlm(llm_config),
    embedder=hf_embedder,
    db=ChromaDB(),
)


def ingest():
    df = pd.read_csv("data/constitution.csv")
    combined = df["article_id"] + "\n" + df["article_desc"]
    combined_texts = combined.tolist()

    for text in combined_texts:
        app.add(text, data_type="text")


def ask():
    while True:
        question = input("> ")
        if question.strip() == "":
            break
        if question == "exit" or question == "quit":
            break
        response = app.query(question)
        print()
        for chunk in response:
            print(chunk, end="", flush=True)
        print()
        print()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--ingest", action="store_true", help="Ingest the constitution"
    )
    args = parser.parse_args()

    if args.ingest:
        ingest()
        exit()

    ask()
