//Checks the latex input area and updates the rendered text area
$('.preview-fields textarea').on('keyup', function(e) {
    const previewArea = ($(e.currentTarget).parent().parent().next().find('.latex-preview').get(0));
    convertLatex(e.currentTarget, previewArea)
});

function convertLatex(inputEl, outputEl) {
    var input = inputEl.value.trim();
    output = outputEl;
    output.innerHTML = input;
    MathJax.typeset();
}

    // text = text.replace(/\B\$\$/m, `<span class="latex-wrap">$$$`);
    // text = text.replace(/\b\$\$/gm, `$$$</span>`);
    // // Headers
    // text = markdown(text, '^#{4}(.*)', 'h4');
    // text = markdown(text, '^#{3}(.*)', 'h3');
    // text = markdown(text, '^#{2}(.*)', 'h2');
    // text = markdown(text, '^#(.*)', 'h1');
    // // Emphasis and Bolding
    // text = markdown(text, '\\*{2}(.*)\\*{2}', 'strong');
    // text = markdown(text, '\\*(.*)\\*', 'em');
    // // Code blocks
    // text = markdown(text, '\\`{3}(.*)\\`{3}', 'pre');
    // text = markdown(text, '\\`(.*)\\`', 'code');
    // // Lists
    // text = markdown(text, '((\\d\\.\\s.*\\n)+)', 'ol');
    // text = markdown(text, '((\\*\\.\\s.*\\n)+)', 'ul');
    // text = markdown(text, '((-\\.\\s.*\\n)+)', 'ul');
    // text = markdown(text, '\\d\\.\\s(.*\\n)', 'li');
    // text = markdown(text, '\\*\\s(.*\\n)', 'li');
    // text = markdown(text, '-\\s(.*\\n)', 'li');
    // // Line Breaks
    // text = text.replace(/\n/gm, `<br>`);
    // text = text.replace(/\r/gm, `<br>`);

    // renderArea.innerHTML = text;
// }

/* Function: Markdown
    * Arguments: text - the text to be modified
    *					  ex	 - the regex to match
    *					  tag  - the HTML tag to use
    * Returns: The text with anything inside the Regex matches
    * 				wrapped by the specified HTML tags
    * TODO: Create a JSON object with all the markdown syntax and tags
    */

// function markdown(text, ex, tag) {
//     var regex = new RegExp(ex, 'gm');
//     var subst = '<' + tag + '>$1</' + tag + '>';
//     return text.replace(regex, subst);
// }