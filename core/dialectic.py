"""
Dialectical logic utilities for aspect similarities and contradiction calculation.
"""

import math
from typing import Dict, List

def rbf_kernel(x: List[float], y: List[float], gamma=1.0) -> float:
    return math.exp(-gamma * sum((xi - yi) ** 2 for xi, yi in zip(x, y)))

def compute_aspect_similarities(
    input_vec: List[float], 
    archetypes: Dict[str, List[float]], 
    gamma=1.0
) -> Dict[str, float]:
    return {aspect: rbf_kernel(input_vec, vec, gamma) for aspect, vec in archetypes.items()}

def calc_internal_contradiction(aspect_similarities: Dict[str, float]) -> float:
    # Contradiction = high when multiple opposing aspects are similarly activated
    sims = list(aspect_similarities.values())
    if not sims:
        return 0.0
    mean = sum(sims)/len(sims)
    return sum(abs(s - mean) for s in sims) / len(sims)  # simple dispersion

def calc_external_contradiction(current: List[float], goal: List[float]) -> float:
    # Contradiction = distance to goal state
    return math.sqrt(sum((c-g)**2 for c, g in zip(current, goal)))

def calc_inter_contradiction(int_con: float, ext_con: float) -> float:
    # Inter-contradiction = interaction of internal and external
    return abs(int_con - ext_con)