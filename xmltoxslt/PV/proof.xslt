

<xsl:stylesheet version="1.0"
	xmlns:xsl = "http://www.w3.org/1999/XSL/Transform" xmlns:msxsl="urn:schemas-microsoft-com:xslt" 
	xmlns:user="http://mycompany.com/mynamespace">	

	
	

	<xsl:template match="/">
		   
		<p>
		
			<div class="container">
				<h1>select the documents to submit</h1>
				<form action="" method ="post" name="myform" enctype="multipart/form-data" >
					<xsl:apply-templates/>
				</form>
			</div>
		</p>
	</xsl:template>
	

	<xsl:template match="policy-name">
    	<script language="JavaScript">
    		<![CDATA[
            //function myFunction () {
				//var e = document.getElementByClassName('').value;
				//var e = document.getElementByClassName("[id^=sample]");
			//	var e = document.querySelector('[id^="sample+"]').id;
			//	alert(e);
			//}

			function myFunction(){
				var postedOnes = getElementsByIdStartsWith("documents", "div", "sample-");
			}

			function getElementsByIdStartsWith(container, selectorTag, prefix) {
    var items = [];
    var myPosts = document.getElementById(container).getElementsByTagName(selectorTag);
    for (var i = 0; i != myPosts.length; i++) {
        //omitting undefined null check for brevity
        if (myPosts[i].id.lastIndexOf(prefix, 0) === 0) {
            items.push(myPosts[i]);
        }
    }
    console.log(items);
}
			]]>
	    </script>
		<xsl:variable name="i" select="0" />
    	<xsl:for-each select="field">
    		
   			<xsl:if test="@type = 'proof_required'">

      			<div id= "documents" class="documents">
      				<xsl:variable name="x" select='$i + position()' /> 

       				<xsl:value-of select="name"/>
    				*:
				<select class="sample+{$x}" required="true" multiple="true">
						<xsl:for-each select="proof/attachments">
							<xsl:variable name="attachments" select="."/>
	            			<option value="{$attachments}">

	               				<xsl:value-of select="."/>

	            			</option>
	            		</xsl:for-each>
	            </select>

       		
  				</div>

      </xsl:if>
    </xsl:for-each>


    <div class="submit">
    <button type="submit" onclick="myFunction()" class="btn btn-success" value="submit">Next</button>
   	</div>
   	
    </xsl:template>

</xsl:stylesheet>




