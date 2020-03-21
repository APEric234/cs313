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