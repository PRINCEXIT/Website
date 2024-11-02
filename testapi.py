from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/ffapi/V1', methods=['GET'])
def get_info():
    # Get the 'id' parameter from the request
    id = request.args.get('id')
    
    if not id:
        return jsonify({'error': 'ID parameter is required'}), 400
    
    # Construct the URL for the external API
    external_api_url = f'https://kelly-120-kaller.onrender.com/info/id={id}'
    
    try:
        # Make a request to the external API
        response = requests.get(external_api_url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Parse the JSON response

        return jsonify(data)  # Return the data as JSON
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
