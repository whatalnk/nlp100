from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient, ASCENDING, DESCENDING

# [ウェブアプリケーションフレームワーク Flask を使ってみる - Qiita](http://qiita.com/ynakayama/items/2cc0b1d3cf1a2da612e4) を参考にした
# アーティスト名で検索して結果をrating.valueの大きい順に並べる

client = MongoClient('localhost', 27017)
db = client.artists
collection = db.tags

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        name = request.form['name']
        artists = []
        for i in collection.find({"name": name}).sort("rating.value", DESCENDING):
            artist = {"name": i["name"]}
            if "aliases" in i.keys():
                artist["aliases"] = ",".join([t["name"] for t in i["aliases"]])
            else:
                artist["aliases"] = ""
            if "tags" in i.keys():
                artist["tags"] = ",".join([t["value"] for t in i["tags"]])
            else:
                artist["tags"] = ""
            if "rating" in i.keys():
                artist["rating"] = i["rating"]["value"]
            else:
                artist["rating"] = ""
            artists.append(artist)
        return render_template('index.html',
                               name=name, artist_info=artists)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True 
    app.run()