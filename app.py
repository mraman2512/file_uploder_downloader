import os
import urllib.request
from flask import Flask, render_template, request
from flask import send_file

app = Flask(__name__)


@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file_url = request.form.get("projectFilePath", "")

        file_name, file_extension = os.path.splitext(file_url)

        save_name = 'demo' + str(file_extension)  # local name to be saved

        if os.path.exists(save_name):

            try:
                os.remove(save_name)
            except:
                print("Error while deleting file")

        urllib.request.urlretrieve(file_url, save_name)
        return render_template('downloader.html', file_name = save_name)



@app.route('/download')
def download():
    file_name = request.args.get("file_name", "")
    return send_file(file_name, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

