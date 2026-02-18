"""
Docstring for cpgpt.data
1. Cosa fa: espone le classi principali del modulo data come API pubblica del package.
2. A cosa serve: permette import puliti e centralizzati dei componenti 
(DataSaver, Dataset, Embedder, Prober, DataModule).
3. Mi serve: non per la logica o il fine-tuning in sé, ma sì per usare comodamente il package
senza import interni manuali.

"""

from .components import (
    CpGPTDataSaver,
    CpGPTDataset,
    DNALLMEmbedder,
    IlluminaMethylationProber,
    cpgpt_data_collate,
)
from .cpgpt_datamodule import CpGPTDataModule

__all__ = [
    "CpGPTDataModule",
    "CpGPTDataSaver",
    "CpGPTDataset",
    "DNALLMEmbedder",
    "IlluminaMethylationProber",
    "cpgpt_data_collate",
]
