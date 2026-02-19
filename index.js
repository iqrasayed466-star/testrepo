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
    // Sanitize input to prevent XSS
    const sanitizedName = req.query.name ? req.query.name.replace(/<|>|&|"/g, '') : '';
    res.send(`<h1>Hello ${sanitizedName}</h1>`);
});

app.listen(3000, () => console.log('Vulnerable app listening on port 3000'));