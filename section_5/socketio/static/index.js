// This code does not work!
// please watch section video for explanation of what was typed
// THIS CODE DOES NOT WORK


document.addEventListener('DOMContentLoaded', () => {

    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // When connected, configure buttons
    socket.on('connect', () => {

        // Each button should emit a "submit vote" event
        document.querySelector('create-channel').onclick = () => {
                const name = document.querySelector('input[name]').value;
                socket.emit('create-channel', {'name': name});
            };

            // Each button should emit a "submit vote" event
        document.querySelector('new-message').onclick = () => {
                // Get the channel
                // Get the message 
                socket.emit('send-message', {'channel': channel, 'msg': msg});
            };
    });

    // When a new vote is announced, add to the unordered list
    socket.on('vote totals', data => {
        document.querySelector('#yes').innerHTML = data.yes;
        document.querySelector('#no').innerHTML = data.no;
        document.querySelector('#maybe').innerHTML = data.maybe;
    });
});
