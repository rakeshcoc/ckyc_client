<xsl:stylesheet version="1.0"
	xmlns:xsl = "http://www.w3.org/1999/XSL/Transform">

	<xsl:template match="/">
		<br>

					<xsl:apply-templates/>
	</br>
	</xsl:template>
	<xsl:template match="policy-name">
		<xsl:if test=".">
			function dependency()
			{
		<xsl:apply-templates select="field"/>
			}
		</xsl:if>
	</xsl:template>
	<xsl:template match="field">
				<xsl:variable name="datatype" select="datatype"/>
				<xsl:variable name="name" select="name"/>
				<xsl:variable name="meta" select="meta"/>
				<xsl:variable name="pattern" select="pattern"/>
				<xsl:variable name="message" select ="message"/>
				<xsl:if test="meta = 'O'">
					<xsl:if test="$datatype = 'text'">
					if(document.myform.<xsl:value-of select="name"/>.value != "")
					{
					<xsl:for-each select = "proof/attachments">
					<xsl:variable name="proofname" select="."/>
						if(document.myform["<xsl:value-of select="."/>"].value == "")
							{
							 alert("Please attach proof in optional field ");
							 document.myform["<xsl:value-of select="."/>"].focus();
							 return false;
							}
					</xsl:for-each>
					}
					</xsl:if>
					<xsl:if test="$datatype = 'select'">
					if(document.myform.<xsl:value-of select="name"/>.value != "optional")
					{
					<xsl:for-each select = "proof/attachments">
					<xsl:variable name="proofname" select="."/>
						if(document.myform["<xsl:value-of select="."/>"].value == "")
							{
							 alert("Please attach proof in optional field ");
							 document.myform["<xsl:value-of select="."/>"].focus();
							 return false;
							}
					</xsl:for-each>
					}
					</xsl:if>

				</xsl:if>
	</xsl:template>
</xsl:stylesheet>
