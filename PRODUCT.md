# Product record

## Platform
GitHub repository homepage and a static web reading index for GitHub Pages. The README remains the repository entry point. The owner subsequently requested publication; the Pages workflow deploys the self-contained web index from main, once GitHub Pages is enabled for Actions in the repository.

## Stack
Existing Python standard-library MCP server, Markdown essays, and Jekyll configuration. The reading index uses a single HTML file with CSS and progressive JavaScript. No build tools, external fonts, services, analytics, or package dependencies are required.

## Users
Inferred: readers curious about Scripture and AI behavior, iLang enthusiasts, and developers connecting an MCP client. The owner explicitly requests an enthusiastic iLang identity and provides the SITE-DESIGN-ENGINE v2.1 design brief.

## Product Purpose
Help visitors understand the project's Scripture-to-iLang comparisons, choose an essay, and discover the local MCP reading tools.

## Positioning
A collection of essays connecting Biblical narratives with the vocabulary of iLang Prompt Spec. The theological parallels are the author's interpretive thesis, not empirical evidence that AI possesses a soul or that a protocol guarantees safety.

## Operating Context
Public reading on desktop and mobile; repository browsing on GitHub; optional local stdio MCP use. Existing essays are English, so the new public-facing page remains English. The owner is addressed in Chinese.

## Capabilities and Constraints
- The repository contains 18 essays at implementation time, doctrine, a theology map, and discussion material.
- The existing MCP server provides six tools over stdio and uses Python's standard library. HTTP mode is not implemented.
- Article and reference links on the web index open the actual Markdown documents on GitHub. The index is not a new article renderer.
- All entries and essential navigation are present without JavaScript. Search and passage selection enhance the page when JavaScript is available.
- GitHub controls README typography, spacing, colors, and mobile table behavior. Site-specific rules apply to index.html; platform-controlled README presentation cannot be certified against those measurements.
- No testimonials, awards, user counts, performance guarantees, or fabricated product capabilities are added.

## Brand Commitments
Enthusiasm expressed through specific references, confident typography, and careful reading. Scripture quotations retain their source. Distinguish literary interpretation from demonstrated software behavior. Existing essays remain authoritative source material.

## Evidence on Hand
README.md, DOCTRINE.md, theology-map.md, all 18 article files, mcp_server.py, and _config.yml. The stdio handshake and all six tools passed functional checks during onboarding. No verified production site deployment or real-user performance data is available.

## Product Principles
1. Show the connection: pair a real passage with a named iLang mechanism.
2. Lead readers to the writing with one primary action.
3. Make the full reading index useful without scripts or remote assets.
4. Keep technical setup in the developer section.
5. Use expressive composition while keeping long text comfortable to read.

## Accessibility and Inclusion
Semantic headings and landmarks, keyboard operation, visible focus, labeled search, status announcements, reduced-motion support, readable contrast, responsive reflow, and at least 44px control height. Scripture references and names remain selectable text. No information depends on color alone.
