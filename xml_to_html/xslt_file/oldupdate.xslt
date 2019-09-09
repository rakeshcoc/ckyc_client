<xsl:stylesheet version="1.0"
	xmlns:xsl = "http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
		<p>
			{% extends 'onboard/base.html' %}
			{% block body %}
			<div class="container">
				<h1>Please Fill Fields Which You Want to Update</h1>
				<form action="" method ="post" name="myform" enctype="multipart/form-data" onsubmit="return(dependency());">
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
		<xsl:if test ="meta = 'R'">
			<xsl:choose>
			<xsl:when test="datatype = 'select'">
				<xsl:variable name="name" select="name"/>
				<div class="form-group">
					<label for="{$name}"><xsl:value-of select = "name"/>:</label>
				<select class="form-control" name = "{$name}">
						<option value="optional">optional</option>
						<xsl:for-each select="select/option">
							<xsl:variable name="option" select="."/>
	            			<option value="{$option}">
	               				<xsl:value-of select="."/>
	            			</option>
	            		</xsl:for-each>
	            </select>
	        	</div>
	            		<xsl:for-each select = "proof/attachments">
						<xsl:variable name="proofname" select="."/>
						<div class="form-group">
						<label><xsl:value-of select = "."/>:</label>
							<input type="file" name="{$proofname}"  accept="image/*"/>
						</div>
						</xsl:for-each>
			</xsl:when>
				<xsl:otherwise>
					<xsl:variable name="datatype" select="datatype"/>
					<xsl:variable name="name" select="name"/>
					<xsl:variable name="pattern" select="pattern"/>
					<xsl:variable name="message" select ="message"/>
					<label for="{$name}"><xsl:value-of select="name"/>:</label>
					<div class="form-group">
						<input type="{$datatype}" name="{$name}" class="form-control" pattern="{$pattern}" title="{$message}"/>
					</div>
            		<xsl:for-each select = "proof/attachments">
						<xsl:variable name="proofname" select="."/>
						<p><label><xsl:value-of select="."/></label>
							<input type="file" name="{$proofname}" accept="image/*"/>
						</p>
					</xsl:for-each>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:if>
		<xsl:if test ="meta = 'O'">
			<xsl:choose>
			<xsl:when test="datatype = 'select'">
				<xsl:variable name="name" select="name"/>
				<div class="form-group">
					<label for="{$name}"><xsl:value-of select = "name"/>:</label>
				<select class="form-control" name = "{$name}">
						<option value="optional">optional</option>
						<xsl:for-each select="select/option">
							<xsl:variable name="option" select="."/>
	            			<option value="{$option}">
	               				<xsl:value-of select="."/>
	            			</option>
	            		</xsl:for-each>
	            </select>
	        	</div>
	            		<xsl:for-each select = "proof/attachments">
						<xsl:variable name="proofname" select="."/>
						<div class="form-group">
						<label><xsl:value-of select = "."/>:</label>
							<input type="file" name="{$proofname}"  accept="image/*"/>
						</div>
						</xsl:for-each>
           		
			</xsl:when>
				<xsl:otherwise>
					<xsl:variable name="datatype" select="datatype"/>
					<xsl:variable name="name" select="name"/>
					<xsl:variable name="pattern" select="pattern"/>
					<xsl:variable name="message" select ="message"/>
					<label for="{$name}"><xsl:value-of select="name"/>:</label>
					<div class="form-group">
						<input type="{$datatype}" name="{$name}" class="form-control"  pattern="{$pattern}" title="{$message}"/>
					</div>
            		<xsl:for-each select = "proof/attachments">
						<xsl:variable name="proofname" select="."/>
						<p><label><xsl:value-of select="."/></label>
							<input type="file" name="{$proofname}" accept="image/*"/>
						</p>
					</xsl:for-each>
				</xsl:otherwise>
			</xsl:choose>

		</xsl:if>

	</xsl:template>
</xsl:stylesheet>