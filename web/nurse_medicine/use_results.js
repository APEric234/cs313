function search() {
  const { Pool, Client } = require('pg')
  const connectionString = 
  'postgres://kxgzangzhzkpdm:c29f98a332d055f61fc092dbfef16a865ee78b843444b8846dfc3d60fb1c19f4@ec2-184-72-236-3.compute-1.amazonaws.com:5432/dergo389khd0pd'
  const pool = new Pool({
    connectionString: connectionString,
  })
  pool.query('SELECT NOW()', (err, res) => {
    console.log(err, res)
    pool.end()
  })
  const client = new Client({
    connectionString: connectionString,
  })
  client.connect()
  client.query('SELECT NOW()', (err, res) => {
    console.log(err, res)
    client.end()
  })
  // Get the value from the search box
  var searchString = document.getElementById('txtSearch').value;
  console.log('Searching for: ' + searchString);
  // Set up the parameters to send to the API
  var params =
    '?&apikey=78b2fe4b&s=' + encodeURIComponent(searchString);
  var url = 'https://www.omdbapi.com/' + params;
  //call fetch with our url...remember that fetch returns a Promise
  //that must be processed with a call to the .then() method.
  console.log(getenv('DATABASE_URL'));
  fetch(url)
    .then(function(response) {
      // fetch also returns a stream as the result...we have to tell it
      // how to format the stream...our choices are: json, text, or blob (binary data)
      return response.json();
      // the json() method also returns a promise...so we need
      //to call .then() on it as well (shown on the next line)
    })
    .then(function(data) {
      // we now have our data and can use it to update our page.
      updateResultList(data);
    });
}
function updateResultList(data) {
  console.log('UpdateResultList');
  console.log(data);
  console.log(data.Search)
  if (data.Search && data.Search.length > 0) {
    console.log("list")
    const resultList = document.getElementById('ulResults');
    resultList.innerHTML = '';
    // you could use a forEach here as well...it would change the following line like this:
    // data.Search.forEach(function(item){ ...process each item here })
    for (let i = 0; i < data.Search.length; i++) {
      const title = data.Search[i].Title;
      console.log('Adding: ' + title);
      const content = `<li><p>${title}</p></li>`;
      resultList.innerHTML += content;
    }
  }
}