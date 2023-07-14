from markupsafe import escape
from flask import Flask, request, render_template
from twitter import get_tweets

app = Flask(__name__)

@app.route('/')
def home():
    # if request.method == 'POST':
    #     hashtag = request.form.get('textbox')
    #     parsed_text = parse_text(hashtag)
    #     print(parsed_text)
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result():
    hashtag = request.form['textbox']
    result_dict = get_result_dict(hashtag)
    return render_template('hashtag-form.html', hashtag=hashtag, results=result_dict)

def get_result_dict(hashtag):
    n = 1
    tweets = get_tweets(hashtag, n)
    for tweet in tweets:
        print(tweet.full_text)
    to_ret = {}
    to_ret["hashtag"] =  hashtag
    to_ret["num tweets"] = n
    to_ret["sentiment"] = "neutral"
    return to_ret
# @app.route('/tweet')
# def hastag_form():
#     return render_template('hastag-form.html')

# @app.route('/', methods=['POST'])
# def hastag_form_post():
#     text = request.form['text']
#     processed_text = text.upper()
#     return processed_text