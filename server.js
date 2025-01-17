const express = require("express");
const bodyParser = require("body-parser");
const path = require("path");

const app = express();
const port = 3000;

// Middleware
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, "public")));

// Route to handle contact form submission
app.post("/contact", (req, res) => {
  const { name, email, message } = req.body;

  // Here you can save the data to a database or send an email
  console.log(`Name: ${name}, Email: ${email}, Message: ${message}`);

  // Send response back to the client
  res.json({ message: "Thank you for your message!" });
});

// Serve the HTML file
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
