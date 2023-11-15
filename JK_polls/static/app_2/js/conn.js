const mysql = import("default")

// Create a connection pool
const pool = mysql.createPool({
  host: "localhost", // Replace with your database host
  user: "jk_poll", // Replace with your database username
  password: "admin_jk_poll", // Replace with your database password
  database: "django" // Replace with your database name
})

// Get a connection from the pool
pool.getConnection((err, connection) => {
  if (err) {
    console.error("Error connecting to MariaDB:", err)
    return
  }

  console.log("Connected to MariaDB!")

  // Use the connection for database operations

  // Release the connection when done
  connection.release()
})
//modules.export = getBlogTitle;