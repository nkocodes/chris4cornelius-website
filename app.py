from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'chris4corneliuscampaign@gmail.com'
app.config['MAIL_PASSWORD'] = #Hidden from Github Public View

mail = Mail(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/issues")
def issues():
    return render_template("issues.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/form", methods=["GET", "POST"])
def forward():
    full_name = request.form.get("fname")
    zipcode = request.form.get("zip")
    email = request.form.get("email")
    
    if request.method =='POST':
        vmsg = Message("Chris4Cornelius", sender='noreply@demo.com', recipients=[email])
        vmsg.body = f"Hello {full_name}, thank you for showing interest in our campaign. We will be contacting you shortly for ways you can volunteer."
        mail.send(vmsg)
        cmsg = Message("New Volunteer!", sender='noreply@demo.com', recipients=['chris4cornelius@gmail.com'])
        cmsg.body = f"{full_name} from zip-code {zipcode} at {email} has shown interest in joining the campaign."
        mail.send(cmsg)
    return render_template('form.html')



if __name__ == "__main__":
    app.run(debug=True)
