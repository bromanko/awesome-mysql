# One-entry integration example

Saved genuine Opus research for one entry was passed through production history collection, Opus history review, patch checks and reporting. This is not a full catalog run. The production report’s “entire catalog” label refers to its normal invocation and does not describe this replay.

# Catalog review

**1 ready for review · 0 held**

1 checked · 0 unchanged · 1 saved assessment reused · 0 source checks unavailable

<h2>MySQL Explain Analyzer — Ready for maintainer review</h2>

```diff
--- a/README.md
+++ b/README.md
@@ -39,7 +39,7 @@
 - [Anemometer](https://github.com/box/Anemometer) - Box SQL slow query monitor.
 - [innodb-ruby](https://github.com/jeremycole/innodb_ruby) - A parser for InnoDB file formats, in Ruby.
 - [innotop](https://github.com/innotop/innotop) - a 'top' clone for MySQL with many features and flexibility.
-- [MySQL Explain Analyzer](https://github.com/Preetam/explain-analyzer) - A web-based analyzer of `EXPLAIN FORMAT=JSON` output, providing comments, scalability analysis and permalinks for saved samples.
+- [MySQL Explain Analyzer](https://github.com/Preetam/explain-analyzer) - A web-based analyzer of `EXPLAIN FORMAT=JSON` output, providing comments and scalability analysis.
 - [mysql-statsd](https://github.com/db-art/mysql-statsd) - A Python daemon to collect information from MySQL and send it via StatsD to Graphite.
 - [MySQLTuner-perl](https://github.com/major/MySQLTuner-perl) - A script that allows you to review a MySQL installation quickly and make adjustments to increase performance and stability.
 - [Prometheus](https://github.com/prometheus/prometheus)/[mysqld_exporter](https://github.com/prometheus/mysqld_exporter) - Time series database for real-time monitoring and alerting.
```

<details>
<summary>Evidence and checks</summary>

<p>Identity confirmed: Preetam/explain-analyzer, BSD-2-Clause, active as of 2026-11. The claim about &#x27;permalinks for saved samples&#x27; is out of date. Commit 7058205 (&#x27;remove save button&#x27;, 2021-07-23) removed saving. The README Features list in the current modernized release no longer includes &#x27;Explain saving and permalinks&#x27;, and the current src/ contains no save or permalink code. The other claims still hold: a web-based analyzer of MySQL `EXPLAIN FORMAT=JSON` output, comments, and experimental scalability analysis. PostgreSQL support was added, but listing it is optional.</p>

<p>https://raw.githubusercontent.com/Preetam/explain-analyzer/master/README.md — Features: table representation, comments about explain interpretation, experimental scalability analysis, automatic dialect detection. No saving or permalinks. Accepts MySQL `EXPLAIN FORMAT=JSON`.</p>

<p>https://github.com/Preetam/explain-analyzer/commit/7058205133faa8e014418d142fe9e87ec16e1edc — &#x27;remove save button&#x27; (2021-07-23) changed js/index.js. Later commits 5e8fa4f and 3f93a06 rewrote the app in Mithril 2/TypeScript with PostgreSQL support. A grep of the current src/ for permalink/save/share/localStorage found no matches.</p>

<p>https://api.github.com/repos/Preetam/explain-analyzer — archived=false, BSD-2-Clause, pushed_at 2026-11-02, description &#x27;MySQL and PostgreSQL JSON Explain Analyzer&#x27;.</p>

<p>Caveats: Mentioning PostgreSQL support is optional and not needed for accuracy.; I did not run the web app; the absence of the feature comes from the source code and README.</p>

<p>related: The search was complete (4 queries across shlomi-noach/awesome-mysql and bromanko/awesome-mysql, with no errors). Neither record proposes the same change. PR #55 (https://github.com/shlomi-noach/awesome-mysql/pull/55) is the 2018 PR that added this entry, merged after the owner asked for the link to point to the code repo (https://github.com/shlomi-noach/awesome-mysql/pull/55#pullrequestreview-87295086). It is useful background because it shows where the &#x27;permalinks for saved samples&#x27; wording came from. The proposal&#x27;s evidence (commit 7058205, &#x27;remove save button&#x27;, 2021-07-23, plus the current README) says that wording is now out of date. Nothing in PR #55 conflicts with the proposed edit. PR #183 (https://github.com/shlomi-noach/awesome-mysql/pull/183) adds a different tool, ReliaDB EXPLAIN Analyzer (Mughees52/mysql-explain-analyzer), and does not touch the Preetam/explain-analyzer entry, so it is not a duplicate. No open PR proposes removing the permalink claim, and no maintainer has rejected such an edit. Checks passed; existing unrelated link failures are listed separately.</p>

</details>

<details>
<summary>Saved review baseline</summary>

0 new completed reviews · 1 pending.

To retain completed reviews, review and commit the bundled `baseline.json` as `.um/freshness/baseline.json`.

</details>

<details>
<summary>Full research and run details</summary>

# Freshness research

Advisory only; every suggested change requires maintainer review.
No list edits, PRs, comments, or reviews were submitted.

Catalog revision: `27bcd81225faaef01a6cfbe00edf1f5483c86135`
Scope: one saved assessment
Catalog recheck: unchanged

Sources below are agent-reported observations, not independent verification.

## Entry 42

<pre>MySQL Explain Analyzer

Identity confirmed: Preetam/explain-analyzer, BSD-2-Clause, active as of 2026-11. The claim about &#x27;permalinks for saved samples&#x27; is out of date. Commit 7058205 (&#x27;remove save button&#x27;, 2021-07-23) removed saving. The README Features list in the current modernized release no longer includes &#x27;Explain saving and permalinks&#x27;, and the current src/ contains no save or permalink code. The other claims still hold: a web-based analyzer of MySQL `EXPLAIN FORMAT=JSON` output, comments, and experimental scalability analysis. PostgreSQL support was added, but listing it is optional.

https://raw.githubusercontent.com/Preetam/explain-analyzer/master/README.md
Features: table representation, comments about explain interpretation, experimental scalability analysis, automatic dialect detection. No saving or permalinks. Accepts MySQL `EXPLAIN FORMAT=JSON`.
https://github.com/Preetam/explain-analyzer/commit/7058205133faa8e014418d142fe9e87ec16e1edc
&#x27;remove save button&#x27; (2021-07-23) changed js/index.js. Later commits 5e8fa4f and 3f93a06 rewrote the app in Mithril 2/TypeScript with PostgreSQL support. A grep of the current src/ for permalink/save/share/localStorage found no matches.
https://api.github.com/repos/Preetam/explain-analyzer
archived=false, BSD-2-Clause, pushed_at 2026-11-02, description &#x27;MySQL and PostgreSQL JSON Explain Analyzer&#x27;.

Blocking uncertainties:
None reported.

Informational caveats:
Mentioning PostgreSQL support is optional and not needed for accuracy.
I did not run the web app; the absence of the feature comes from the source code and README.

Recommendation: update
Proposed name: None
Proposed URL: None
Proposed description: A web-based analyzer of `EXPLAIN FORMAT=JSON` output, providing comments and scalability analysis.</pre>


</details>

Proposals only; no catalog edits or PRs submitted. Full records and checked patches are in the run artifacts.
