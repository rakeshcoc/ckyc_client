import lxml.html
from lxml import etree
#xslt_doc = etree.parse("fieldss.xslt")
xslt_doc = etree.parse("xml_to_html/xslt_file/fieldss1.xslt")
xslt_transformer = etree.XSLT(xslt_doc)
source_doc = etree.parse("xml_to_html/xml_file/field.xml")
output_doc = xslt_transformer(source_doc)
output_doc.write("templates/onboard/choose_doc_2.html", pretty_print=True)
# file:///home/cps/Downloads/fieldss.xslt
