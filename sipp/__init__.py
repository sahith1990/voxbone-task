import markdown
import os
import subprocess
import itertools

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = shelve.open("devices.db")
#     return db

# @app.teardown_appcontext
# def teardown_db(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()

@app.route("/")
def index():
    """Present some documentation"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)


class Call(Resource):
    def get(self):
        # payload_data=["A","B","C","D","E","F","G"]
        # service_urls=["s1","s2","s3"]
        # Mixed_lists = []
        # # get_roundrobin = roundrobin.basic(payload_data)
        # # Mixed_lists = ''.join([get_roundrobin() for _ in range(2)])
        # # test_echo = subprocess.run(["echo", text], capture_output=True, text=True)
        # for payload,url in zip(itertools.cycle(payload_data), service_urls):
        #     # Mixed_lists = list(itertools.izip(itertools.cycle(payload_data), service_urls))
        #     test_echo = subprocess.run(["echo", payload, url], capture_output=True, text=True)
        #     # print("{} for {}".format(payload,url))
        test_sipp = subprocess.run(["/usr/src/app/sipp-3.5.1/sipp", "-sn", "uac", "127.0.0.1", "-s", "+551126265587", "-m", "1"], capture_output=True, text=True)

        return { 'message': test_sipp.stdout }, 202


# class DeviceList(Resource):
#     def get(self):
#         shelf = get_db()
#         keys = list(shelf.keys())
#
#         devices = []
#
#         for key in keys:
#             devices.append(shelf[key])
#
#         return {'message': 'Success', 'data': devices}, 200
#
#     def post(self):
#         parser = reqparse.RequestParser()
#
#         parser.add_argument('identifier', required=True)
#         parser.add_argument('name', required=True)
#         parser.add_argument('device_type', required=True)
#         parser.add_argument('controller_gateway', required=True)
#
#         # Parse the arguments into an object
#         args = parser.parse_args()
#
#         shelf = get_db()
#         shelf[args['identifier']] = args
#
#         return {'message': 'Device registered', 'data': args}, 201
#
#
# class Device(Resource):
#     def get(self, identifier):
#         shelf = get_db()
#
#         # If the key does not exist in the data store, return a 404 error.
#         if not (identifier in shelf):
#             return {'message': 'Device not found', 'data': {}}, 404
#
#         return {'message': 'Device found', 'data': shelf[identifier]}, 200
#
#     def delete(self, identifier):
#         shelf = get_db()
#
#         # If the key does not exist in the data store, return a 404 error.
#         if not (identifier in shelf):
#             return {'message': 'Device not found', 'data': {}}, 404
#
#         del shelf[identifier]
#         return '', 204


api.add_resource(Call, '/sipp/call')
# api.add_resource(DeviceList, '/devices')
# api.add_resource(Device, '/device/<string:identifier>')
