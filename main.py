import redis
import os
from flask import Flask, json, request

r = redis.Redis(host='redis', port=6379, password=os.environ["REDIS_PASSWORD"],decode_responses=True)

api = Flask(__name__)

@api.route('/', methods=['GET'])
def index():  
  return json.dumps({"status": True, "value": "It's Work !"})

@api.route('/<key>', methods=['GET'])
def get(key):  
  return json.dumps({"status": True, "value": r.get(key)})
  
@api.route('/<key>', methods=['POST'])
def set(key):  
  return json.dumps({"status": r.set(key, request.data), "value": key})
    
if __name__ == '__main__':
  api.run(host='0.0.0.0', port=8080)
