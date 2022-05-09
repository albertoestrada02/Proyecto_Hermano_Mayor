
//const express = require('express')
//const app = express()
//const port = 3006

const mysql = require('mysql')
const connection = mysql.createConnection({
  host     : 'hermanomayordb.mysql.database.azure.com',
  user     : 'Big_brother@hermanomayordb',
  password : 'kirbys_N',
  database : 'bigbrotherdb',
  port : 3006
});

connection.connect();

connection.query('SELECT * FROM bigbrotherdb.usert ', (err, rows, fields) => {
  if (err) throw err;
  console.log(rows);
});

connection.end()