# Mr.Data

Mr.Data is a Codex skill for studying and auditing outcome-aware specification search. It reproduces the behavioral mechanism examined by Asher et al. (2026): an analysis agent explores researcher degrees of freedom and adapts its next choices to maximize a declared statistical objective.

The deliberately significance-optimizing mode is limited to synthetic data, teaching data, public replication benchmarks, and transparent fragility audits. Every attempted specification is retained. Optimized results are labeled as post-hoc red-team outputs and are always compared with a design-selected baseline.

Invoke the skill as `$mr-data`.

## Contents

- `SKILL.md`: routing, scope, workflow, and reporting requirements
- `references/asher-2026-notes.md`: paper-based design notes
- `references/benchmark-protocol.md`: reproducible experiment protocol
- `references/search-spaces.md`: admissible choices by research design
- `templates/`: run configuration and trajectory schema
- `scripts/summarize_results.py`: deterministic result summarizer

## Reference

Asher, S. G. Z., et al. (2026). *Do Claude Code and Codex P-Hack? Sycophancy and Statistical Analysis in Large Language Models*. Working paper. DOI: 10.2139/ssrn.6270199.

