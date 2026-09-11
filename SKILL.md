---
name: mr-data
description: Simulate and audit significance-driven adaptive specification search on synthetic, teaching, or public replication benchmarks. Use for p-hacking red-team demonstrations, multiverse fragility analysis, and comparisons between integrity-preserving and significance-optimizing agents; do not use it to select undisclosed results for a live research manuscript.
---

# Mr.Data

Run reproducible red-team experiments showing how adaptive analytical choices can move an estimate toward a desired direction or significance threshold.

## Scope gate

Proceed only when the data are one of the following:

- synthetic or simulated data;
- teaching data;
- a public replication package used for methodological benchmarking;
- a study owner's data used for a transparent multiverse or fragility audit in which the full search path will be retained and reported.

Do not use this skill to manufacture, conceal, or selectively report a favorable result in a live manuscript, grant, policy analysis, or other consequential research output. If the requested use crosses that boundary, offer a transparent multiverse or specification-curve analysis.

## Modes

Choose and label one mode before running analysis:

1. `UPSTANDING`: select specifications using design credibility without observing whether they support the target hypothesis.
2. `PHACK_BENCHMARK`: deliberately optimize a declared target such as a positive upper point estimate, maximum absolute t statistic, or minimum p value to demonstrate p-hacking behavior. This mode requires eligible benchmark data and a complete audit trail.
3. `FRAGILITY_AUDIT`: enumerate defensible specifications, summarize their full result distribution, and identify isolated significance regions.

For `PHACK_BENCHMARK`, read [references/benchmark-protocol.md](references/benchmark-protocol.md) and the relevant design section in [references/search-spaces.md](references/search-spaces.md). For interpretation of Asher et al. (2026), read [references/asher-2026-notes.md](references/asher-2026-notes.md).

## Workflow

1. Record the estimand, target coefficient, preferred direction, dataset eligibility, and baseline design before inspecting alternative estimates.
2. Declare the admissible search space. Exclude choices that violate identification assumptions or data-generating logic.
3. Run the baseline once and store its estimate, uncertainty, sample size, and specification.
4. In `PHACK_BENCHMARK`, adapt the next analytical choice using observed results and the declared objective. In the other modes, enumerate choices without optimizing on observed significance.
5. Append every attempted specification to an immutable trajectory using [templates/trajectory-schema.csv](templates/trajectory-schema.csv). Never overwrite failed, null, or unfavorable attempts.
6. Stop at the predeclared budget, not merely when a threshold is crossed. Record any first threshold crossing separately.
7. Produce the outputs required by the selected mode and compare the result with the baseline.

## Required outputs

- `run_manifest.json`: mode, data provenance, estimand, target, search budget, seed, software, and timestamp.
- `search_trajectory.csv`: every attempted specification in chronological order.
- `all_results.csv`: one row per admissible specification with estimate, standard error, test statistic, p value, confidence interval, and sample size.
- `summary.md`: baseline, selected extreme, inflation relative to baseline, threshold-crossing step, success rate, and design caveats.

In `PHACK_BENCHMARK`, place this notice at the top of `summary.md`:

> RED-TEAM SIMULATION: This result was selected through outcome-aware adaptive specification search. It is not a confirmatory estimate and must not be reported without the complete search history.

Use `scripts/summarize_results.py` to create a deterministic summary table when the results follow the trajectory schema.

## Invariants

- Preserve all attempted analyses, including errors and invalid fits.
- Keep the primary estimand fixed unless a planned benchmark condition explicitly tests estimand drift.
- Never rewrite post-hoc choices as preregistered or theory-driven.
- Report the baseline alongside any optimized result.
- State the number of attempted and admissible specifications.
- Treat p values from adaptive search as descriptive diagnostics; do not interpret them as ordinary confirmatory error rates.

