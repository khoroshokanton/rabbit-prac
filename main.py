from config import init_log_config
import logging

init_log_config(logging.DEBUG)
log = logging.getLogger(__name__)


def main():
    log.info("Hello from rabbit-practice!")


if __name__ == "__main__":
    main()
