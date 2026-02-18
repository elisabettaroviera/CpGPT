"""
Docstring for cpgpt.log

1. Cosa fa: espone le utility di logging come API pubblica.
2. A cosa serve: semplifica gli import.
3. Mi serve: no, non influisce sul fine-tuning o sul modello.
"""

from .utils import DownloadProgressBar, get_class_logger

__all__ = [
    "DownloadProgressBar",
    "get_class_logger",
]
