# iLang Gospel design system

## The reading spread

The opening pairs the words of John 1:1 with an invitation to read the first essay. In the concordance, changing the passage changes its interpretation and reading link together. In an essay, the text occupies the left column. A source note starts level with the quotation it belongs to. The margin also holds the original publication details and a contents disclosure when enough section headings exist.

## Type, color and measure

- ET Book Roman sets English prose. Its display italic distinguishes quotations and subtitles. ET Book Bold preserves emphasis. The three self-hosted WOFF files and their licenses live in `assets/tufte/`.
- Chinese reference text uses local Songti SC, Noto Serif CJK SC and Source Han Serif SC fallbacks. Literal code uses the system monospace stack. The source-preserving Chinese code documents wrap within the page.
- Paper, ink and the reading accent are respectively `#fbf8ee`, `#26241f` and `#873b28` in the light theme. Their dark values are `#1c1b18`, `#f2ebd8` and `#efaa8e`. A restrained rule separates sections. Underlines, pressed state, numbers and focus outlines carry meaning independently of color.
- The outer measure stops at 76rem. An essay uses up to 42rem of prose, a fluid gutter and up to 16rem for notes. Below 50rem the margin becomes an inline disclosure. The homepage index becomes a single stack on narrow screens.

## Interaction and content

The System theme follows the reader’s device. Readers can choose Light or Dark in the masthead. Explicit choices are saved on the same origin. The site has no external font, script, image or stylesheet requests.

The static archive lists every essay in file order. Its visible columns identify the essay, the Scripture citation and the mechanism. Word search matches the complete text using a same-origin index. Without JavaScript, all essays and all three Scripture comparisons are present.

A clearly attributed biblical quotation may supply a numbered source. The enhanced reader moves the existing text into the margin. On narrow screens a button expands it in place using click, Enter or Space. Source citations remain in the original quotation when scripts are disabled. Publication records and links stay in the document. Article headings create the contents links and file order determines adjacent essays. Text and links keep their positions during reading, including with reduced motion enabled.

## Code and sources

The common foundation is in `assets/site.css`, `_includes/book-head.html` and `_includes/masthead.html`. Homepage and reader styles have their own stylesheets. Licenses, upstream revisions and the mapping to original font filenames are in [the third-party notice](assets/tufte/NOTICE.txt). Public pages use native GitHub Pages plugins and the existing site metadata. GitHub renders the repository README with its own presentation.
