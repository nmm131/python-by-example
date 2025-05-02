# 19_logging - Python by Example
import logging

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logging.debug("This is a DEBUG message")
    logging.info("This is an INFO message")
    logging.warning("This is a WARNING mesage")
    logging.error("This is an ERROR message")
    logging.critical("This is a CRITICAL message")

if __name__ == "__main__":
    main()
