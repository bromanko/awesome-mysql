# Catalog review inventory

**12 proposed changes · 7 uncertain · 9 unresolved keeps**

112 entries researched. 84 saved reviews for recurring runs.

Research recommendations from the initial Opus review. The full set has not passed prior-discussion or patch validation. Proposed diffs are previews, not approved patches. Nothing was applied or submitted.

Catalog: `27bcd81225faaef01a6cfbe00edf1f5483c86135` · README SHA-256: `32164431b18be910a06e9c46d312eea2ff6f4ce74b20be6111916336c50b7e3b`

## Proposed changes

<h3>MySQL Explain Analyzer — update</h3>

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
<summary>Evidence and limitations</summary>

<p>Identity confirmed: Preetam/explain-analyzer, BSD-2-Clause, active as of 2026-11. The claim about &#x27;permalinks for saved samples&#x27; is out of date. Commit 7058205 (&#x27;remove save button&#x27;, 2021-07-23) removed saving. The README Features list in the current modernized release no longer includes &#x27;Explain saving and permalinks&#x27;, and the current src/ contains no save or permalink code. The other claims still hold: a web-based analyzer of MySQL `EXPLAIN FORMAT=JSON` output, comments, and experimental scalability analysis. PostgreSQL support was added, but listing it is optional.</p>

<p>https://raw.githubusercontent.com/Preetam/explain-analyzer/master/README.md — Features: table representation, comments about explain interpretation, experimental scalability analysis, automatic dialect detection. No saving or permalinks. Accepts MySQL `EXPLAIN FORMAT=JSON`.</p>

<p>https://github.com/Preetam/explain-analyzer/commit/7058205133faa8e014418d142fe9e87ec16e1edc — &#x27;remove save button&#x27; (2021-07-23) changed js/index.js. Later commits 5e8fa4f and 3f93a06 rewrote the app in Mithril 2/TypeScript with PostgreSQL support. A grep of the current src/ for permalink/save/share/localStorage found no matches.</p>

<p>https://api.github.com/repos/Preetam/explain-analyzer — archived=false, BSD-2-Clause, pushed_at 2026-11-02, description &#x27;MySQL and PostgreSQL JSON Explain Analyzer&#x27;.</p>

<p>Caveats: Mentioning PostgreSQL support is optional and not needed for accuracy.; I did not run the web app; the absence of the feature comes from the source code and README.</p>

<p>Independent source check: The saved-permalink claim is outdated. Current app code has analyze/example controls but no save handler or routes. Historical removal of the save feature corroborates the current implementation; an old README alone would not have been enough.</p>

<p>https://github.com/Preetam/explain-analyzer/blob/master/README.md — Current features describe analysis, comments, scalability and dialects.</p>

<p>https://github.com/Preetam/explain-analyzer/blob/master/src/App.ts — Current application has input, parse, analyze and example-loading paths, without the former save feature.</p>

<p>https://github.com/Preetam/explain-analyzer/blob/master/src/main.ts — Mounts the application without permalink routing.</p>

<p>https://github.com/Preetam/explain-analyzer/commit/7058205133faa8e014418d142fe9e87ec16e1edc — Historical commit removes the save button and handler.</p>

</details>

