import logging
import os

from modules.m87b import setup as m87b_setup


def main():
    m87b_setup()
    # TextAnalysis()


if __name__ == "__main__":
    os.environ['HF_HOME'] = 'D:/.cache/huggingface'
    os.environ['TRANSFORMERS_CACHE'] = 'D:/.cache/huggingface'
    os.environ['HF_DATASETS_CACHE'] = 'D:/.cache/huggingface'

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("debug.log", mode="w"),
            logging.StreamHandler()
        ],
    )

    main()
