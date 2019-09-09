

<xsl:stylesheet version="1.0"
	xmlns:xsl = "http://www.w3.org/1999/XSL/Transform" xmlns:msxsl="urn:schemas-microsoft-com:xslt" 
	xmlns:user="http://mycompany.com/mynamespace">	

	
	

	<xsl:template match="/">
			<div class="container">
				<h1>select the documents to submit</h1>

				<form action="" method ="post" name="myform" enctype="multipart/form-data" >
						<button type="submit" onclick="myFunction()" class="btn btn-success" value="submit">Submit</button>
						<xsl:apply-templates/>
				</form>
			</div>
			<div id="content">
				
			</div>		
	</xsl:template>

	<xsl:template match="policy-name">
    	
      			<script type="text/javascript">
			    		<![CDATA[
			    			var globalArray = []
			    			function globalFunc(op){
			    				globalArray.push(op);
			    			}

			    			function myFunction(){
			    				for(var i=0; i!= globalArray.length;i++){
			    					addElement("content", "p", globalArray+i )
			    				}
			    			}

			    			function getSelectedOptions(sel) {
							  var opts = [],
							    opt;
							  var len = sel.options.length;
							  for (var i = 0; i != len; i++) {
							    opt = sel.options[i];

							    if (opt.selected) {
							      opts.push(opt.value);
							      //alert(opt.value);
							    }
							  }

							  console.log(opts);
							  globalFunc(opts)
							}

							function addRow () {
  document.querySelector('#content').insertAdjacentHTML(
    'afterbegin',
    `<div class="row">
      <input type="text" name="name" value="globalArray[0]" />
    </div>`      
  )
}
						]]>
				</script>
			
    	<xsl:for-each select="field">
   			<xsl:if test="@type = 'proof_required'">
      			<div id="doc" class="documents_div">

       				<xsl:value-of select="name"/>
    				*:
				<select class="documents" required="true" multiple="true" onChange="getSelectedOptions(this)">
						<xsl:for-each select="proof/attachments">
							<xsl:variable name="attachments" select="."/>
	            			<option value="{$attachments}">
	            				<xsl:if test="@selected='true'">
            						<xsl:attribute name="selected">selected</xsl:attribute>
          						</xsl:if>
	               				<xsl:value-of select="."/>

	            			</option>
	            		</xsl:for-each>
	            </select>

       		
  				</div>

      </xsl:if>
    </xsl:for-each>
    
   	
    </xsl:template>

	

	

</xsl:stylesheet>

