from flask import Flask, render_template, request, redirect

# initialize app flask object
# intializing to the name of the file
app = Flask(__name__)

# now we use app routing to map a function to a given page of our website
# in app routing, it starts from the root of our website
# so if our website is mysite.com, and we wanted to route to mysite.com/hello
# we would pass /hello to the app route call

# app routing uses special @ and then the flask app oobject
# then we immediately define the associated function for the URL
@app.route("/test")
def testfunc():
    return "Testing web page!"

# we can have several routes for the different pages on our website
# just by adding more app routes and the subsequent functions that handle them

# page when the chat dialog (transcript or file) is submitted
@app.route('/dialogSubmitted', methods=['POST', 'GET'])
def route_dialog_submitted():
    if request.method == 'POST':
        if request.args['source'] == 'transcript':
            # handle chat transcript form
            # using the name attribute of the text input tag in index.html
            transcript_text = request.form['dialog_text_box']
            return render_template('console.html', content='The text: {}'.format(transcript_text))
        else:
            return render_template('console.html', content='{}-{}'.format(request.args, request.mimetype))
    else:
        return 'Get Request Called!'

# submit chat transcript text
@app.route('/ChatTranscript', methods=['POST', 'GET'])
def route_chat_transcript():
    return render_template('chat_transcript.html')

# for the root of the website, we would just pass in "/" for the url
@app.route('/')
def index():
    # render index html which contains the form
    # form submission will route to /submitForm
    return render_template('index.html')

# running the code
if __name__ == '__main__':
    # debug is true to show errors on the webpage
    app.run(debug=True)