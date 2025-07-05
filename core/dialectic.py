import math

def rbf_kernel(x: list, y: list, gamma=1.0):
    return math.exp(-gamma * sum((xi - yi) ** 2 for xi, yi in zip(x, y)))

def compute_aspect_similarities(input_vec, archetypes: dict, gamma=1.0):
    return {aspect: rbf_kernel(input_vec, vec, gamma) for aspect, vec in archetypes.items()}