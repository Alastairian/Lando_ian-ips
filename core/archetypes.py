"""
Defines archetypal vectors for use in dialectical aspect similarity.
You should expand or adjust these archetypes to fit your cognitive domain.
"""

from typing import Dict, List

# Example: Each archetype is a unit vector in a feature space.
# In practice, you may want to learn or tune these.
def default_archetypes(input_dim: int) -> Dict[str, List[float]]:
    # Example for Structure vs. Chaos (expand as needed)
    return {
        "Structure": [1.0] + [0.0]*(input_dim-1),
        "Chaos":    [0.0]*(input_dim-1) + [1.0],
        "Potential": [0.5]*input_dim,
        "Kinetic":   [-0.5]*input_dim,
        "Growth":    [0.7]*input_dim,
        "Sustainability": [-0.7]*input_dim,
    }