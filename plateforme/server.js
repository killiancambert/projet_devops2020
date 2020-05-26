const http = require('http');
var fs = require('fs');

const hostname = '127.0.0.1';

const express = require('express')
const app = express()
const port = 8080
const path = require('path')

const server = http.createServer((req, res) => {
  fs.readFile('index.html', function(err, data) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(data);
    return res.end();
  });
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});



// app.get('/', function(req, res) {
//     res.sendFile(path.join(__dirname + '/index.html'));
// });

// app.listen(port, () => console.log(`App listening at http://localhost:${port}`))

// function css(request, response) {
//   if (request.url === '/styles.css') {
//     response.writeHead(200, {'Content-type' : 'text/css'});
//     var fileContents = fs.readFileSync('/styles.css', {encoding: 'utf8'});
//     response.write(fileContents);
//   }
// } 