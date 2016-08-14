
var tabId;


function pushToDatabase(content) {
	
	var req = new XMLHttpRequest();
	req.open("POST", "http://localhost:9000", true);
	req.onreadystatechange = function() {
		if (req.readyState == 4) {
			if (req.status == 200) {
				console.log(req.responseText);
				
				payload = JSON.parse(req.responseText);
				
				chrome.tabs.sendMessage(tabId, payload, function(response) {});
				
			}
		}
	};
	req.send(JSON.stringify(content));

}






chrome.runtime.onMessage.addListener(
	function(request, sender, sendResponse) {
		
		if (sender.tab) {
			
			tabId = sender.tab.id;
			
			
			if (request.hasOwnProperty("type")) {
				
				if (request["type"] === "pushToDatabase") {
					
					pushToDatabase(request);
					
				}
			}			
		}
		
					
		sendResponse({message: "message"});
	}
);
