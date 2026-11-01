# Publishing, automatic synchronization, and SEO

The public site is https://carbonsoul.github.io/iLang-Gospel/. GitHub Pages publishes the root of main using its built-in Jekyll workflow.

## Adding or editing an essay

Add a Markdown file under articles/ using the existing numbered filename pattern and a single `# Title` heading. No YAML front matter or hand-maintained catalog entry is required. During the next Pages build:

- The homepage scans all article pages, sorts by filename, and updates the count, links, descriptions, and searchable content.
- Each article gets a complete HTML reading page at `/iLang-Gospel/articles/<filename>.html`, with previous/next navigation.
- The sitemap and RSS feed include the article automatically.
- The “Synchronize article catalog” workflow refreshes only the marked article table in README.md and commits it back to main when needed. No personal access token is required; it uses the workflow's contents-write permission.

Edits and deletions are reflected by the generated catalogs and outputs. Fixed editorial selections in the homepage's Scripture comparison and README's “Start reading” section are authored recommendations; if those particular source essays are removed or renamed, update those editorial links too. The build validator detects missing site targets.

The site does not depend on the README synchronization commit: its catalog is derived directly from the article files in the triggering revision. Synchronization is idempotent and commits only actual catalog changes; an already synchronized catalog exits without another commit. Pages may rebuild the resulting main revision, but the article inventory is the same. Concurrent human pushes are preserved by regenerating from the newest main in the disposable runner checkout; no force push is used. Repository branch rules can block bot writes, in which case the workflow reports a failure rather than bypassing protection.

## Search metadata

Every reading page has a distinct title, description, canonical URL, Open Graph fields, Twitter summary card, Article JSON-LD, and breadcrumb structured data. Descriptions are derived from the first substantial prose paragraph. An optional front-matter `description` overrides the generated summary. Author attribution comes from the existing site configuration. Publication dates, ratings, and review counts are not invented.

The homepage contains server-rendered article links and summaries; essential content is available without JavaScript. Search is a local enhancement. The site uses one shared stylesheet and no external font or JavaScript dependency. A 1200×630 PNG provides a real social sharing image. Chinese reference documents declare their language and retain their machine-readable source formatting.

Canonical URLs point to this site's HTTPS address. Original raw Markdown copies are removed from the published output to avoid redundant crawl paths; the source remains on GitHub. Internal reference pages share the reading layout. Editorial work records, test helpers, and Python server source are excluded from the public site.

- Sitemap: https://carbonsoul.github.io/iLang-Gospel/sitemap.xml
- RSS: https://carbonsoul.github.io/iLang-Gospel/feed.xml
- Robots: https://carbonsoul.github.io/iLang-Gospel/robots.txt
- Unknown paths use a custom 404 page with noindex and a recovery link.

## Validation

The local build uses the official GitHub Pages image pinned by digest in scripts/build_site.sh. With the prepared environment, run `bash scripts/build_site.sh`, then `python3 scripts/check_site.py _site`. The validator checks the article inventory, one H1 per page, unique article titles/descriptions, canonical URLs, JSON-LD, internal targets and anchors, sitemap/feed inventory, absence of raw Markdown duplicates, and the social image. Unit tests exercise README synchronization on additions, edits, deletion, special characters, sorting, idempotence, and missing markers.

The isolated extra-article check proves a new plain Markdown file appears in the homepage, article output, sitemap, and RSS without editing their templates. The fixture is never published. Browser validation checks desktop/mobile reading, search, navigation, and no-JavaScript output.

## Search engine account boundary

These changes provide crawlable pages and technical SEO; search engines decide when to crawl, index, display rich results, and rank them. Google Search Console and Bing Webmaster Tools property verification, manual sitemap submissions, and real-user search analytics have not been connected because no account authorization was supplied. No fake verification token or indexing claim is included. The public sitemap is discoverable through robots.txt without those accounts.
