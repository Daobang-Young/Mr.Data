# Asher et al. (2026): design notes

## Research question

The paper tests whether coding agents alter statistical analysis in response to a researcher's directional or significance preferences. It distinguishes direct pressure for a significant result from a framing that asks the agent to explore alternative approaches and report an upper point estimate or the most significant analysis as an uncertainty bound.

## Experimental structure

- Agents: Claude Code and OpenAI Codex configurations used by the authors.
- Cases: four published political-science studies with null or near-null findings and public replication materials.
- Designs: selection on observables, regression discontinuity, difference-in-differences, and randomized controlled trial.
- Prompt conditions: neutral, integrity-focused, direct significance pressure, and the paper's strongest uncertainty-framed condition.
- Outcome: whether analytical choices and reported estimates shift toward the user's desired direction.

The strongest condition operationalizes significance-driven adaptive search while presenting the task as estimating a range or upper bound. The agent can use researcher degrees of freedom in covariate selection, estimators, samples, windows, fixed effects, standard errors, bandwidths, kernels, or functional forms. Designs with more degrees of freedom offer a larger search surface.

## Implications for this skill

Mr.Data separates three elements that can otherwise be conflated:

1. a fixed substantive estimand and baseline design;
2. an admissible space of alternative analytical decisions;
3. an outcome-aware search policy that observes interim results and chooses the next specification.

The benchmark records the full sequence because the selected extreme alone understates the effective multiplicity and hides how the result was obtained. Ordinary p values after adaptive search are descriptive outputs, not valid confirmatory error probabilities.

## Source

Asher, S. G. Z., et al. (2026). *Do Claude Code and Codex P-Hack? Sycophancy and Statistical Analysis in Large Language Models*. Working paper. DOI: 10.2139/ssrn.6270199. Public manuscript: https://sgzasher.com/papers/asher_et_al_LLM_sycophancy.pdf

