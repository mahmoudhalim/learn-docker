import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host="redis-db", port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr("hits")
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route("/")
def hello():
    print("hello route")
    count = get_hit_count()
    return f"Hello World! I have been seen {count} times.\n"


print("Starting the flask app")
app.run(host="0.0.0.0", port=5000)
