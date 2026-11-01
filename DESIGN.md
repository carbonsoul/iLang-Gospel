---
system: Gospel reading index
source: index.html
fonts:
  reading: "Georgia, Times New Roman, serif"
  literal_code: "ui-monospace, monospace"
colors:
  primary: "#203f57"
  secondary: "#f3ce78"
  tertiary: "#d7e7f2"
  neutral_light: ["#f7f9fa", "#233e52", "#506373", "#bdcbd5", "#ffffff"]
  on_primary: ["#f1f5f8", "#c8dae7"]
  focus_light: "#935000"
  neutral_dark: ["#152a39", "#e6eef4", "#b9ccd9", "#627c8f", "#1b3548", "#2e526c"]
type_rem:
  label: 0.875
  body: 1
  lead: 1.25
  title: 1.5625
  headline: "clamp(2rem, 4vw, 3.125rem)"
  display: "clamp(2.8rem, 6.1vw, 5.5rem)"
spacing_rem: [0.5, 0.75, 1, 1.5, 2, 3, 4.5, 6]
radius_px: [0]
motion: "350ms cubic-bezier(.16, 1, .3, 1)"
---

# Gospel design system

## Creative North Star
Authored: a contemporary concordance. Blue cloth, cool white reading space, substantial roman type, and the act of following a source into an interpretation. The first view offers the first essay. The characteristic interaction changes a Scripture quotation and its iLang explanation together.

## Color
Primary blue owns the opening and reference sections. Secondary gold identifies the primary action and focus on blue. Tertiary pale blue marks code and text selection. Neutral tokens distinguish body text, secondary text, boundaries, and fields. Colors are declared in :root; the dark preference supplies explicit surface and text values, rather than inverting the page. Content does not depend on color alone.

## Typography
One reading family, Georgia with Times New Roman and generic serif fallback. Code uses the system monospace only for actual commands and tool names. Display and headline sizes are fluid; title, lead, body, and label use the frontmatter scale. Normal text line-height is 1.6; headings and large quotations use 1.3. The only weights are normal and bold. Tracking is -.035em on display and -.025em on headlines. Prose is limited to 65ch, with shorter measures in paired columns. Headings and short explanatory paragraphs use balanced wrapping to avoid stranded final words; other paragraphs use pretty wrapping where supported.

## Space and Shape
The spacing scale is defined by --s1 through --s8. Sections have 6rem breathing room, reduced to 4.5rem on phones. Related items use .5–1.5rem gaps. Square forms and flat lists replace cards; radius is 0. No shadow or depth system is needed. The page width is capped at 74rem. Side margins are 3rem wide, 1.5rem medium, and 1.25rem narrow. A .2rem optical offset aligns the article mechanism with the title baseline. Focus uses a 3px outline with a 5px offset.

## Components
Components are semantic HTML and shared CSS, not a framework dependency. Repeated essays use one .essay pattern and common search behavior.

| Component | Background / text | Typography | Radius | Padding / size |
| --- | --- | --- | --- | --- |
| Primary reading link | secondary / primary | body, bold | 0 | .75rem 1.5rem, min-height 48px |
| Passage button | paper / ink; selected primary / on-primary | body | 0 | .75rem 1.5rem, min-height 46px |
| Essay row | paper / ink, muted metadata | lead title, body source, label mechanism | 0 | 1.5rem block, 1rem inline; linked title min-height 44px |
| Search field | field / ink | body | 0 | .75rem 1rem, min-height 48px |
| Code sample | tertiary / ink | literal code, label | 0 | 1.5rem |
| Empty-state recovery | field / ink | body | 0 | .5rem 1.5rem, min-height 44px |

## Interaction and Accessibility
Search uses actual article text and source metadata, normalizes Unicode, and matches all entered words. Result counts are announced. Empty results offer a clear action that restores all essays and returns focus to search. The three passage buttons expose pressed state and work with standard keyboard activation. A skip link, heading order, landmarks, and visible focus support keyboard navigation. Native details discloses the optional six-tool list. The page has no network-loaded data, loading simulator, modal, or submit action, so corresponding loading/error/disabled flows are inapplicable. External documents remain clearly identified as GitHub links.

## Responsive Layout and Motion
Wide layouts pair related content; at 640px they become a single reading column. At 900px the archive changes from three columns to two, then to one on phones. Text wraps inside shrinking containers. The only authored animation is an 8px passage-change translation over 350ms; content stays visible throughout. Reduced motion removes it entirely. There are no background loops, hover-only content, or hidden entrance states.

## Implementation and Verification
index.html holds all styling and behavior. No external fonts, images, build tools, or client dependencies are required. Existing Markdown remains the source of truth; adding an essay requires adding its static row to the page and README. The initial 18 rows were derived from the existing README article catalog. Verification evidence and rule dispositions are recorded in DESIGN-REVIEW.md. GitHub's own README styling remains a documented platform limitation; these CSS tokens apply to the authored webpage.
