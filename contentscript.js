
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
	  

		console.log(request);
		
		console.log(request["nextpage"]);
		
		window.location.href = request["nextpage"];

	}
);



console.log("Hello");

chrome.runtime.sendMessage(
	{
		type:    "pushToDatabase",
		payload: {
			title : document.evaluate("//title/text()", document, null, XPathResult.STRING_TYPE, null).stringValue
		}
	}, function(response) {
		console.log(response);
	}
);


