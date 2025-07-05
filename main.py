from core.cognitive_unit import CognitiveUnit

def main():
    # Example: 5-dimensional input
    input_dim = 5
    goal_state = [0.5] * input_dim  # Arbitrary goal
    unit = CognitiveUnit(input_dim, goal_state)

    # Example input: closer to "Structure" archetype
    test_input = [1.0, 0.0, 0.0, 0.0, 0.0]
    output = unit.process(test_input)

    print("Layer Outputs:")
    for i, layer in enumerate(unit.layer_outputs):
        print(f"  L{i+1}: {layer}")

    print("\nContradiction Metrics:")
    for k, v in unit.last_contradictions.items():
        print(f"  {k}: {v:.4f}")

    print("\nFinal Output (Layer 10):", output)

if __name__ == "__main__":
    main()