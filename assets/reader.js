(() => {
  const body = document.querySelector('.article-body');
  if (!body) return;

  // A terminal book/chapter/verse identifies a source. Dashes inside prose and
  // protocol quotations are common in these essays and must stay in the text.
  const book = '(?:Genesis|Exodus|Leviticus|Numbers|Deuteronomy|Joshua|Judges|Ruth|[12] Samuel|[12] Kings|[12] Chronicles|Ezra|Nehemiah|Esther|Job|Psalms?|Proverbs|Ecclesiastes|Song of (?:Solomon|Songs)|Isaiah|Jeremiah|Lamentations|Ezekiel|Daniel|Hosea|Joel|Amos|Obadiah|Jonah|Micah|Nahum|Habakkuk|Zephaniah|Haggai|Zechariah|Malachi|Matthew|Mark|Luke|John|Acts|Romans|[12] Corinthians|Galatians|Ephesians|Philippians|Colossians|[12] Thessalonians|[12] Timothy|Titus|Philemon|Hebrews|James|[12] Peter|[123] John|Jude|Revelation)';
  const verses = book + String.raw`\s+\d+:\d+(?:(?:[-–—,;]\s*)\d+(?::\d+)?)*`;
  const source = new RegExp(String.raw`\s*[—–]\s*(` + verses + String.raw`(?:\s+\([A-Z0-9 -]+\))?)\s*$`);
  const standalone = new RegExp(String.raw`^(?:“[^”]+”|"[^"]+")\s*\(` + verses + String.raw`(?:,\s*[A-Z0-9 -]+)?\)\.?$`, 's');

  // Use DOM ranges so italics and links survive even if a citation spans nodes.
  function textPoint(element, offset) {
    const walker = document.createTreeWalker(element, NodeFilter.SHOW_TEXT);
    let node;
    while ((node = walker.nextNode())) {
      if (offset < node.length) return [node, offset];
      offset -= node.length;
    }
    return [element, element.childNodes.length];
  }

  function addSource(quote, paragraph, match, number) {
    const range = document.createRange();
    range.selectNodeContents(paragraph);
    const referenceStart = match.index + match[0].indexOf(match[1]);
    range.setStart(...textPoint(paragraph, referenceStart));
    const reference = range.extractContents();
    range.selectNodeContents(paragraph);
    range.setStart(...textPoint(paragraph, match.index));
    range.deleteContents();

    const container = document.createElement('div');
    container.className = 'reader-citation';
    quote.before(container);
    container.append(quote);

    const note = document.createElement('div');
    note.id = 'reader-source-' + number;
    while (document.getElementById(note.id)) note.id += '-ref';
    note.className = 'reader-source';
    note.setAttribute('role', 'note');
    note.setAttribute('aria-label', 'Scripture source ' + number);
    const label = document.createElement('sup');
    label.textContent = number;
    label.setAttribute('aria-hidden', 'true');
    const value = document.createElement('span');
    value.append(reference);
    note.append(label, value);
    container.append(note);

    const mark = document.createElement('sup');
    mark.className = 'reader-mark';
    mark.textContent = number;
    mark.setAttribute('aria-hidden', 'true');
    const button = document.createElement('button');
    button.className = 'reader-note-toggle';
    button.type = 'button';
    button.textContent = number;
    button.setAttribute('aria-label', 'Scripture source ' + number);
    button.setAttribute('aria-controls', note.id);
    button.setAttribute('aria-expanded', 'false');
    button.addEventListener('click', () => {
      button.setAttribute('aria-expanded', String(note.classList.toggle('is-open')));
    });
    const anchor = paragraph.textContent.trim() ? paragraph : paragraph.previousElementSibling || paragraph;
    anchor.append(mark, button);
    if (anchor !== paragraph) paragraph.remove();
  }

  let notes = 0;
  let epigraph;
  for (const block of Array.from(body.children)) {
    if (block.matches('p') && !epigraph && standalone.test(block.textContent.trim())) epigraph = block;
    if (!block.matches('blockquote')) continue;
    const paragraph = block.lastElementChild;
    if (!paragraph || !paragraph.matches('p')) continue;
    const match = source.exec(paragraph.textContent);
    if (!match) continue;
    if (!epigraph) epigraph = block;
    addSource(block, paragraph, match, ++notes);
  }
  if (epigraph) epigraph.classList.add('reader-epigraph');
})();
