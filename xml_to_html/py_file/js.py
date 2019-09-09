import lxml.html
from lxml import etree
xslt_doc = etree.parse("xml_to_html/xslt_file/js.xslt")
xslt_transformer = etree.XSLT(xslt_doc)
source_doc = etree.parse("xml_to_html/xml_file/field.xml")
output_doc = xslt_transformer(source_doc)
output_doc.write("templates/onboard/form.js", pretty_print=True)