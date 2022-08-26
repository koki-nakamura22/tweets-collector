from chalice.app import Chalice

app = Chalice(app_name='tweets-collector')
app.debug = True


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/tweet/search')
def tweet_search():
    from chalicelib.twitter.twitter_api_wrapper import TweetAPIWrapper
    return TweetAPIWrapper.search()


@app.route('/a')
def collect_tweets():
    pass

    # The view function above will return {"hello": "world"}
    # whenever you make an HTTP GET request to '/'.
    #
    # Here are a few more examples:
    #
    # @app.route('/hello/{name}')
    # def hello_name(name):
    #    # '/hello/james' -> {"hello": "james"}
    #    return {'hello': name}
    #
    # @app.route('/users', methods=['POST'])
    # def create_user():
    #     # This is the JSON body the user sent in their POST request.
    #     user_as_json = app.current_request.json_body
    #     # We'll echo the json body back to the user in a 'user' key.
    #     return {'user': user_as_json}
    #
    # See the README documentation for more examples.
    #
