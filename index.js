const express = require('express');
const app = express();
const helmet = require('helmet');

// PROBLEM 4: Hardcoded AWS Keys
const AWS_CONFIG = {
    accessKeyId: "AKIA5F7G9H2J1K3L4M5N", // Fake but detectable AWS key
    secretAccessKey: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
    region: "us-east-1"
};

// PROBLEM 5: Reflected XSS
app.get('/hello', helmet.contentSecurityPolicy(), (req, res) => {
    const name = req.query.name;
    // Safe response prevents scripts injection
    res.send(`<h1>Hello ${name}</h1>`);
});

app.listen(3000, () => console.log('Vulnerable app listening on port 3000'));
```

Note: The `helmet.contentSecurityPolicy()` function is used to prevent XSS attacks by setting the Content-Security-Policy header, which defines which sources of content are allowed to be executed.