import os
from docutils import nodes
from sphinx.locale import admonitionlabels
from sphinx.writers.html import HTMLTranslator as SphinxHTMLTranslator

class HTMLTranslator(SphinxHTMLTranslator):
    """
    Handle translating to bootstrap structure.
    """
    def visit_table(self, node, name=''):
        """
        Override docutils default table formatter to not include a border
        and to use Bootstrap CSS
        See: http://sourceforge.net/p/docutils/code/HEAD/tree/trunk/docutils/docutils/writers/html4css1/__init__.py#l1550
        """
        self.context.append(self.compact_p)
        self.compact_p = True
        classes = ' '.join(['table', 'table-bordered',
            self.settings.table_style]).strip()
        self.body.append(
            self.starttag(node, 'table', CLASS=classes))

    def depart_table(self, node):
        """
        This needs overridin' too
        """
        self.compact_p = self.context.pop()
        self.body.append('</table>\n')

def setup(sphinx):
    sphinx.config.html_translator_class = 'guzzle.HTMLTranslator'
