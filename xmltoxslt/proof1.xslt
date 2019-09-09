<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"	xmlns:xsl = "http://www.w3.org/1999/XSL/Transform">	

	<xsl:template match="/">
		<p>
		
			<div class="container">
				<h1>select the documents to submit</h1>
				<form action="" method ="post" name="myform" enctype="multipart/form-data" >
					<xsl:apply-templates/>
				<xsl:template match="policy-name">
    
    	<xsl:for-each select="field">
   			<xsl:if test="@type = 'proof_required'">
      			<div class="documents">

       				<xsl:value-of select="name"/>
    				*:
				<select id="sample" required="true" multiple="true" >
						<xsl:for-each select="proof/attachments">
							<xsl:variable name="attachments" select="."/>
	            			<option value="{$attachments}">
	            				<xsl:if test="@selected='yes'">
            						<xsl:attribute name="selected">selected</xsl:attribute>
          						</xsl:if>
	               				<xsl:value-of select="."/>
	            			</option>
	            		</xsl:for-each>
	            </select>
       		
  				</div>

      </xsl:if>
    </xsl:for-each>
   
    <button type="submit" onclick="myFunction()" class="btn btn-success" value="submit">Next</button> 
   
   <script>
   <![CDATA[
            
            function myFunction(){
            	var element = document.getElementById("sample");
            	 var text = element.options[element.selectedIndex].text;
    			console.log(text)
            }
          ]]>
          </script>

    </xsl:template>
				</form>
			</div>
		</p>
	</xsl:template>
	

	
    
        

								
</xsl:stylesheet>