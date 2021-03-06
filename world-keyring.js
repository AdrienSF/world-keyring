const encoder = new TextEncoder();
const decoder = new TextDecoder();

function checkLoaded() {
  console.log("world-keyring loaded on: " + siteName);
}


// this function is not the conventional way to "xor" two strings, it is the xor between ASCII representations of strings
function pseudo_XOR_str(a, b) {
  // convert strings to ASCII char codes
  var aList = a.split('');
  var bList = b.split('');
  var xored = '';
  for (var i = 0; i < aList.length && i < bList.length; i++) {
    xored += String.fromCharCode(aList[i].charCodeAt() ^ bList[i].charCodeAt());
  }

  return xored
}

function failureCallback(error) {
  console.error("Error: " + error);
}

function successCallback(result) {
  var hashed = decoder.decode(result);
  console.log("autoFilling with password: " + hashed);

  // get password input element(s)
  var allInputs = document.getElementsByTagName('input');

  for(var i = 0; i < allInputs.length; i++) {
    if(allInputs[i].type.toLowerCase() == 'password' && allInputs[i].id != 'masterPassInput') {
      console.log(allInputs[i]);
      // autofill
      allInputs[i].value = hashed;
    }
  }

}

function autoFill() {
  var masterPassword = document.getElementById("masterPassInput").value;
  var toHash = pseudo_XOR_str(siteName, masterPassword);
  console.log("toHash: " + toHash);
  const shaPromise = crypto.subtle.digest('SHA-1', encoder.encode(toHash));
  shaPromise.then( successCallback, failureCallback );
}


// get website name
// var siteName = window.location.href.split("/")[2];
var siteName = window.location.href;

// display master password input
var masterPassLabel = document.createElement("t");
masterPassLabel.innerText = "Input master password: ";
var masterPassInput = document.createElement("input");
masterPassInput.type = "password";
masterPassInput.id = "masterPassInput";
var autoFillButton = document.createElement("button");
autoFillButton.className = "btn";
autoFillButton.onclick = function(){autoFill();}
autoFillButton.innerHTML = "auto-fill password";

var masterPassInputDiv = document.createElement('div');
masterPassInputDiv.appendChild(masterPassLabel);
masterPassInputDiv.appendChild(masterPassInput);
masterPassInputDiv.appendChild(autoFillButton);

document.body.prepend(masterPassInputDiv);


checkLoaded();
