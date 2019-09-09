
var currentTab = 0; // Current tab is set to be the first tab (0)
function init(){
  
  showTab(currentTab); // Display the current tab
  //alert("Loaded");
  //nextPrev(currentTab);
}

function showTab(n) {
  // This function will display the specified tab of the form...
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";
  //alert(x.length);
  //... and fix the Previous/Next buttons:
  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (n == (x.length - 1)) {
    document.getElementById("nextBtn").innerHTML = "Submit";
  } else {
    document.getElementById("nextBtn").innerHTML = "Next";
  }
  //... and run a function that will display the correct step indicator:
  //fixStepIndicator(n)
}

var globalArray = []
var globalSet = new Set()
var proof_Map = new Map();

function nextPrev(n) {
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");
  // Exit the function if any field in the current tab is invalid:
  if (n == 1 && !validateForm()) return false;
  // Hide the current tab:
  x[currentTab].style.display = "none";
  // Increase or decrease the current tab by 1:
  currentTab = currentTab + n;
  // if you have reached the end of the form...
  if(currentTab == 1){
    removeDivfromPage2();
  }
  if(currentTab == 2){
    getCheckedCheckboxesFor();
    //removeDivfromPage2();
    console.log("mapKey"+proof_Map.size)
    var get_keys = proof_Map.keys();
    var verification_set = new Set();
    for(var ele of get_keys){
      var temp_set = proof_Map.get(ele);
      temp_set.forEach(function(item){
        console.log("mapkey:"+ele+" mapval:"+item)
      if(verification_set.has(item)){
          console.log("Already inside Set");
          /*var label = document.createElement('Label');
          label.setAttribute("for", item);
          label.innerHTML = ele+":"+item;
          var input_tag = document.createElement('input');
          
          input_tag.setAttribute("type", "file");
          input_tag.setAttribute("name", ele);
          input_tag.setAttribute("id", item);
          input_tag.setAttribute("disabled", true);
          
          document.getElementById('page3').appendChild(label);
          document.getElementById('page3').appendChild(input_tag);  */
      }else{
      var label = document.createElement('Label');
      label.setAttribute("for", item);
      label.innerHTML = ele+":"+item;
      var input_tag = document.createElement('input');
      
      input_tag.setAttribute("type", "file");
      input_tag.setAttribute("name", ele);
      input_tag.setAttribute("id", item);
      
      document.getElementById('page3').appendChild(label);

      document.getElementById('page3').appendChild(input_tag);
      verification_set.add(item)
      }
        
      
      });
  }

  var input_tag = document.createElement('input');
      
    input_tag.setAttribute("type", "hidden");
    input_tag.setAttribute("name", "map");
    input_tag.setAttribute("id", "proofMapping");
    const myJson = {};
    const myString = "string value"
    myJson.myMap = mapToObj(proof_Map);
    //myJson.myString = myString;
    const json = JSON.stringify(myJson);
    input_tag.setAttribute("value", json); 
    document.getElementById("regForm").appendChild(input_tag);
  }
  if (currentTab >= x.length) {
    // ... the form gets submitted:
    
    
    document.getElementById("regForm").submit();
    return false;
  }
  
  showTab(currentTab);
}


function prev(n) {
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");
  // Exit the function if any field in the current tab is invalid:
  if (n == 1 && !validateForm()) return false;
  // Hide the current tab:
  x[currentTab].style.display = "none";
  // Increase or decrease the current tab by 1:
  currentTab = currentTab + n;
  if (currentTab == 1) {
      var inputs = document.getElementsByTagName('input');
      for(var i = 0; i < inputs.length; i++) {
          if(inputs[i].type.toLowerCase() == 'checkbox') {
              //alert(inputs[i].value);
              inputs[i].checked = false;
          }
      }
      // Remove all uploads from page3
      var e = document.getElementById('page3');
        e.innerHTML = "";

      // Remove input having proofMap
      var element = document.getElementById("proofMapping");
      element.parentNode.removeChild(element)  

      proof_Map.clear()
  }

  // if you have reached the end of the form...
  if (currentTab >= x.length) {
    // ... the form gets submitted:
    
    document.getElementById("regForm").submit();
    return false;
  }
  // Otherwise, display the correct tab:
  showTab(currentTab);
}

function validateForm() {
  // This function deals with validation of the form fields
  var x, y, i, valid = true;
  x = document.getElementsByClassName("tab");
  y = x[currentTab].getElementsByTagName("input");
  // A loop that checks every input field in the current tab:
  if(currentTab == 1){
    var alldivs = document.getElementsByClassName("documents_div");
    
    for(var i =0 ; i < alldivs.length; i++){
        var validate = false
        count=0;
        var span_ele = alldivs[i].childNodes;
        for(var j=0 ; j< span_ele.length; j++){
          var input_elements = span_ele[j].childNodes;
           for(var k=0 ; k < input_elements.length; k++){
            if(input_elements[k].checked == true){
              validate = true;
              break;
            }
            /*console.log(input_elements[k].checked)*/
           }
           valid = validate;
        }
        //.childNodes;
        //var input_elements = span_ele[0].childNodes;
        /*for(var j=0; j< input_elements.length; j++ ){
          if(input_elements[j].checked == true){
            validate = true
            break;
          }

        }*/

    }
    valid = validate
  }
  for (i = 0; i < y.length; i++) {
    // If a field is empty...
    if (y[i].value == "" && y[i].disabled !=true && y[i].placeholder != 'Optional') {
      // add an "invalid" class to the field:
      y[i].className += " invalid";
      // and set the current valid status to false
      valid = false;
    }
  }
  
  return valid; // return the valid status
}

function fixStepIndicator(n) {
  // This function removes the "active" class of all steps...
  var i, x = document.getElementsByClassName("step");
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }
  //... and adds the "active" class on the current step:
  x[n].className += " active";
}

function clearSelected(){
    var elements = document.getElementsByClassName("documents").options;

    for(var i = 0; i < elements.length; i++){
      elements[i].selected = false;
    }
  }

function getCheckedCheckboxesFor() {
    var checkboxName = "sample123";
    var checkboxes = document.querySelectorAll('input[name="' + checkboxName + '"]:checked') ;
    for(var i=0; i < checkboxes.length; i++ ){
      var elms = document.querySelectorAll('input[id="' + checkboxes[i].id + '"]');//"[id="'+duplicateID+"']");
      for(var k = 0; k < elms.length; k++){
        var x = elms[k].parentElement.parentElement.id;
        if(proof_Map.has(x)){
          var temp_set1 = proof_Map.get(x);
          temp_set1.add(checkboxes[i].id)

        }else{
          var temp_set2 = new Set();
          temp_set2.add(checkboxes[i].id);
          proof_Map.set(x, temp_set2);
        }
      }
      
    }
    console.log(proof_Map);
}

function mapToObj(map){
  const obj = {}
  for (let [k,v] of map){
     var v1 = Array.from(v)
    console.log(v1)
    obj[k] = v1
  }
  return obj
}

function removeDivfromPage2(){
  var input_list = document.getElementsByClassName('up-class');
  for(var i=0; i < input_list.length;i++){
    if(input_list[i].value != ''){
      
    }else{
      var element = document.getElementById(input_list[i].name);
      console.log(element)
      //element.innerHTML = "";
      element.parentNode.parentNode.removeChild(element.parentNode)
    }
  }


}
