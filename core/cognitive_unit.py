"""
A single 10-layer Cognitive Unit with dynamic contradiction handling.
"""

from typing import List, Dict
from core.dialectic import (
    compute_aspect_similarities, 
    calc_internal_contradiction, 
    calc_external_contradiction, 
    calc_inter_contradiction
)
from core.core_node import CoreNode
from core.archetypes import default_archetypes

class CognitiveUnit:
    def __init__(self, input_dim: int, goal_state: List[float]):
        self.input_dim = input_dim
        self.goal_state = goal_state
        self.archetypes = default_archetypes(input_dim)
        self.core_node = CoreNode()
        self.layer_outputs: List[List[float]] = [[] for _ in range(10)]
        self.last_contradictions: Dict[str, float] = {}

    def process(self, input_data: List[float]) -> List[float]:
        # L1: Input
        self.layer_outputs[0] = input_data

        # L2: Opposing Aspects
        aspect_sims = compute_aspect_similarities(input_data, self.archetypes)
        self.layer_outputs[1] = list(aspect_sims.values())

        # L3: Contradictions
        internal = calc_internal_contradiction(aspect_sims)
        external = calc_external_contradiction(input_data, self.goal_state)
        inter = calc_inter_contradiction(internal, external)
        contradictions = {"internal": internal, "external": external, "inter": inter}
        self.layer_outputs[2] = [internal, external, inter]
        self.last_contradictions = contradictions

        # Notify CoreNode
        self.core_node.monitor(contradictions)
        widths = self.core_node.get_layer_widths()

        # L4-L9: Intermediate dynamic layers (simulate with simple transforms)
        x = self.layer_outputs[2]
        for i in range(3, 9):
            # Example: expand/contract vector based on layer width, apply nonlinearity
            width = widths[i-3]
            x = [(xi + (j+1)*0.01) % 1.0 for j, xi in enumerate([sum(x)]*width)]
            self.layer_outputs[i] = x

        # Core Node (feedbacks already handled via monitor)
        # L10: Output/Solution
        self.layer_outputs[9] = [sum(self.layer_outputs[8])/len(self.layer_outputs[8])]
        return self.layer_outputs[9]