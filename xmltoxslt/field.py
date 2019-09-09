import lxml.html
from lxml import etree
#xslt_doc = etree.parse("fieldss.xslt")
xslt_doc = etree.parse("fieldss1.xslt")
xslt_transformer = etree.XSLT(xslt_doc)
source_doc = etree.parse("field.xml")
output_doc = xslt_transformer(source_doc)
output_doc.write("choose_doc_2.html", pretty_print=True)
# file:///home/cps/Downloads/fieldss.xslt