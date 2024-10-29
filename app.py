from flask import Flask, request, jsonify
from flask_cors import CORS
import scrap

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/scrape', methods=['POST'])
def scrape_data():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    # Scrape data based on the input URL
    headings, links, images = scrap.get_scraped_data(url)

    return jsonify({
        "headings": [heading.text for heading in headings],
        "links": [link.get('href') for link in links if link.get('href')],
        "images": [img.get('src') for img in images if img.get('src')]
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
