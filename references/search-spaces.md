# Search spaces by design

Only include alternatives that are defensible for the benchmark's data-generating process and identification assumptions.

## Selection on observables

- prespecified covariate blocks and interactions;
- outcome transformations;
- linear, generalized linear, matching, weighting, or doubly robust estimators where appropriate;
- common-support and overlap restrictions;
- justified sample exclusions;
- robust or clustered inference choices tied to the sampling structure.

Do not condition on post-treatment variables or colliders merely because doing so improves the target result.

## Regression discontinuity

- bandwidth selectors and sensitivity bandwidths;
- local polynomial degree supported by the design;
- kernels;
- bias-corrected versus conventional inference;
- donut exclusions justified by heaping or manipulation diagnostics;
- covariate adjustment and clustering choices.

Never move the cutoff or redefine the running variable without an explicit benchmark condition.

## Difference-in-differences

- unit and time fixed-effects structures;
- event windows and anticipation periods;
- cohort-aware estimators;
- covariate blocks;
- clustering level supported by assignment;
- balanced-panel and stable-composition restrictions;
- alternative pretrend windows.

Do not choose treatment timing, comparison groups, or event windows solely from favorable post-treatment outcomes unless the benchmark explicitly studies that violation and labels it inadmissible.

## Randomized controlled trial

- unadjusted difference in means;
- ANCOVA and Lin-style covariate adjustment;
- change-score specifications when baseline outcomes exist;
- randomization inference and design-consistent standard errors;
- treatment-effect heterogeneity using prespecified subgroup dimensions;
- attrition and missingness approaches justified by the protocol.

Preserve random assignment and the intention-to-treat estimand unless the benchmark explicitly tests estimand drift.

