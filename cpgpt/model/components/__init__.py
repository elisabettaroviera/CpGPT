"""
Docstring for cpgpt.model.components

1. Cosa fa: re-esporta CpGPT e i moduli architetturali (positional encodings, MLP/Transformer
blocks, mask Hi-C) come API pubblica di components.
2. A cosa serve: semplifica e standardizza gli import, definendo cosa è “pubblico” nel
sottopacchetto.
3. Mi serve: non per il training, ma utile per usare/estendere la repo.
"""

from .model import CpGPT
from .modules import (
    AbsolutePositionalEncoding,
    ChromosomePositionalEncoding,
    L2ScaleNorm,
    MLPBlock,
    SwiGLU,
    TransformerPPBlock,
    create_hic_attention_mask,
)

__all__ = [
    "AbsolutePositionalEncoding",
    "ChromosomePositionalEncoding",
    "CpGPT",
    "L2ScaleNorm",
    "MLPBlock",
    "SwiGLU",
    "TransformerPPBlock",
    "create_hic_attention_mask",
]
