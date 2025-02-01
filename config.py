import logging


def init_log_config(level=logging.INFO):
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="%(asctime)s - %(name)s - %(levelname)-7s - %(message)s",
    )
