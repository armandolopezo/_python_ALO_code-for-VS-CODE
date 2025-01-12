from flask import Flask, redirect
app = Flask(__name__)
@app.route('/')
def page():
    return redirect('http://mediatech.com.ec/', code=301)
if __name__ == "__main__":
    app.run()

  