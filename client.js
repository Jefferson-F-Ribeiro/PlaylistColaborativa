const WebSocket = require('ws');

const ws = new WebSocket('ws://localhost:8765');

ws.onopen = function() {
    console.log("Connected to the server.");
};

ws.onmessage = function(event) {
    console.log("Received message: " + event.data);
};

ws.onclose = function() {
    console.log("Disconnected from the server.");
};

ws.onerror = function(error) {
    console.error("Error: " + error);
};

function sendMessage(message) {
    ws.send(message);
}