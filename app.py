from flask  import Flask, request, jsonify
from flask_restful import reqparse

app = Flask(__name__)

temps_put_args = reqparse.RequestParser()
temps_put_args.add_argument('GPU Core' , type=str)
temps_put_args.add_argument('GPU Fan' , type=str)
temps_put_args.add_argument('CPU Package' , type=str)

@app.route('/temps', methods=['PUT'])
def temps():
    args = temps_put_args.parse_args()
    with open('temps.txt', 'w', encoding='utf-8') as f:
        f.write('Hardware Monitor: \n\n')
        f.write(str(args))
    return jsonify(args), 200


if __name__ == '__main__':
    app.run(debug=True)