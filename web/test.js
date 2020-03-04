const http = require('http');

const onRequest= (request,response) => {

  if (request.url == "/home"){
    response.statusCode =200;
    response.write("<h1>Welcome to the home page</h1>");
  } else if (request.url == "/getData"){
    response.statusCode =200;
    let student ={
      name: 'Eric Allen'
      , class: 'CS313'
    };
    response.setHeader('Content-Type', 'application/json');
    response.end(JSON.stringify(student));

  }else{
    response.statusCode =404;
    response.write("Page not found");
  }

}



const hostname = '127.0.0.1';
const port = 8888;

const server = http.createServer(onRequest);

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
console.log("Hello world");