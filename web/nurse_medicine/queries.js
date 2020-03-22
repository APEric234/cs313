const Pool = require('pg').Pool
const pool = new Pool({
  user: 'kxgzangzhzkpdm',
  host: 'ec2-184-72-236-3.compute-1.amazonaws.com',
  database: 'dergo389khd0pd',
  password: 'c29f98a332d055f61fc092dbfef16a865ee78b843444b8846dfc3d60fb1c19f4',
  port: 5432,
})

const getMedicines = (request, response) => {
  pool.query('SELECT * FROM medicine', (error, results) => {
    if (error) {
      throw error
    }
    response.status(200).json(results.rows)
  })
}

module.exports = {
  getMedicines
}