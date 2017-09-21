
/*

Copyright 2017, James Melanson, jmelanson1965@gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, and distribute
copies of the Software, and to permit persons to whom the Software is furnished to do so, subject
to the following conditions:

  -The original copyright notice (above) shall remain intact.
  
  -The above copyright notice and this permission notice shall be included in all copies or
   substantial portions of the Software.

  -THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
   BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
   NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
   DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

NOTE: Refer to the accompanying ajax_demo.html for information on how to use this file.

*/

function loadStringToFunction(sourceURL, funcName, funcArgument) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      window[funcName](this.responseText, funcArgument);
    }
  };
  xhttp.open("GET", sourceURL, true);
  xhttp.send();
} 
  
function loadJSONToFunction(sourceURL, funcName, funcArgument) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var useFunction = funcName;
      window[funcName](this.responseText, funcArgument);
    }
  };
  xhttp.open("GET", sourceURL, true);
  xhttp.send();
} 

