import redis
import os
from flask import Flask, request

r = redis.Redis(host='redis', port=6379, password=os.environ["REDIS_PASSWORD"])

api = Flask(__name__)

@api.route('/<key>', methods=['GET'])
def get(key):  
  return json.dumps({"status": True, "value": r.get(key)})
  
@api.route('/<key>', methods=['POST'])
def set(key):  
  return json.dumps({"status": r.set(request.data), "value": key})
    
if __name__ == '__main__':
  api.run(host='0.0.0.0', port=8080)
