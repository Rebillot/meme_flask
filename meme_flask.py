from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    url = 'https://meme-api.com/gimme'
    response = json.loads(requests.get(url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]

    return meme_large, subreddit

@app.route('/')
def index():
    meme_large, subreddit = get_meme()
    return render_template('meme_index.html', meme_large=meme_large, subreddit=subreddit)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
