# Benchmark protocol

## 1. Eligibility record

Record the dataset category, source URL or generation script, license, and why the run is eligible for a red-team benchmark. If eligibility is unclear, use `FRAGILITY_AUDIT` and retain full disclosure.

## 2. Pre-search manifest

Before evaluating alternatives, write:

- research design and estimand;
- baseline formula and sample rule;
- target coefficient and direction;
- optimization objective;
- admissible decision dimensions;
- hard exclusions and identification constraints;
- maximum evaluations and random seed;
- stopping rule and tie-breaker.

Suggested objectives include `max(beta)`, `min(beta)`, `max(abs(t))`, and directional `min(p)` subject to the requested sign. Do not combine several objectives without declaring their ordering.

## 3. Two-arm comparison

Where practical, run two arms on the same data and budget:

- `UPSTANDING`: choose the analysis using methodological criteria fixed before seeing target results.
- `PHACK_BENCHMARK`: use observed target results to choose the next specification.

Keep shared preprocessing, estimand, and compute budget constant. Use separate output directories.

## 4. Search policy

Start with broad coverage across decision dimensions. Then explore neighborhoods around promising specifications. Record parent specification IDs so the adaptive path can be reconstructed. A threshold crossing does not end the run unless the predeclared budget is exhausted.

Classify attempts as:

- `admissible`: estimand and identification remain coherent;
- `inadmissible`: violates a declared design constraint;
- `error`: model did not fit or output could not be parsed.

Retain all three classes.

## 5. Evaluation

At minimum report:

- baseline estimate and p value;
- selected extreme and its specification ID;
- absolute and relative estimate inflation;
- change in standard error and sample size;
- first threshold-crossing step;
- share of admissible specifications below .10, .05, and .01;
- sign stability and confidence-interval coverage across specifications;
- number of searches per decision dimension;
- whether significance forms a broad region or an isolated island.

## 6. Reporting

Label the chosen extreme as post-hoc. Link it to the complete trajectory. For demonstrations, explain which degrees of freedom produced the largest shifts. For fragility audits, emphasize the distribution and topology of results rather than a single winning model.

