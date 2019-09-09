
    			var globalArray = []
    			var globalSet = new Set()
    			
    			function getSelectedOptions(sel) {
				  var opts = [],opt;
				  var len = sel.options.length;
				  for (var i = 0; i != len; i++) {
				    opt = sel.options[i];

				    if (opt.selected) {
				      	opts.push(opt.value);
				      	globalArray.push(opt.value)
				      	globalSet.add(opt.value)
					}else{
				    	console.log("Hello World");

				    }
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


