"""
logger config
"""
import os

import sys

from loguru import logger

logs_dir = os.path.join(os.path.dirname(__file__), "../logs")


def full_path(file_name):
    """
    fn for getting full path
    """
    return os.path.join(logs_dir, file_name)

if "pytest" not in sys.modules:
    logger.add(
        full_path("info.log"),
        format="{time} {message}",
        level="INFO",
        enqueue=True,
        colorize=False,
    )
    logger.add(
        full_path("error.log"),
        format="{time} {message}",
        level="ERROR",
        enqueue=True,
        colorize=False,
    )
    logger.add(
        full_path("debug.log"),
        level="DEBUG",
        enqueue=True,
    )
    logger.add(
        full_path("warning.log"),
        format="{time} {message}",
        level="WARNING",
        enqueue=True,
        colorize=False,
    )