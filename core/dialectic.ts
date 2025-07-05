// Utilities for dialectical processing

import { Aspect } from "./cognitiveUnit";

// Example: Compute RBF similarity to each aspect archetype
export function computeAspectSimilarities(input: number[], archetypes: Record<Aspect, number[]>): Record<Aspect, number> {
  const similarities: Record<Aspect, number> = {} as any;
  for (const aspect in archetypes) {
    similarities[aspect] = rbfKernel(input, archetypes[aspect]);
  }
  return similarities;
}

function rbfKernel(x: number[], y: number[], gamma = 1.0): number {
  let sum = 0;
  for (let i = 0; i < x.length; i++) {
    sum += (x[i] - y[i]) ** 2;
  }
  return Math.exp(-gamma * sum);
}