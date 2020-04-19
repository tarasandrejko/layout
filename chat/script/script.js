function message(text) {
	jQuery('#chat-result').append(text);
}

var socket = new WebSocket("ws://localhost:8090/chat/server.php");

jQuery(document).ready(function($) {

	/*var socket = new WebSocket("ws://localhost:8090/chat/server.php");*/

	socket.onopen = function() {
		message("<div>Зєднання встановлено</div>");
	};

	socket.onerror = function(error) {
		message("<div>Помилка при зєднанні" + (error.message ? error.message : "") + "</div>");
	}

	socket.onclose = function() {
		message("<div>Зєднання закрито</div>");
	}
	var data = JSON.parse(event.data);

	socker.onmessage = function(event) {
		var data = JSON.parse(event.data);
		message("<div>" + data.type + " - " + data.message + "</div>");
	}
});
