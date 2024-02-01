from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        image = request.files['image']
        with open('log/DataLib.txt', 'a') as f:
            f.write(f'Text: {text}\n')
            f.write(f'Image: {image.filename}\n')
            image.save('uploads/' + image.filename)
        return '完成！'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)