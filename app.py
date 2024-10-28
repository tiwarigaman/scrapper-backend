from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
import scrap  # Import your scraping logic from scrap.py

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/data', methods=['GET'])
def get_data():
    # Extract data using your scraping logic
    headings, links = scrap.get_scraped_data()

    # Return the data as JSON
    return jsonify({
        "headings": [heading.text for heading in headings],
        "links": [link.get('href') for link in links if link.get('href')]
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
