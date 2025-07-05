"""
Central controller for a Cognitive Unit. Adjusts processing based on contradictions.
"""

from typing import Any, Dict
from core.dialectic import calc_internal_contradiction, calc_external_contradiction, calc_inter_contradiction

class CoreNode:
    def __init__(self):
        self.state: Dict[str, Any] = {
            "layer_widths": [8]*6,  # e.g., default width for layers 4-9
            "plasticity": 1.0,      # how much to adapt layer sizes
        }

    def monitor(self, contradictions: Dict[str, float]):
        # Example: If contradiction is high, increase plasticity
        threshold = 0.5
        if contradictions["internal"] > threshold or contradictions["external"] > threshold:
            self.state["plasticity"] = min(2.0, self.state["plasticity"] + 0.1)
            self.state["layer_widths"] = [min(32, w+2) for w in self.state["layer_widths"]]
        else:
            self.state["plasticity"] = max(0.5, self.state["plasticity"] - 0.05)
            self.state["layer_widths"] = [max(4, w-1) for w in self.state["layer_widths"]]

    def get_layer_widths(self):
        return self.state["layer_widths"]