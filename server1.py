const express = require('express');
const app = express();
const jwt = require('jsonwebtoken');

// Hardcoded Secret
const DB_PASSWORD = "supersecretpassword123";

app.get('/unsafe', (req, res) => {
    // Reflected XSS Vulnerability
    const name = req.query.name;
    res.send("<h1>Hello " + name + "</h1>");
});

app.post('/login', (req, res) => {
    // Weak Cryptography / Hardcoded JWT Secret
    const token = jwt.sign({ user: 'admin' }, 'secret', { expiresIn: '1h' });
    res.json({ token });
});

app.get('/files', (req, res) => {
    // Path Traversal
    const filePath = req.query.path;
    res.sendFile(filePath);
});

app.listen(3000);
