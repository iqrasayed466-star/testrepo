const express = require('express');
const app = express();
const jwt = require('jsonwebtoken');
const helmet = require('helmet');

// Hardcoded Secret
const DB_PASSWORD = "supersecretpassword123";

// Enable Helmet to protect against common web vulnerabilities
app.use(helmet());

app.get('/unsafe', (req, res) => {
    // Reflected XSS Vulnerability Fix: Use template literals and HTML escaping
    const name = req.query.name;
    res.send(`<h1>Hello ${name}</h1>`);
});

app.post('/login', (req, res) => {
    // Weak Cryptography / Hardcoded JWT Secret
    const token = jwt.sign({ user: 'admin' }, 'secret', { expiresIn: '1h' });
    res.json({ token });
});

app.get('/files', (req, res) => {
    // Path Traversal Fix: Validate and sanitize the file path
    const filePath = req.query.path;
    if (filePath && filePath.startsWith('/')) {
        res.status(400).send('Invalid file path');
    } else {
        const sanitizedPath = require('path').join(__dirname, filePath);
        res.sendFile(sanitizedPath);
    }
});

app.listen(3000);