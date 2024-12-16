import logging
import time


def initialize_logger(name="halloween", level=logging.INFO):
    logging.getLogger("py4j.clientserver").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.basicConfig(
        level=level,
        format="%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    return logging.getLogger(name)


logger = initialize_logger()


def is_center(i, j, len_x, len_y) -> bool:
    return (i != 0 and i != len_x - 1) and (j != 0 and j != len_y - 1)


def is_corner(i, j, len_x, len_y) -> bool:
    return (i == 0 or i == len_x - 1) and (j == 0 or j == len_y - 1)


def exec_time(func):
    def funct_to_measured(*args, **kwargs):
        init = time.time()
        c = func(*args, **kwargs)
        total_time = round((time.time() - init) * 1000, 4)
        logger.info(f"Tiempo Total (ms): {total_time}")
        return c

    return funct_to_measured
