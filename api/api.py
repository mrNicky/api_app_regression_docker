
from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from joblib import dump, load
from flask_httpauth import HTTPDigestAuth

app = Flask(__name__)
api = Api(app)
#app.config['SECRET_KEY'] = 'lol'
api = Api(app)
auth = HTTPDigestAuth()

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('text')
parser.add_argument('key')


def auth(key):
    api_key = "lol"
    if key == api_key:
        return True
    else:
        return False

class Welcome(Resource):
    def get(self):
        return jsonify({
                    "Message" : "Bonsoir, ceci est la beta d'un algorithm d'analyse de sentiment",
                    "Status Code": 200
                })
        
class SentimentAnalysis(Resource):
    def post(self):
        #postedData = request.get_json(force=True)
        #print(postedData)
       # text = postedData["text"]

        try:
            #try:
            args = parser.parse_args()
            text = args['text']
            key = args['key']
            print("args", args)
            if text is None and key is None:
                postedData = request.get_json(force=True)
                text = postedData["text"]
                key = postedData["key"]
                print(postedData)
            if auth(key):
                clf_pipe = load('sentiment.pkl')
                prediction = clf_pipe.predict([text])[0]
                prediction = "Positif" if prediction == 1 else "Négatif"
                return jsonify({
                    "text" : text,
                    "prediction" : prediction,
                    "Status Code": 200
                }
                )
            else:
                return jsonify({"auth": "Invalid auth key"})
        except:

            return jsonify({"auth": "no key"})



api.add_resource(SentimentAnalysis, "/sentiment")
api.add_resource(Welcome, "/welcome")

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0") 
