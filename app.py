from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():  # <--- This name is the "endpoint"
    return render_template('service.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # This captures the data from your contact.html form
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # For now, we print it to your terminal
        print(f"New Message from {name}: {message}")
        
        # You can redirect back or show a success message
        return "<h1>Message Sent successfully!</h1><a href='/'>Go Home</a>"
        
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)