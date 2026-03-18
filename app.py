from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)
#API endpoint, used when visiting a site using /url_preview
@app.route('/url_preview')
def link_preview():
    #get the site from the url, have example.com as default
    site = request.args.get('site', 'http://example.com')
    try:
        #send a HEAD request to the site so as to get metadata, with a timeout of 3 seconds
        response = requests.head(site, timeout=3)
        #pack the info into a json response
        return jsonify({
            "result": "link preview got generated successfully",
            "timestamp": int(time.time()),
            "status": "success",
            "site": site,
            "server": response.headers.get('Server', 'Unknown')
        })
    except Exception as e:
        #if the site is down or invalid send an error message
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    #bind to 0.0.0.0 so that the container can be accessed from outside the container
    # using port 8080
    app.run(host='0.0.0.0', port=8080)