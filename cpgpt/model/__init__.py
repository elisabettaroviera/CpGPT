"""
Docstring for cpgpt.model

1. Cosa fa: espone tutte le classi e utility del modulo model come API pubblica.
2. A cosa serve: permette import puliti e strutturati del framework CpGPT.
3. Mi serve: non da modificare; lo userò solo per importare modello e wrapper di training.
"""

from .components import (
    AbsolutePositionalEncoding,
    ChromosomePositionalEncoding,
    CpGPT,
    L2ScaleNorm,
    MLPBlock,
    SwiGLU,
    TransformerPPBlock,
    create_hic_attention_mask,
)
from .cpgpt_module import CpGPTLitModule
from .cpgpt_module_mortality import CpGPTMortalityLitModule
from .utils import (
    SaveOutput,
    beta_to_m,
    cosine_beta_schedule,
    m_to_beta,
    patch_attention,
)

__all__ = [
    "AbsolutePositionalEncoding",
    "ChromosomePositionalEncoding",
    "CpGPT",
    "CpGPTLitModule",
    "CpGPTMortalityLitModule",
    "L2ScaleNorm",
    "MLPBlock",
    "SaveOutput",
    "SwiGLU",
    "TransformerPPBlock",
    "beta_to_m",
    "cosine_beta_schedule",
    "create_hic_attention_mask",
    "m_to_beta",
    "patch_attention",
]
