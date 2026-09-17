import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

export default function App() {
  const [url, setUrl] = useState('');
  const [qrImage, setQrImage] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleGenerate = async (e) => {
    e.preventDefault();
    if (!url.trim()) return;

    setLoading(true);
    setError('');
    setQrImage(null);

    try {
      const response = await axios.get(`http://127.0.0.1:8000/generated-qr`, {
        params: { url: url.trim() },
        responseType: 'blob',
      });

      const imageObjectURL = URL.createObjectURL(response.data);
      setQrImage(imageObjectURL);
    } catch (err) {
      if (err.response && err.response.status === 400) {
        setError('Please enter a valid URL starting with http:// or https://');
      } else {
        setError('Failed to generate QR code. Please check your backend connection.');
      }
    } finally {
      setLoading(false);
    }
  };

  const handleDownload = () => {
    if (!qrImage) return;
    const link = document.createElement('a');
    link.href = qrImage;
    link.download = 'qrcode.png';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="page-wrapper">
      <div className="card">
        <h1 className="title">QR Code Generator</h1>
        <p className="subtitle">Enter a web address below to generate your QR code instantly.</p>

        <form onSubmit={handleGenerate} className="qr-form">
          <input
            type="url"
            placeholder="https://example.com"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            className="qr-input"
            required
            autoCapitalize="none"
            autoCorrect="off"
          />
          <button type="submit" disabled={loading} className="generate-btn">
            {loading ? 'Generating...' : 'Generate QR'}
          </button>
        </form>

        {error && <div className="error-message">{error}</div>}

        {qrImage && (
          <div className="result-container">
            <div className="qr-wrapper">
              <img src={qrImage} alt="Generated QR Code" className="qr-image" />
            </div>
            <button onClick={handleDownload} className="download-btn">
              Download PNG
            </button>
          </div>
        )}
      </div>
    </div>
  );
}