<h3>sql-tap — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -47,7 +47,7 @@
 - [ReliaDB EXPLAIN Analyzer](https://github.com/Mughees52/mysql-explain-analyzer) - a browser-based MySQL and MariaDB EXPLAIN visualizer with issue detection, index recommendations, and query rewrites. 100% client-side.
 - [Wireshark](https://gitlab.com/wireshark/wireshark/) - a protocol analyzer that can decode the MySQL protocol.
 - [Dolphie](https://github.com/charles-001/dolphie) - a modern terminal tool for real-time analytics into MySQL/MariaDB & ProxySQL
-- [sql-tap](https://github.com/mickamy/sql-tap) - Real-time SQL traffic viewer.
+- [sql-tap](https://github.com/proto-tap/sql-tap) - Real-time SQL traffic viewer.
 
 ## Backup
 
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL github.com/mickamy/sql-tap redirects. The GitHub API returns 301 to repository id 1157577714, whose full_name is proto-tap/sql-tap. The README install instructions now use github.com/proto-tap/sql-tap and the proto-tap/tap Homebrew cask, and explicitly note the move from mickamy/tap. The name and description (&#x27;Real-time SQL traffic viewer&#x27; matches the README) remain accurate, and MySQL is a supported driver. Only the URL needs to change.</p>

<p>https://api.github.com/repos/mickamy/sql-tap — HTTP 301 to api.github.com/repositories/1157577714, which resolves to full_name &#x27;proto-tap/sql-tap&#x27;, owner proto-tap, archived=false, MIT, pushed_at 2026-10-27.</p>

<p>https://raw.githubusercontent.com/proto-tap/sql-tap/main/README.md — &#x27;Real-time SQL traffic viewer — proxy daemon + TUI / Web client.&#x27; Works with PostgreSQL, MySQL, or TiDB. Install: &#x27;go install github.com/proto-tap/sql-tap@latest&#x27;. A note says it moved from mickamy/tap to proto-tap/tap.</p>

<p>Caveats: The README still has a sponsor badge for github.com/sponsors/mickamy. The original author appears to remain involved, but I did not check proto-tap org membership.; Adding a TUI/web mention to the description is optional.</p>

<p>Independent source check: Canonical repository moved from mickamy/sql-tap to proto-tap/sql-tap. Old URL redirects; this is a supported cleanup, not a broken-project claim.</p>

<p>https://api.github.com/repos/mickamy/sql-tap — Repository response resolves to full_name proto-tap/sql-tap, repository ID 1157577714.</p>

<p>https://github.com/proto-tap/sql-tap/blob/main/README.md — Current installation instructions use the new organization and explicitly describe the Homebrew tap move.</p>

</details>

<h3>Databasus — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -53,7 +53,7 @@
 
 *Backup/restore/recovery tools*
 
-- [Databasus](https://github.com/databasus/databasus) - tool for scheduled MySQL backups via web UI with external storages (local, S3, FTP, Google Drive, etc.), notifications (webhook, Discord, Slack, etc.) and team management.
+- [Databasus](https://github.com/databasus/databasus) - tool for scheduled MySQL backups via web UI with external storages (local, S3, FTP, etc.), notifications (webhook, Discord, Slack, etc.) and team management.
 - [Dumpling](https://github.com/pingcap/tidb/tree/master/dumpling) - Logical, parallel backup/dumper tool for MySQL/TiDB written in GoLang - support csv format output and integrated as library
 - [MyDumper](https://github.com/mydumper/mydumper) - Logical, parallel backup/dumper tool for MySQL
 - [Percona Xtrabackup](https://github.com/percona/percona-xtrabackup) - an open-source hot backup utility for MySQL - based servers that doesn’t lock your database during the backup.
```

<details>
<summary>Evidence and limitations</summary>

<p>databasus/databasus is canonical, Apache-2.0 licensed, and active. The project now positions itself mainly as a PostgreSQL backup tool, but its README still lists MySQL 5.7–9/26 support (logical backups only), so it still fits the Backup section. Scheduled backups, web UI, webhook/Discord/Slack notifications and team features (workspaces, access management) are still documented, and local, S3 and FTP storage are still listed. Google Drive is not: neither the README storage list nor the official Storages docs page (Local, S3, Cloudflare R2, Azure Blob, NAS, FTP, SFTP) mentions it, and backend/go.mod has no Google Drive API dependency. I recommend removing that example; non-exhaustive &#x27;etc.&#x27; wording keeps it durable.</p>

<p>https://raw.githubusercontent.com/databasus/databasus/main/README.md — Tagline &#x27;PostgreSQL backup tool&#x27;. Supported databases: PostgreSQL 14–18 (physical and logical), MySQL 5.7, 8.0, 8.4, 9 and 26 (logical only), MariaDB, MongoDB. Storages: &#x27;S3, Cloudflare R2, Azure Blob Storage, NAS, FTP, SFTP and more&#x27;. Notifiers: Email, Telegram, Slack, Discord, Teams, Mattermost, webhooks. Workspaces and access management. No mention of Google Drive.</p>

<p>https://databasus.com/storages — Supported storages: Local Storage, S3, Cloudflare R2, Azure Blob Storage, NAS, FTP, SFTP. Google Drive is absent.</p>

<p>https://raw.githubusercontent.com/databasus/databasus/main/backend/go.mod — Includes Azure blob, minio (S3), jlaffaye/ftp and pkg/sftp clients, and go-sql-driver/mysql. There is no google.golang.org/api (Drive) module.</p>

<p>https://api.github.com/repos/databasus/databasus — archived=false, Apache-2.0, pushed 2026-11-10, description &#x27;PostgreSQL backup tool with Point-In-Time-Recovery and restore verification&#x27;.</p>

<p>Caveats: The README says &#x27;and more&#x27; after the storage list. Removal of Google Drive is inferred from the official docs list and the dependency manifest; I did not find a changelog entry that announces it.; The project&#x27;s focus has shifted to PostgreSQL. MySQL support is logical-only but still documented.; I did not run the software.</p>

<p>Independent source check: Current code explicitly removed built-in Google Drive storage, and subsequently removed rclone storage too. Removing Google Drive from the current supported-destination examples is supported. Older releases retain it; MySQL support itself remains.</p>

<p>https://github.com/databasus/databasus/blob/main/backend/migrations/20261109083400_remove_google_drive_storage.sql — Migration states Google Drive support ended after 3.67.0 and rejects remaining configured Google Drive storages.</p>

<p>https://github.com/databasus/databasus/blob/main/backend/migrations/20261109134345_remove_rclone_storage.sql — Subsequent migration states 3.67.1 was the last rclone-supporting release and removes its storage support.</p>

<p>https://github.com/databasus/databasus/blob/main/backend/internal/modules/storages/internal/providers/type.go — Current storage enum contains local, S3, NAS, Azure Blob, FTP and SFTP, without Google Drive or rclone.</p>

</details>

<h3>libAttachSQL — remove</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -96,7 +96,6 @@
 - [DBD::MariaDB](https://github.com/perl5-dbi/DBD-MariaDB) - MariaDB and MySQL driver for the Perl5 Database Interface.
 - [DBD::mysql](https://github.com/perl5-dbi/DBD-mysql) - MySQL driver for the Perl5 Database Interface.
 - [go-sql-driver](https://github.com/go-sql-driver/mysql) - a lightweight and fast MySQL-Driver for Go's (golang) database/sql package.
-- [libAttachSQL](https://github.com/libattachsql/libattachsql) - libAttachSQL is a lightweight, non-blocking C API for MySQL servers.
 - [MariaDB Connector/J](https://github.com/mariadb-corporation/mariadb-connector-j) - LGPL-licensed MariaDB Client Library for Java Applications.
 - [mex-mariadb](https://github.com/markuman/mex-mariadb) - MIT licensed MariaDB/MySQL Client Library for GNU Octave and Matlab.
 - [MySQL C API](https://dev.mysql.com/downloads/c-api/) - Official C driver for MySQL.
```

<details>
<summary>Evidence and limitations</summary>

<p>The project&#x27;s own official GitHub repository description reads &#x27;* NOTE: This is now a dead project and used for CI testing * A lightweight C API for MySQL servers&#x27;. That is affirmative official evidence of discontinuation, and the list rules say &#x27;Code must not be abandoned/discontinued&#x27;. The project homepage libattachsql.org returns HTTP 502 (supporting only, not decisive). Per the contribution rules, removal should be proposed by opening an issue; no documented successor was found.</p>

<p>https://github.com/libattachsql/libattachsql — Repository description/title: &#x27;* NOTE: This is now a dead project and used for CI testing * A lightweight C API for MySQL servers&#x27;.</p>

<p>https://raw.githubusercontent.com/libattachsql/libattachsql/master/README.rst — README points to libattachsql.org and Travis/Waffle badges; says master has an unstable API and recommends the v1.0 branch for a stable API.</p>

<p>http://libattachsql.org/ — Returned HTTP 502 (access failure, not used as sole evidence).</p>

<p>Caveats: The v1.0 branch is referenced as the stable API, but its maintenance status was not examined and should not be inferred from its existence; the dead-project notice applies to the project as a whole.; Removal must go through an issue per contribution rules; this is a recommendation for that discussion.</p>

</details>

<h3>wtx — remove</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -111,7 +111,6 @@
 - [PyMySQL](https://github.com/PyMySQL/PyMySQL) - MySQL database connector for Python.
 - [Ruby Mysql2 gem](https://github.com/brianmario/mysql2) - MySQL driver for Ruby and Rails projects.
 - [MyZql](https://github.com/speed2exe/myzql) - MySQL and MariaDB driver in native Zig.
-- [wtx](https://github.com/c410-f3r/wtx) - Client for MySQL/MariaDB/Percona written in Rust
 
 ## Deployment
 
```

<details>
<summary>Evidence and limitations</summary>

<p>Recommend opening a removal issue, not a patch. The listed project no longer provides the MySQL/MariaDB/Percona client the entry describes. Commit e266e965fb (2026-05-01, PR #523) deleted wtx/src/database/client/mysql*, the MySQL example and the MySQL integration-test scripts. The current wtx/Cargo.toml has only postgres features, and the database-client docs and README cover only PostgreSQL. The project is still active, but its MySQL interface has been removed. Version 0.44.2 still had the mysql feature.</p>

<p>https://github.com/c410-f3r/wtx/commit/e266e965fb — Commit &#x27;feat!: Allow the decoding and encoding of arbitrary collections&#x27; (2026-05-01, PR #523) removes wtx/src/database/client/mysql.rs, the mysql/ submodule files, wtx-examples/database/database-client-mysql.rs, .scripts/integration-tests-mysql.sh and .test-utils/mysql.sh.</p>

<p>https://raw.githubusercontent.com/c410-f3r/wtx/main/wtx/Cargo.toml — Current manifest (version 0.52.1) defines postgres and postgres-pool features. No mysql, mariadb or percona feature exists. A recursive tree listing of main has no mysql paths.</p>

<p>https://raw.githubusercontent.com/c410-f3r/wtx/main/wtx-docs/src/database-client/README.md — Database Client docs document only PostgreSQL.</p>

<p>https://github.com/c410-f3r/wtx/blob/3cd0350316/wtx/Cargo.toml — At tag wtx-0.44.2 (2026-04-21) the manifest still had &#x27;mysql = [&quot;database&quot;, ...]&#x27;. MySQL support existed until this release line.</p>

<p>https://github.com/c410-f3r/wtx/issues/280 — Issue &#x27;[MySQL] Add support for MariaDB/MySQL/Percona&#x27; was closed 2025-02-23. MySQL support was added around March 2025 (commit &#x27;Add MySQL client&#x27;) and later removed.</p>

<p>Caveats: The removal commit and PR #523 give no reason, and I found no statement on whether MySQL support might return.; Older crates.io releases (≤0.44.x) still include the mysql feature. They are a legacy line, and I did not verify their maintenance status.</p>

</details>

<h3>Shift — replace</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Shift README now officially states: &#x27;Shift is no longer under active development. Its successor is SchemaBot, Block&#x27;s GitOps tool for database schema changes&#x27;, with online MySQL changes run by Spirit. Block is Square&#x27;s parent company, and the notice was merged into square/shift in 2026-09. The project is therefore officially discontinued, which conflicts with the &#x27;must not be abandoned/discontinued&#x27; condition, and it names an official successor. block/schemabot is Apache-2.0, actively released (v0.1.83 on 2026-11-03), and its README badges MySQL support as GA. Because this effectively removes Shift, the change should go through an issue.</p>

<p>https://raw.githubusercontent.com/square/shift/master/README.md — NOTE block: &#x27;Shift is no longer under active development. Its successor is SchemaBot (https://github.com/block/schemabot), Block&#x27;s GitOps tool for database schema changes ... Online MySQL schema changes run with Spirit.&#x27;</p>

<p>https://github.com/square/shift/commits/master — Latest commits: 2026-09-04/08 &#x27;Point readers to SchemaBot and Spirit in the README&#x27; (merged PR #112). The previous functional commit is from 2020-09.</p>

<p>https://github.com/block/schemabot — GitHub API: block/schemabot, not archived, Apache-2.0, created 2026-04-07, pushed 2026-11-10. Description: &#x27;Define your database schema in code and apply changes safely through pull requests or the CLI&#x27;.</p>

<p>https://raw.githubusercontent.com/block/schemabot/main/README.md — README badges: &#x27;MySQL: GA&#x27;, &#x27;Vitess: GA&#x27;, &#x27;PostgreSQL: early alpha&#x27;. Declarative and GitOps-driven: compares SQL files to the live database and applies changes through PRs or a CLI. Releases v0.1.81–v0.1.83 in Oct–Nov 2026.</p>

<p>Blocking questions: SchemaBot is young (created 2026-04, v0.1.x, a few dozen stars). Whether it meets the list&#x27;s &#x27;reasonably recognized and adopted&#x27; / GA-quality conditions, or should go under Incubating, needs maintainer judgement.</p>

<p>Caveats: SchemaBot is declarative/GitOps, whereas Shift was a UI-driven pt-osc runner. The workflows differ, but the successor relationship is officially stated.; I did not run either tool.</p>

</details>

<h3>DBeaver — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -139,7 +139,7 @@
 *GUI frontends & applications*
 
 - [Adminer](https://github.com/vrana/adminer/) - Database management in a single PHP file.
-- [DBeaver](https://github.com/dbeaver/dbeaver/) - A cross-platform SQL and NoSQL database client.
+- [DBeaver](https://github.com/dbeaver/dbeaver/) - A cross-platform universal database tool and SQL client.
 - [StackRender](https://github.com/stackrender/stackrender) - Free and open-source database schema design and SQL migration generator for MySQL. 
 - [HeidiSQL](https://github.com/HeidiSQL/HeidiSQL) - MySQL GUI frontend for Windows.
 - [ILLA Cloud](https://github.com/illacloud/illa-builder) - Low-code internal tool builder integrated with Mysql, can be used as GUI for Mysql. 
```

<details>
<summary>Evidence and limitations</summary>

<p>DBeaver remains a relevant open-source, multi-platform GUI with MySQL support. However, the &#x27;SQL and NoSQL&#x27; claim does not hold for the linked repository, which is the Community edition. Its README says the commercial versions &#x27;support NoSQL databases&#x27; (MongoDB, Cassandra, Redis, etc.) and that commercial versions &#x27;include NoSQL databases support&#x27;. Suggested wording follows the official repo description and README.</p>

<p>https://raw.githubusercontent.com/dbeaver/dbeaver/devel/README.md — &#x27;Free multi-platform database tool for developers, SQL programmers, database administrators and analysts.&#x27; Under &#x27;PRO versions&#x27;: &#x27;Commercial versions extends functionality of community drivers, supports NoSQL databases and many more: ... Cassandra, ... MongoDB, ... Redis ...&#x27;. Later: commercial versions &#x27;include NoSQL databases support&#x27;. The Community list includes MySQL and MariaDB.</p>

<p>https://github.com/dbeaver/dbeaver — GitHub API: not archived, Apache-2.0, default branch devel, pushed_at 2026-11-10. Description: &#x27;Free universal database tool and SQL client&#x27;.</p>

<p>Caveats: The Community driver list includes a few non-relational sources accessed through SQL/JDBC (e.g. Elasticsearch, OpenSearch, Solr). The suggested wording avoids the NoSQL claim rather than enumerating them.</p>

</details>

<h3>LibreDB Studio — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -143,7 +143,7 @@
 - [StackRender](https://github.com/stackrender/stackrender) - Free and open-source database schema design and SQL migration generator for MySQL. 
 - [HeidiSQL](https://github.com/HeidiSQL/HeidiSQL) - MySQL GUI frontend for Windows.
 - [ILLA Cloud](https://github.com/illacloud/illa-builder) - Low-code internal tool builder integrated with Mysql, can be used as GUI for Mysql. 
-- [LibreDB Studio](https://github.com/libredb/libredb-studio) - Browser-based SQL IDE for MySQL and nine other engines, deployed as a container or Helm chart next to the database.
+- [LibreDB Studio](https://github.com/libredb/libredb-studio) - Browser-based SQL IDE for MySQL and many other engines, deployed as a container or Helm chart next to the database.
 - [mycli](https://github.com/dbcli/mycli) - A Terminal Client for MySQL with AutoCompletion and Syntax Highlighting.
 - [MySQL Shell](https://github.com/mysql/mysql-shell/) - Advanced client and code editor for MySQL that supports development and administration for the MySQL Server and MySQL InnoDB cluster (AdminAPI) with an interactive JavaScript, Python, or SQL interface.
 - [MySQL Workbench](https://github.com/mysql/mysql-workbench) - provides DBAs and developers an integrated tools environment for database design & modeling; SQL devleopment; database administration.
```

<details>
<summary>Evidence and limitations</summary>

<p>The repository is reachable at libredb/libredb-studio and is MIT licensed. It is still a browser-based SQL IDE that deploys next to the data as a container or Helm chart. However, the count in &#x27;MySQL and nine other engines&#x27; is out of date: the current README says &#x27;Forty-two engines share one interface&#x27;. The suggested replacement drops the count, since it is likely to keep changing.</p>

<p>https://raw.githubusercontent.com/libredb/libredb-studio/main/README.md — Reads &#x27;Forty-two engines share one interface: PostgreSQL, MySQL, Oracle, Db2 LUW, SQL Server, ...&#x27; and &#x27;It deploys next to the data: a container, a Helm chart, an operator, a one-click template on your PaaS, or npm i @libredb/studio&#x27;. Quick start uses docker run ghcr.io/libredb/libredb-studio:latest. License is MIT.</p>

<p>https://github.com/libredb/libredb-studio — Resolves with HTTP 200 and no redirect, so the canonical owner/name is unchanged.</p>

<p>Caveats: Other install paths (Homebrew, Snap, winget, desktop wrapper) also exist. The description does not need to list them.; The software was not run.</p>

</details>

<h3>MySQL Workbench — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -146,7 +146,7 @@
 - [LibreDB Studio](https://github.com/libredb/libredb-studio) - Browser-based SQL IDE for MySQL and nine other engines, deployed as a container or Helm chart next to the database.
 - [mycli](https://github.com/dbcli/mycli) - A Terminal Client for MySQL with AutoCompletion and Syntax Highlighting.
 - [MySQL Shell](https://github.com/mysql/mysql-shell/) - Advanced client and code editor for MySQL that supports development and administration for the MySQL Server and MySQL InnoDB cluster (AdminAPI) with an interactive JavaScript, Python, or SQL interface.
-- [MySQL Workbench](https://github.com/mysql/mysql-workbench) - provides DBAs and developers an integrated tools environment for database design & modeling; SQL devleopment; database administration.
+- [MySQL Workbench](https://github.com/mysql/mysql-shell-plugins) - provides DBAs and developers an integrated environment for SQL development, database administration and migration.
 - [Ocelot GUI](https://github.com/ocelot-inc/ocelotgui) - GUI client for MySQL or MariaDB, including debugger.
 - [OmniDB: Web tool for database management](https://github.com/OmniDB/OmniDB)
 - [Percona Monitoring and Management](https://github.com/percona/pmm) - An open-source platform for managing and monitoring MySQL performance.
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed repository mysql/mysql-workbench now officially describes itself as &#x27;the now EOL version of MySQL Workbench 8&#x27; and points to https://github.com/mysql/mysql-shell-plugins for the new Workbench. That repository&#x27;s README says it contains the source code for MySQL Workbench. Official release notes show 8.0.47 (2026-04-23) followed by Workbench 26.7.0 and 26.10.0. This is the same product from the same owner (mysql), not a competitor. The current description also has a typo (&#x27;devleopment&#x27;) and claims design &amp; modeling, which the new Workbench README does not mention. The suggested wording follows the new README.</p>

<p>https://github.com/mysql/mysql-workbench — Repository description: &#x27;This repository contains the now EOL version of MySQL Workbench 8. For the new Workbench, see https://github.com/mysql/mysql-shell-plugins&#x27;. Default branch is 8.0, last commit 2026-04-02.</p>

<p>https://raw.githubusercontent.com/mysql/mysql-shell-plugins/master/README.md — &#x27;It also contains the source code for MySQL Workbench, which is built on MySQL Shell and these plugins.&#x27; Also: &#x27;MySQL Workbench is a desktop application for developing, administering, and migrating MySQL databases. It includes a rich SQL editor, database administration and maintenance tools, and migration tools.&#x27;</p>

<p>https://github.com/mysql/mysql-shell-plugins — Repository description: &#x27;Plugins for the MySQL Shell, including the new MySQL Workbench 26&#x27;.</p>

<p>https://dev.mysql.com/doc/relnotes/workbench/en/ — Release notes index lists Workbench 26.10.0 (2026-10-21), 26.7.0 (2026-09-10) and 8.0.47 (2026-04-23) as the last 8.0 release.</p>

<p>https://raw.githubusercontent.com/mysql/mysql-workbench/8.0/README.md — The 8.0 README still describes SQL development, data modeling, server administration and data migration.</p>

<p>Caveats: mysql-shell-plugins also holds other MySQL Shell plugins (MDS, MRS, MSM, Utils), so the URL points at a broader repository than Workbench alone.; Whether Workbench 26 keeps the visual data-modeling features of 8.0 was not confirmed. The suggested description leaves that claim out rather than asserting it.; License of the new repo was not checked through the API (rate-limited). WORKBENCH_DEV.md carries GPLv2 text.</p>

</details>

<h3>Galera Cluster — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -162,7 +162,7 @@
 
 *High availability solutions*
 
-- [Galera Cluster](https://github.com/codership/galera) - a true Multimaster Cluster based on synchronous replication.
+- [Galera Cluster](https://github.com/mariadb-corporation/galera) - a true Multimaster Cluster based on synchronous replication.
 - [mha4mysql-node](https://github.com/yoshinorim/mha4mysql-node) and [mha4mysql-manager](https://github.com/yoshinorim/mha4mysql-manager) (both unmaintained) - Master High Availability Manager and tools for MySQL.
 - [Orchestrator](https://github.com/ProxySQL/orchestrator) - MySQL replication topology management and High Availability solution.
 - [Percona Replication Manager](https://github.com/percona/replication-manager) - Asynchronous MySQL replication manager agent for Pacemaker. Supports file and GTID based replication, geo-distributed clusters using booth.
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL https://github.com/codership/galera now redirects to https://github.com/mariadb-corporation/galera. The packet snapshot also resolves to mariadb-corporation/galera, and galeracluster.com now redirects to MariaDB&#x27;s Galera Cluster documentation, which corroborates the ownership change. The project and its description (synchronous multi-master replication) are unchanged, so only the canonical URL should be updated.</p>

<p>https://github.com/codership/galera — Following redirects ends at https://github.com/mariadb-corporation/galera with HTTP 200.</p>

<p>https://raw.githubusercontent.com/codership/galera/4.x/README — &#x27;This is Galera replication - Codership&#x27;s implementation of the write set replication (wsrep) interface&#x27;, GPLv2. The README still credits Codership.</p>

<p>https://galeracluster.com — Redirects to https://mariadb.com/docs/galera-cluster (&#x27;MariaDB Galera Cluster&#x27;).</p>

<p>Caveats: Repository description per the snapshot is &#x27;Synchronous multi-master replication library&#x27;. The word &#x27;true&#x27; in the entry is mild puffery, but not a factual error.; The exact date and terms of the Codership to MariaDB transfer were not read from an announcement.</p>

</details>

<h3>Percona Replication Manager — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -165,7 +165,7 @@
 - [Galera Cluster](https://github.com/codership/galera) - a true Multimaster Cluster based on synchronous replication.
 - [mha4mysql-node](https://github.com/yoshinorim/mha4mysql-node) and [mha4mysql-manager](https://github.com/yoshinorim/mha4mysql-manager) (both unmaintained) - Master High Availability Manager and tools for MySQL.
 - [Orchestrator](https://github.com/ProxySQL/orchestrator) - MySQL replication topology management and High Availability solution.
-- [Percona Replication Manager](https://github.com/percona/replication-manager) - Asynchronous MySQL replication manager agent for Pacemaker. Supports file and GTID based replication, geo-distributed clusters using booth.
+- [Percona Replication Manager](https://github.com/percona/replication-manager) - Manages asynchronous GTID replication links between Percona XtraDB Cluster or MariaDB Galera clusters.
 - [replication-manager](https://github.com/signal18/replication-manager) - a high availability solution to manage MariaDB 10.x and MySQL & Percona Server 5.7 GTID replication topologies.
 
 ## MCP
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL works, but the repository it points to is a different tool from the one the entry describes. percona/replication-manager (not a fork) is a shell-script tool that manages asynchronous GTID replication links between Percona XtraDB Cluster or MariaDB Galera clusters. Its README says it works only with GTID-based replication and never mentions Pacemaker or booth. The Pacemaker agent the description refers to (PRM: Pacemaker, file and GTID agents, booth for geo-DR) is a separate repo, Percona-Lab/pacemaker-replication-agents (percona/percona-pacemaker-agents redirects there). That repo&#x27;s last commit was in 2017. Recommended: keep the URL and correct the description so it matches the repo actually linked.</p>

<p>https://raw.githubusercontent.com/percona/replication-manager/main/README.md — Titled &#x27;Replication manager for PXC and MariaDB&#x27;. Manages asynchronous replication between PXC or MariaDB clusters, uses Galera for quorum within a cluster, and states &#x27;This solution works only with GTID based replication&#x27;. No mention of Pacemaker or booth.</p>

<p>https://github.com/percona/replication-manager — Canonical nwo percona/replication-manager, not a fork. Files: replication_manager.sh, replication_manager5.sh, percona-replication-manager_builder.sh, debian/, rpm/. Latest commit is dated 2026-01-07.</p>

<p>https://github.com/percona/percona-pacemaker-agents — Redirects to Percona-Lab/pacemaker-replication-agents, described as a &#x27;Repository of the Percona Pacemaker resource agents&#x27;. README refers to PRM mailing lists. Agents include mysql_prm and mysql_prm_gtid.</p>

<p>https://raw.githubusercontent.com/Percona-Lab/pacemaker-replication-agents/master/doc/PRM-geo-DR-guide.rst — The geo-DR guide mentions booth 26 times. This matches the entry&#x27;s &#x27;geo-distributed clusters using booth&#x27; claim, so the current description belongs to this repo, not the one linked. Its latest commit is dated 2017-03-31.</p>

<p>Caveats: Did not run either tool.; The other possible fix, pointing the entry at Percona-Lab/pacemaker-replication-agents and keeping the old description, is also consistent with the evidence, but that repo has had no commits since 2017. The maintainer may prefer that option or opening an issue.</p>

</details>

<h3>MCP MariaDB Server — replace</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -170,7 +170,7 @@
 
 ## MCP
 
-- [MCP MariaDB Server](https://github.com/MariaDB/mcp) - the official MariaDB MCP server.
+- [MariaDB AI Plugins](https://github.com/mariadb-corporation/ai-plugins) - official MariaDB AI agent plugins, including the MariaDB Shell-based MCP server.
 - [MySQL MCP Server](https://github.com/askdba/mysql-mcp-server) - Advanced MCP server exposing MySQL via the Model Context Protocol
 - [TiDB MCP Server](https://pingcap.github.io/ai/integrations/tidb-mcp-server/) - MCP Server for TiDB.
 
```

<details>
<summary>Evidence and limitations</summary>

<p>The MariaDB/mcp README opens with an official deprecation notice: effective November 3, 2026, the repo is deprecated, and all MariaDB MCP Server development and releases move to mariadb-corporation/ai-plugins. That repo exists, is the network root (MariaDB/ai-plugins is a fork of it), is licensed GPL-2.0, and provides a MariaDB Shell-based MCP server plus agent skills. This is an officially documented successor, not a competitor.</p>

<p>https://raw.githubusercontent.com/MariaDB/mcp/main/README.md — &#x27;Deprecation Notice: MariaDB MCP Server is moving (Effective Nov 3, 2026)… this repository (mariadb/mcp) is officially deprecated… all development, updates, and releases for the MariaDB MCP Server will take place in… mariadb-corporation/ai-plugins&#x27;.</p>

<p>https://raw.githubusercontent.com/mariadb-corporation/ai-plugins/main/README.md — &#x27;MariaDB AI Plugins&#x27;: agent skills plus the native mariadb-shell MCP server, which provides a live connection to MariaDB for schema reads, queries and EXPLAIN. Licensed GPL-2.0.</p>

<p>https://github.com/mariadb-corporation/ai-plugins — Page metadata: nwo mariadb-corporation/ai-plugins, is_fork=false, network root itself. github.com/mariadb/ai-plugins is a fork whose parent is mariadb-corporation/ai-plugins.</p>

<p>Caveats: The successor is a different implementation (an MCP plugin for MariaDB Shell, bundled with agent skills), not a renamed Python server. The maintainer may want to confirm it still fits the MCP section.; The deprecation took effect only a week before this review. The new repo is young, and its adoption was not assessed.; The old MariaDB/mcp repo is not archived.</p>

</details>

## Uncertain findings

<h3>innodb-ruby — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>Description is accurate, but the README explicitly warns against critical production use and describes unstable/buggy investigative tooling. The catalog contribution rules require production/GA readiness outside Incubating. Hold this keep pending curator interpretation rather than automatically removing it.</p>

<p>https://api.github.com/repos/jeremycole/innodb_ruby — archived=false, pushed_at 2026-04-28, description &#x27;A parser for InnoDB file formats, in Ruby&#x27;.</p>

<p>https://raw.githubusercontent.com/jeremycole/innodb_ruby/main/README.md — Title &#x27;A parser for InnoDB file formats, in Ruby&#x27;. Says it is a learning, teaching, investigative and debugging tool, &#x27;not intended for critical production usage&#x27;.</p>

<p>https://raw.githubusercontent.com/jeremycole/innodb_ruby/main/LICENSE — Revised (3-clause) BSD license.</p>

<p>Blocking questions: Description is accurate, but the README explicitly warns against critical production use and describes unstable/buggy investigative tooling. The catalog contribution rules require production/GA readiness outside Incubating. Hold this keep pending curator interpretation rather than automatically removing it.</p>

<p>Caveats: The upstream README says the tool is not meant for critical production use. The maintainer may consider this against the list&#x27;s GA-quality guideline, but it does not make the description wrong.</p>

<p>Independent source check: Description is accurate, but the README explicitly warns against critical production use and describes unstable/buggy investigative tooling. The catalog contribution rules require production/GA readiness outside Incubating. Hold this keep pending curator interpretation rather than automatically removing it.</p>

<p>https://github.com/jeremycole/innodb_ruby/blob/main/README.md — Describes an InnoDB Ruby parser intended for learning, teaching and investigation, with production and stability warnings.</p>

<p>https://github.com/shlomi-noach/awesome-mysql/blob/master/CONTRIBUTING.md — Contribution rules require production/GA readiness, with an Incubating exception.</p>

</details>

<h3>MySQL Connector/Node.js — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>Identity and description are accurate: the README says it is &#x27;a MySQL 8 driver for Node.js, officially supported and maintained by Oracle&#x27; (X DevAPI), and the MySQL download page still lists GA 8.0.35. However, the npm package @mysql/xdevapi has had no release since 8.0.35 (2023-10-25), with none for MySQL 8.1/8.4/9.x. Whether Oracle still maintains it is unresolved; no official discontinuation notice was found.</p>

<p>https://raw.githubusercontent.com/mysql/mysql-connector-nodejs/trunk/README.md — &#x27;MySQL Connector/Node.js is a MySQL 8 driver for Node.js, officially supported and maintained by Oracle. It contains an implementation of the X DevAPI&#x27;.</p>

<p>https://registry.npmjs.org/@mysql/xdevapi — dist-tags latest 8.0.35; last publish 2023-10-25; latest version not marked deprecated.</p>

<p>https://dev.mysql.com/downloads/connector/nodejs/ — Download page still lists &#x27;General Availability (GA) Releases&#x27; with Connector/Node.js 8.0.35.</p>

<p>Blocking questions: Whether Oracle has discontinued or stopped maintaining Connector/Node.js after 8.0.35 is unconfirmed; no official end-of-life statement was found.</p>

<p>Caveats: X Protocol/X DevAPI only, not the classic protocol; the entry does not claim otherwise.</p>

</details>

<h3>Liquibase — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>Liquibase is active and still fits as a schema-change and source-control tool for databases. However, the repository&#x27;s root LICENSE.txt is now the Functional Source License 1.1 with an Apache-2.0 future license (FSL-1.1-ALv2, copyright 2025 Liquibase Inc.). FSL is source-available, not an OSI- or FSF-recognized free/open-source license. The contribution rules say &#x27;halfway open sourced&#x27; software will not be accepted and will be removed. That is a licensing-policy question for a removal issue, not a purpose or interface loss, so I mark this uncertain rather than remove.</p>

<p>https://raw.githubusercontent.com/liquibase/liquibase/main/LICENSE.txt — Header: &#x27;Functional Source License, Version 1.1, ALv2 Future License&#x27;. Abbreviation FSL-1.1-ALv2. &#x27;Copyright © 2025 Liquibase Inc.&#x27;</p>

<p>https://github.com/liquibase/liquibase — GitHub API: not archived, license NOASSERTION, pushed_at 2026-11-10. Description &#x27;Main Liquibase Source&#x27;.</p>

<p>Blocking questions: Whether FSL-1.1-ALv2 makes Liquibase ineligible under the list&#x27;s &#x27;free and open source / FSF listings&#x27; rule is a maintainer policy decision. It should be raised in a removal issue per the contribution rules.</p>

<p>Caveats: Earlier Liquibase releases (4.x line) were Apache-2.0. I did not verify whether that line is still maintained.; I did not verify the exact release in which the FSL change took effect.</p>

</details>

<h3>ILLA Cloud — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>Identity and description are supported. illacloud/illa-builder is reachable with no redirect, Apache-2.0 licensed, and its README says it connects to MySQL as a data source for low-code internal tools. What is unresolved is whether the project is still maintained, which the contribution rules require: the last tagged release is illa-builder@4.8.5 from August 2024, the last commit on the default beta branch is from May 2025, and the official site could not be reached. No official discontinuation notice was found, and inactivity alone does not justify removal.</p>

<p>https://raw.githubusercontent.com/illacloud/illa-builder/beta/README.md — &#x27;ILLA is a robust open source low-code platform for developers to build internal tools.&#x27; Step 3 reads &#x27;Connect to MySQL or REST API through our GUI data connectors.&#x27; Self-hosting via Docker/k8s is documented, and the license badge shows Apache 2.</p>

<p>https://github.com/illacloud/illa-builder/releases.atom — Most recent release entry is illa-builder@4.8.5, dated 2024-08-05.</p>

<p>https://github.com/illacloud/illa-builder/commits/beta.atom — Latest commit on the beta (default) branch is dated 2025-05-14.</p>

<p>Blocking questions: Unresolved: whether ILLA Builder or ILLA Cloud has been officially discontinued or is only dormant. If a maintainer wants to raise abandonment, it would need an issue under the contribution rules.</p>

<p>Caveats: https://www.illacloud.com returned a proxy 502 from this environment. That is an access failure, not evidence that the service has shut down.; The GitHub REST API was rate-limited, so the archived flag comes from the packet snapshot (archived=false).</p>

</details>

<h3>OmniDB: Web tool for database management — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>This is a bare-link entry. The repository is reachable at OmniDB/OmniDB with no redirect, and the repo description &#x27;Web tool for database management&#x27; matches the link text. However, the README still describes &#x27;OmniDB 3.0.3 Beta&#x27;, released 2020-12-17. Both the last release (3.0.3b) and the last commit are from December 2020, roughly six years ago. No official discontinuation notice could be read: omnidb.org was unreachable from this environment. Current MySQL support in the 3.x line was not confirmed beyond legacy test folders (tests.old/mysql).</p>

<p>https://raw.githubusercontent.com/OmniDB/OmniDB/master/README.md — Headed &#x27;OmniDB 3.0.3 Beta, Release Date: December 17, 2020&#x27;. Release notes focus on PostgreSQL 13 support. Points to https://omnidb.org and omnidb.readthedocs.io.</p>

<p>https://github.com/OmniDB/OmniDB/commits/master.atom — Latest commit is dated 2020-12-17.</p>

<p>https://github.com/OmniDB/OmniDB/releases.atom — Latest release is 3.0.3b, dated 2020-12-17.</p>

<p>Blocking questions: Unresolved: whether OmniDB has been officially discontinued, and whether the current 3.x release still supports MySQL. Removal would need an issue under the contribution rules plus affirmative evidence.</p>

<p>Caveats: https://omnidb.org returned a proxy 502 here. That is an access failure, not evidence the project is dead.; The archived flag comes from the packet snapshot (archived=false). The GitHub API was rate-limited.</p>

</details>

<h3>data-diff — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>Datafold has officially discontinued the open-source data-diff, and the repo is archived. The catalog entry already marks it &#x27;(archived)&#x27;. The pinned rules say code must not be abandoned/discontinued. However, the tool&#x27;s purpose and interface have not been withdrawn, and the existing &#x27;(archived)&#x27; annotation suggests the maintainer chose to keep archived entries. Whether the catalog keeps discontinued-but-useful tools is a policy question for the maintainer.</p>

<p>https://raw.githubusercontent.com/datafold/data-diff/master/README.md — &#x27;As of May 17, 2024, Datafold is no longer actively supporting or developing open source data-diff.&#x27; Links to a sunsetting blog post. Licensed MIT.</p>

<p>https://github.com/datafold/data-diff — Canonical datafold/data-diff, archived. Description: &#x27;Compare tables within or across databases&#x27;.</p>

<p>Blocking questions: Maintainer policy is unresolved: the &#x27;(archived)&#x27; annotation suggests keeping, while the rule against discontinued code suggests a removal issue.</p>

<p>Caveats: Did not research community forks. Datafold names no official successor.</p>

</details>

<h3>Database Systems Lecture Notes — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL now redirects http→https and returns HTTP 503, as does the parent /caubert/ page, so the current live content can&#x27;t be confirmed. The latest Wayback snapshot (2024-09-28) shows the expected page: &quot;CSCI 3410 - Database Systems Lecture Notes&quot; at Augusta University, with PDF, HTML and ODT downloads and source on RocketGit. It covers exercises, problems and hands-on install guides for MariaDB/MySQL. The description matched the resource then. An access failure alone doesn&#x27;t justify removal, and I found no official notice of a move or withdrawal.</p>

<p>https://spots.augusta.edu/caubert/db/ln/ — http://spots.augusta.edu/caubert/db/ln/ redirects to https and returns HTTP 503 (tested 2026-11-10). The parent https://spots.augusta.edu/caubert/ also returns 503.</p>

<p>https://web.archive.org/web/20240928101004/https://spots.augusta.edu/caubert/db/ln/ — Archived page: &quot;CSCI 3410 - Database Systems Lecture Notes&quot;. It contains exercises, exams, problems and selected solutions, plus a hands-on guide to install, configure and run MariaDB, MySQL and MongoDB. It links to CSCI_3410_lecture_notes.pdf/.html/.odt and RocketGit source. The CDX index shows 200 responses through 2024-09-28.</p>

<p>https://rocketgit.com/user/caubert/CSCI_3410 — HTTP 200. This is the source repository linked from the archived page. Its contents were not inspected in detail.</p>

<p>Blocking questions: Live content at the listed URL could not be read (HTTP 503), so it&#x27;s unknown whether the notes are still published there or have moved.; No official notice of a new canonical hosting location was found. The RocketGit repo is a source repository, and I didn&#x27;t confirm whether it publishes the rendered notes.</p>

<p>Caveats: The 503 may be a temporary or institutional outage. It isn&#x27;t evidence the resource was withdrawn.; The RocketGit source repo is reachable, but it is the source, not a published book. I did not verify that it is an officially endorsed replacement URL.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

## Unresolved keeps

These entries were not added to the baseline.

<h3>Wireshark — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The GitLab URL resolves (HTTP 200) to the canonical wireshark/wireshark project, which was active on 2026-11-10. The repo contains the dissector epan/dissectors/packet-mysql.c (&#x27;Routines for MySQL/MariaDB packet dissection&#x27;), which confirms that Wireshark decodes the MySQL protocol.</p>

<p>https://gitlab.com/api/v4/projects/wireshark%2Fwireshark — path_with_namespace wireshark/wireshark, web_url https://gitlab.com/wireshark/wireshark, last_activity_at 2026-11-10.</p>

<p>https://gitlab.com/wireshark/wireshark/-/raw/master/epan/dissectors/packet-mysql.c — Header: &#x27;packet-mysql.c — Routines for MySQL/MariaDB packet dissection&#x27;, covering MySQL 4.1+ and the MariaDB protocol.</p>

<p>Caveats: The unauthenticated GitLab API did not return the archived flag, but recent activity shows the project is live.</p>

</details>

<h3>go-tpc — keep</h3>

<p>Source or watched-source coverage changed since research.</p>

<details>
<summary>Evidence and limitations</summary>

<p>pingcap/go-tpc is canonical and Apache-2.0 licensed. Its README describes a Go toolbox for TPC workloads on TiDB, MySQL-compatible and PostgreSQL-compatible databases, which still covers TPC-C and TPC-H on MySQL. Extra workloads and PostgreSQL support are additions, not corrections. The two inline TPC links in the entry must be preserved.</p>

<p>https://raw.githubusercontent.com/pingcap/go-tpc/master/README.md — &#x27;A toolbox to benchmark workloads in TPC for TiDB and almost MySQL compatible databases, and PostgreSQL compatible database&#x27;.</p>

<p>https://api.github.com/repos/pingcap/go-tpc — archived=false, Apache-2.0, pushed_at 2026-01-13.</p>

<p>Caveats: I took TPC-C/TPC-H support from the README overview and the packet&#x27;s tpch/dbgen directory; I did not run the tool.; The entry has extra inline links (tpc.org) that go against the one-link guideline. They are kept as-is per the brief.</p>

</details>

<h3>Percona Xtrabackup — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The packet snapshot failed, so I checked directly. percona/percona-xtrabackup is reachable, not archived, has default branch trunk, and has recent release tags (latest percona-xtrabackup-9.7.2-2). Its README opens with &#x27;Percona XtraBackup is an open-source hot backup utility for MySQL - based servers that doesn&#x27;t lock your database during the backup&#x27;, which is identical to the entry&#x27;s description.</p>

<p>https://raw.githubusercontent.com/percona/percona-xtrabackup/trunk/README.md — &#x27;Percona XtraBackup is an open-source hot backup utility for MySQL - based servers that doesn&#x27;t lock your database during the backup.&#x27; Covers 8.0 and 2.4 lines.</p>

<p>https://github.com/percona/percona-xtrabackup — Page loads with defaultBranch &#x27;trunk&#x27; and no archived banner. git ls-remote shows branches trunk, 8.0 and 2.4, and tags up to percona-xtrabackup-9.7.2-2.</p>

<p>Caveats: The GitHub API was rate-limited for this repo, so licence and archived status come from the repo page and README rather than API metadata.; Legacy branches 2.4 and 8.0 exist. I did not determine their individual maintenance status from their existence alone.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>TPCC-MySQL — keep</h3>

<p>Source or watched-source coverage changed since research.</p>

<details>
<summary>Evidence and limitations</summary>

<p>Repository Percona-Lab/tpcc-mysql is archived (per snapshot), and the catalog line already marks it &#x27;(archived)&#x27;. The README still documents building and running a TPC-C-like benchmark against MySQL (tpcc_load, tpcc_start), so the description is accurate. No official discontinuation notice or documented successor was found. Archive status alone does not justify removal, but the maintainer may weigh it against the &#x27;not abandoned&#x27; rule.</p>

<p>https://raw.githubusercontent.com/Percona-Lab/tpcc-mysql/master/README.md — README documents building with mysql_config, loading data with tpcc_load (warehouses), and running tpcc_start against MySQL with New Order throughput and latency output. No successor or deprecation note.</p>

<p>https://raw.githubusercontent.com/Percona-Lab/tpcc-mysql/master/LICENSE — Returned 404; no LICENSE file at that path, so the licence was not verified.</p>

<p>Caveats: Archived and unmaintained, which is in tension with the &#x27;Code must not be abandoned&#x27; rule; a maintainer discussion question, not proven unsuitability.; Licence not verified (no LICENSE file at repo root; GitHub API rate-limited).</p>

</details>

<h3>MySQL C API — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The URL resolves (HTTP 200) to the official MySQL &#x27;Download C API (libmysqlclient)&#x27; page, which states &#x27;C API (libmysqlclient) is a client library for C development&#x27; and that it is included in MySQL 8.0 distributions. &#x27;Official C driver for MySQL&#x27; is supported. The packet snapshot failure was transient or tool-specific.</p>

<p>https://dev.mysql.com/downloads/c-api/ — Page title &#x27;MySQL :: Download C API (libmysqlclient)&#x27;; &#x27;C API (libmysqlclient) is a client library for C development&#x27;; &#x27;C API (libmysqlclient) is included in MySQL 8.0&#x27;; recommends Connector/C++ for X DevAPI.</p>

<p>Caveats: The page text references MySQL 8.0 and older; it may lag current 8.4/9.x releases, but libmysqlclient remains the official C client library.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>sys — keep</h3>

<p>Source unavailable at final recheck.</p>

<details>
<summary>Evidence and limitations</summary>

<p>mysql/mysql-sys is archived, and the entry already says so. Its README matches the description word for word. The sys schema itself ships with MySQL, and the linked 8.4 sys schema docs page loads. The entry is a deliberately annotated historical resource with a pointer to current docs.</p>

<p>https://raw.githubusercontent.com/mysql/mysql-sys/master/README.md — &#x27;A collection of views, functions and procedures to help MySQL administrators get insight in to MySQL Database usage.&#x27; Install files for 5.6 and 5.7.</p>

<p>https://dev.mysql.com/doc/refman/8.4/en/sys-schema.html — Returns HTTP 200.</p>

<p>https://github.com/mysql/mysql-sys — Canonical mysql/mysql-sys, archived. Description: &#x27;The MySQL sys schema&#x27;.</p>

<p>Caveats: The entry has a second link (the docs link), which the one-link rule discourages. That is pre-existing formatting and should be preserved.</p>

</details>

<h3>MySQL Server &amp; MySQL Cluster — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The packet&#x27;s snapshot fetch failed, but the repo loads. GitHub&#x27;s title describes it as MySQL Server and MySQL Cluster, and the README identifies it as Oracle&#x27;s MySQL release. The description is accurate.</p>

<p>https://github.com/mysql/mysql-server — HTTP 200. Title: &#x27;mysql/mysql-server: MySQL Server, the world&#x27;s most popular open source database, and MySQL Cluster, a real-time, open source transactional database.&#x27;</p>

<p>https://raw.githubusercontent.com/mysql/mysql-server/trunk/README — &#x27;This is a release of MySQL, an SQL database server… brought to you by the MySQL team at Oracle&#x27;, copyright 2000–2026.</p>

<p>Caveats: Did not enumerate the repo&#x27;s NDB/Cluster sources directly. That claim rests on GitHub&#x27;s repo title.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>MySQL Router — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The packet&#x27;s snapshot fetch failed, but the URL loads and redirects to the current MySQL Router 26.10 manual. The official docs say &#x27;MySQL Router is part of InnoDB Cluster and is lightweight middleware&#x27;, which matches the description.</p>

<p>https://dev.mysql.com/doc/mysql-router/en/ — Redirects to https://dev.mysql.com/doc/mysql-router/26.10/en/ (HTTP 200, title &#x27;MySQL :: MySQL Router 26.10&#x27;).</p>

<p>https://dev.mysql.com/doc/mysql-router/26.10/en/mysql-router-innodb-cluster.html — Contains &#x27;MySQL Router is part of InnoDB Cluster and is lightweight middleware&#x27;.</p>

<p>https://dev.mysql.com/doc/mysql-router/26.10/en/mysql-router-general.html — &#x27;MySQL Router is a building block for high availability (HA) solutions… routing connections to MySQL servers.&#x27;</p>

<p>Caveats: The entry links to documentation, which the guidelines discourage. Router source lives in mysql/mysql-server under router/. Changing the URL is optional and up to the maintainer.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>SQL-exercise — keep</h3>

<p>Source or watched-source coverage changed since research.</p>

<details>
<summary>Evidence and limitations</summary>

<p>XD-DENG/SQL-exercise resolves directly. The README says the schemas and questions come from the Wikibook SQL Exercises, with additional exercises by the author. Each exercise folder contains a schema figure (.png), a build-schema SQL file and a questions-and-solutions SQL file, exactly as the entry says. It&#x27;s free to access under CC BY-SA 3.0, which fits the e-books section rules.</p>

<p>https://raw.githubusercontent.com/XD-DENG/SQL-exercise/master/README.md — README: schemas and questions come from Wikibook &quot;SQL Exercises&quot; (exercises 1-8), with 9-10 added by the author. The structure shows SQL_exercise_*/ containing *_schema_figure.png, *_build_schema.sql and *_questions_and_solutions.sql. License: CC BY-SA 3.0.</p>

<p>Caveats: Did not verify that the embedded Wikibooks link is still reachable.</p>

</details>

The complete research records remain local. This inventory contains all recommendations and unresolved entries from the saved initial review.

[One-entry integration example](https://github.com/bromanko/awesome-mysql/blob/codex/catalog-inventory-preview/.um/catalog-inventory/checked-example.md). Saved research with real discussion-history and patch checks.
