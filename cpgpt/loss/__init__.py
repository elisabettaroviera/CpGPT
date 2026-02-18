"""
Docstring for cpgpt.loss

1. Cosa fa: rende pubbliche le funzioni loss del progetto.
2. A cosa serve: API organizzativa per training flessibile.
3. Mi serve: no per classificazione standard; utile solo per task survival/contrastive
o se richiamate dal modulo principale.
"""

from .loss import (
    beta_loss,
    c_index_loss,
    censored_mae_loss,
    contrastive_loss,
    cph_loss,
    gompertz_aft_loss,
    kld_bernoulli_loss,
    kld_normal_loss,
    robust_loss,
    wd_loss,
)

__all__ = [
    "beta_loss",
    "c_index_loss",
    "censored_mae_loss",
    "contrastive_loss",
    "cph_loss",
    "gompertz_aft_loss",
    "kld_bernoulli_loss",
    "kld_normal_loss",
    "robust_loss",
    "wd_loss",
]
