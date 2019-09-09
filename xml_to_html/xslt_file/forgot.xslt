<xsl:stylesheet version="1.0"
	xmlns:xsl = "http://www.w3.org/1999/XSL/Transform">

	<xsl:template match="/">
		<p>
			{% extends 'onboard/base.html' %}
			{% block body %}
			<div class="container">
				<h1>Please Fill required field</h1>
				<form action="" method ="post" name="myform" enctype="multipart/form-data">
					{% csrf_token %}
					<xsl:apply-templates/>
				</form>
			</div>
			{% endblock %}
		</p>
	</xsl:template>
	<xsl:template match="policy-name">
		<xsl:apply-templates select="field"/>
	    <div class="form-group">        
	    <div class="col-sm-offset-2 col-sm-10">
			<button type="submit" class="btn btn-success" value="submit">Submit</button>
		</div>
		</div>
	</xsl:template>
	<xsl:template match="field">
		<xsl:choose>
			<xsl:when test="datatype = 'select'">
				<xsl:variable name="name" select="name"/>
				<xsl:if test="meta = 'primary'">
					
				<div class="form-group">
					<label for="{$name}"><xsl:value-of select = "name"/></label>*:
				<select class="form-control" name = "{$name}" required="true">
						<xsl:for-each select="select/option">
							<xsl:variable name="option" select="."/>
	            			<option value="{$option}">
	               				<xsl:value-of select="."/>
	            			</option>
	            		</xsl:for-each>
	            </select>
				</div>
		        </xsl:if>
     		
			</xsl:when>
			<xsl:otherwise>
				<xsl:variable name="datatype" select="datatype"/>
				<xsl:variable name="name" select="name"/>
				<xsl:variable name="meta" select="meta"/>
				<xsl:variable name="pattern" select="pattern"/>
				<xsl:variable name="message" select ="message"/>
				<xsl:if test="meta = 'primary'">
					<label for="{$name}"><xsl:value-of select="name"/>*:</label>
					<div class="form-group">
						<input type="{$datatype}" name="{$name}" required="true" class="form-control" placeholder="Required" pattern="{$pattern}" title="{$message}"/>
					</div>
				</xsl:if>
			</xsl:otherwise>
		</xsl:choose>	
	</xsl:template>
</xsl:stylesheet>