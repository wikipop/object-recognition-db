import logging

from modules.textAnalysis import TextAnalysis


def main():
    TextAnalysis()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("debug.log", mode="w"),
            logging.StreamHandler()
        ],
    )

    main()
