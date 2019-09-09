<xsl:stylesheet version="1.0"
	xmlns:xsl = "http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html"/>

	<xsl:template match="/">
		<html>
		<head>
			<title>dxhcb</title>
<!-- 	  <meta charset="utf-8">
	  <meta name="viewport" content="width=device-width, initial-scale=1">
	  <link rel="stylesheet" href="css/bootstrap.min.css">
	  <script src="js/jquery.min.js"></script>
	  <script src="js/bootstrap.min.js"></script>
 -->
<!-- 			<link rel="stylesheet" type="text/css" href="style.css" /> -->
		<style>
		#regForm {
		background-color: #fff;
		margin: 100px auto;
		font-family: Raleway;
		padding: 40px;
		width: 70%;
		min-width: 300px;
		}
		body {
		  background-color: skyblue;
		}

		h1 {
		text-align: center;  
		}

		input {
		padding: 10px;
		width: 100%;
		font-size: 17px;
		font-family: Raleway;
		border: 1px solid #aaaaaa;
		}
input.invalid {
  background-color: #ffdddd;
}

* {
  box-sizing: border-box;
  padding:10px;
}

/* Hide all steps by default: */
.tab{
	display: none;
}


button {
  background-color: #4CAF50;
  color: #ffffff;
  border: none;
  padding: 10px 20px;
  font-size: 17px;
  font-family: Raleway;
  cursor: pointer;
}

button:hover {
  opacity: 0.8;
}

#prevBtn {
  background-color: #bbbbbb;
}

/* Make circles that indicate the steps of the form: */
.step {
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbbbbb;
  border: none;  
  border-radius: 50%;
  display: inline-block;
  opacity: 0.5;
}

.step.active {
  opacity: 1;
}

/* Mark the steps that are finished and valid: */
.step.finish {
  background-color: #4CAF50;
}

		</style>


		</head>	
		<body onload="init()">
			<div class="container">
				<script  type="text/javascript" src="addform.js">
					
					<p>Hello</p>
				</script>
				<h1>Please Fill detail form</h1>
				
				<form action="" id='regForm' method ="post" name="myform" enctype="multipart/form-data" onsubmit="return(dependency());" >
					<xsl:apply-templates/>
					<div style="overflow:auto;">
    			<div style="float:right;">
      				<button type="button" id="prevBtn" onclick="prev(-1)">Previous</button>
      			<button type="button" id="nextBtn" onclick="nextPrev(1)">Next</button>
    			</div>
  				</div>

				<div id="page3" class="tab" ></div>
				
				
				  <!-- Circles which indicates the steps of the form: -->
			       <!-- <div style="text-align:center;margin-top:40px;">
				    <span class="step"></span>
				    <span class="step"></span>
				    <span class="step"></span>
		     		</div> -->

				</form>


			</div>
			
		</body>
	</html>
	</xsl:template>



	<xsl:template match="policy-name">
		<script type="text/javascript">
    		<![CDATA[


    			var globalArray = []
    			var globalSet = new Set()
    			var myMap = new Map();

    			function getSelectedOptions(sel) {
				  var opts = [],opt;
				  var len = sel.options.length;
				  for (var i = 0; i != len; i++) {
				    opt = sel.options[i];

				    if (opt.selected) {
				    	// Example Code
				    	//console.log("selected option"+opt.value)

				    	if(myMap.has(sel.name)){
				    	 var selected_elements = myMap.get(sel.name);
				    	 if(selected_elements.has(opt.value)){
				    	 	selected_elements.delete(opt.value);
				    	 }else{
				    	 	selected_elements.add(opt.value);
				    	 }
				    	 myMap.set(sel.name , selected_elements);
				    	 globalSet.add(opt.value)
				    	}
				    	else{
				    		var temp_array = new Set();
				    		temp_array.add(opt.value);
				    		myMap.set(sel.name, temp_array);
				    		globalSet.add(opt.value);
				    	}
                  	}
                
          			console.log(myMap);
				  }
				}

				function generatePage3(){
						globalSet.forEach(function(item){
						  var label = document.createElement('Label');
					      label.setAttribute("for", item);
					      label.innerHTML = item;
					      var input_tag = document.createElement('input');
					      
					      input_tag.setAttribute("type", "file");
					      input_tag.setAttribute("name", item);
					      input_tag.setAttribute("id", item);
					      
					      document.getElementById('page3').appendChild(label);
					      document.getElementById('page3').appendChild(input_tag);
					      
					      console.log(globalSet)
						});
					      
					
				}


//pages js css added stuff

//end of css,js pages 

			]]>
	</script>
		<h3>Policy Name is <xsl:value-of select="@title"/></h3>
		<div id="page1" class="tab" >
		<xsl:apply-templates select="field"/>
		</div>

		<div id="page2" class="tab" >
			<xsl:for-each select="field">
   			<xsl:if test="@type = 'proof_required'">
      			<div id="doc" class="documents_div">

       				<xsl:value-of select="name"/>
    				*:
				<!-- <select name="{name}" class="select1" required="true" multiple="true" onChange="getSelectedOptions(this)">
						<xsl:for-each select="proof/attachments">
							<xsl:variable name="attachments" select="."/>
	            			<option class="documents" value="{$attachments}" >
	            				<xsl:value-of select="."/>

	            			</option>
	            		</xsl:for-each>
	            </select> -->
	            <div id="{name}">
	            <xsl:for-each select="proof/attachments">
	            <span>
	            	<xsl:variable name="attachments" select="."/>
    				<input name="sample123" type="checkbox" id="{$attachments}">
    				<xsl:value-of select="."/>
    			</input>
    			</span>
    			</xsl:for-each>
    			</div>
       		
  				</div>

      </xsl:if>
    </xsl:for-each>
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
				</xsl:if>
				
				<xsl:if test="meta = 'R'">
					<label for="{$name}"><xsl:value-of select="name"/>*:</label>
					<div class="form-group">
						<input type="{$datatype}" name="{$name}" required="true" class="form-control" placeholder="Required" pattern="{$pattern}" title="{$message}"/>
					</div>
				</xsl:if>

				<xsl:if test="meta = 'O'">
					<label for="{$name}"><xsl:value-of select="name"/>:</label>
					<div class="form-group">
						<input type="{$datatype}" name="{$name}" class="form-control" placeholder="Optional" pattern="{$pattern}" title="{$message}"/>
					</div>
				</xsl:if>

			</xsl:otherwise>
		</xsl:choose>	
	</xsl:template>
</xsl:stylesheet>