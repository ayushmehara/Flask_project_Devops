const express = require('express');
const path = require('path');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();
const API_TARGET = process.env.API_TARGET || 'http://backend:5000';

app.use('/api', createProxyMiddleware({
    target: API_TARGET,
    changeOrigin: true
}));

app.use('/submit', createProxyMiddleware({
    target: API_TARGET,
    changeOrigin: true
}));

app.use(express.static('public'));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

const PORT = 3000;

app.listen(PORT, () => {
    console.log(`Frontend running on port ${PORT}`);
});