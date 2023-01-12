from flask import Flask
from flask_restful import Resource, Api

import main


app=Flask(__name__)
api=Api(app)


class Quote(Resource):
    
    @app.route('/wifi/<int:id>')
    def get(id):
        x=main.main_(id)
        if x==-1:
            return 'Not found', 404
        else:
            return x, 200
    
    @app.route('/trace')
    def trace():
        x=main.output()
        return x, 200
    



if __name__ == '__main__':
    

    app.run(host="0.0.0.0", port="8080",debug=True)

        