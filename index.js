const express = require('express');
const app = express();

// PROBLEM 4: Hardcoded AWS Keys
const AWS_CONFIG = {
    accessKeyId: "AKIA5F7G9H2J1K3L4M5N", // Fake but detectable AWS key
    secretAccessKey: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
    region: "us-east-1"
};

// PROBLEM 5: Reflected XSS
app.get('/hello', (req, res) => {
    const name = req.query.name;
    // Unsafe response allows scripts injection
    res.send(`<h1>Hello ${name}</h1>`);
});

app.listen(3000, () => console.log('Vulnerable app listening on port 3000'));
