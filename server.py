from flask import Flask, send_from_directory, render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:filename>')
def download_file(filename):
    return send_from_directory('files', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
