<xsl:stylesheet version="1.0"
	xmlns:xsl = "http://www.w3.org/1999/XSL/Transform">

	<xsl:template match="/">
		<p>
			{% extends 'onboard/base.html' %}
			{% block body %}
			<div class="container">
				<h1>Please Fill detail form</h1>
				<form action="" method ="post" name="myform" enctype="multipart/form-data" onsubmit="return(dependency());">
					{% csrf_token %}
					<xsl:apply-templates/>
				</form>
			</div>
			{% endblock %}
		</p>
	</xsl:template>
	<xsl:template match="policy-name">
		<h3>Policy Name is <xsl:value-of select="@title"/></h3>
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
				<div class="form-group">
					<label for="{$name}"><xsl:value-of select = "name"/></label>
				<xsl:if test="meta = 'R,K'">
					*:
				<select class="form-control" name = "{$name}" required="true">
						<xsl:for-each select="select/option">
							<xsl:variable name="option" select="."/>
	            			<option value="{$option}">
	               				<xsl:value-of select="."/>
	            			</option>
	            		</xsl:for-each>
	            </select>
  	            		<xsl:for-each select = "proof/attachments">
						<xsl:variable name="proofname" select="."/>
						<div class="form-group">
						<label><xsl:value-of select = "."/>*:</label>
							<input type="file" name="{$proofname}" class="form-control" accept="image/*" required="true"/>
						</div>
						</xsl:for-each>

		        </xsl:if>
    			<xsl:if test="meta = 'R'">
    				*:
				<select class="form-control" name = "{$name}" required="true">
						<xsl:for-each select="select/option">
							<xsl:variable name="option" select="."/>
	            			<option value="{$option}">
	               				<xsl:value-of select="."/>
	            			</option>
	            		</xsl:for-each>
	            </select>
    	            	<xsl:for-each select = "proof/attachments">
						<xsl:variable name="proofname" select="."/>
						<div class="form-group">
						<label><xsl:value-of select = "."/>*:</label>
							<input type="file" name="{$proofname}" class="form-control" accept="image/*" required="true"/>
						</div>
						</xsl:for-each>

		        </xsl:if>
   				<xsl:if test="meta = 'O'">
   					:
				<select class="form-control" name = "{$name}">
						<option value="optional">optional</option>
						<xsl:for-each select="select/option">
							<xsl:variable name="option" select="."/>
	            			<option value="{$option}">
	               				<xsl:value-of select="."/>
	            			</option>
	            		</xsl:for-each>
	            </select>
   	            		<xsl:for-each select = "proof/attachments">
						<xsl:variable name="proofname" select="."/>
						<div class="form-group">
						<label><xsl:value-of select = "."/>:</label>
							<input type="file" name="{$proofname}" class="form-control" accept="image/*"/>
						</div>
						</xsl:for-each>

		        </xsl:if>

		        	</div>
           		
			</xsl:when>
			<xsl:otherwise>
				<xsl:variable name="datatype" select="datatype"/>
				<xsl:variable name="name" select="name"/>
				<xsl:variable name="meta" select="meta"/>
				<xsl:variable name="pattern" select="pattern"/>
				<xsl:variable name="message" select ="message"/>
				<xsl:if test="meta = 'R,K'">
					<label for="{$name}"><xsl:value-of select="name"/>*:</label>
					<div class="form-group">
						<input type="{$datatype}" name="{$name}" required="true" class="form-control" placeholder="Required" pattern="{$pattern}" title="{$message}"/>
					</div>
					<xsl:for-each select = "proof/attachments">
					<div class="form-group">
					<xsl:variable name="proofname" select="."/>
					<label><xsl:value-of select="."/>*:</label>
						<input type="file" name="{$proofname}" accept="image/*" required="true" pattern="{$pattern}" title="{$message}"/>
					</div>
				</xsl:for-each>

				</xsl:if>
				<xsl:if test="meta = 'R'">
					<label for="{$name}"><xsl:value-of select="name"/>*:</label>
					<div class="form-group">
						<input type="{$datatype}" name="{$name}" required="true" class="form-control" placeholder="Required" pattern="{$pattern}" title="{$message}"/>
					</div>
					<xsl:for-each select = "proof/attachments">
					<div class="form-group">
					<xsl:variable name="proofname" select="."/>
					<label><xsl:value-of select="."/>*:</label>
						<input type="file" name="{$proofname}" accept="image/*" required="true"/>
					</div>
				</xsl:for-each>

				</xsl:if>
				<xsl:if test="meta = 'O'">
					<label for="{$name}"><xsl:value-of select="name"/>:</label>
					<div class="form-group">
						<input type="{$datatype}" name="{$name}" class="form-control" placeholder="Optional" pattern="{$pattern}" title="{$message}"/>
					</div>
					<xsl:for-each select = "proof/attachments">
					<div class="form-group">
					<xsl:variable name="proofname" select="."/>
					<label><xsl:value-of select="."/>:</label>
						<input type="file" name="{$proofname}" accept="image/*"/>
					</div>
				</xsl:for-each>

				</xsl:if>
			</xsl:otherwise>
		</xsl:choose>	
	</xsl:template>
</xsl:stylesheet>