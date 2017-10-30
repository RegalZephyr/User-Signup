from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
password = ""
user = ""
email = ""
@app.route("/")
def form():"""
    <!DOCTYPE html>
        <html>
            <head>
                <style>
                    .error {
                        color: red;
                    }
                </stle>
            </head>
        <body>
        <h1> User Signup </h1>
           <form action="/action_page.php">
                Username:<br>
                <input type="text" name="username" value="">
                <br>
                Password:<br>
                <input type="text" name="password" value="">
                Resubmit password:<br>
                <input type="text" name="verification" value="">
                Email(optional):<br>
                input type="text" name="verification" value="">
                <input type="submit" value="Submit">
            </form> 
        </html>

"""

app.run()