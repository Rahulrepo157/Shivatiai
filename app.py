from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

# Home route
@app.route('/')
def home():
    """View for the home page."""
    return render_template('home.html')


# Get material data API



# Page routes
@app.route('/careers')
def careers():
    return render_template('careers.html')


@app.route('/thermosolver/')
def thermosolver():
    return render_template('thermosolver.html')


@app.route('/stressmaster/')
def stressmaster():
    return render_template('stress master.html')


@app.route('/about-us')
def about_us():
    return render_template('about_us.html')


@app.route('/product')
def product():
    return render_template('product.html')


@app.route('/mechai')
def mechai():
    return render_template('mech-ai.html')


@app.route('/fluid-flow')
def fluid_flow():
    return render_template('fluid_flow_ai.html')

@app.route('/security/')
def security():
    return render_template('security.html')
@app.route('/design_master/')
def design_master():
    return render_template('design_master.html')

@app.route('/resources/')
def resources():
    return render_template('resources.html')
@app.route('/manufacturing-twin')
def manufactring_twin():
    return render_template('manufactaring_ai.html')


@app.route('/robopilot-ai')
def robopilot_ai():
    return render_template('robopilot_ai.html')


@app.route('/mat-si')
def mat_si():
    return render_template('mat_si.html')

@app.route('/demo/')
def demo():
    return render_template('demo.html')


@app.route('/submit_demo', methods=['POST'])
def submit_demo():
    name = request.form.get('name')
    email = request.form.get('email')
    product = request.form.get('product')
    company_size = request.form.get('company_size')
    source = request.form.get('source')
    message = request.form.get('message')

    # For now, just return a success message
    # In a real application, you would store this data in a database
    return f"""
    <div style="font-family: Arial, sans-serif; padding: 2rem;">
        <h1>Thank you, {name}!</h1>
        <p>We have received your request for a demo of <strong>{product}</strong> and will get back to you at {email} shortly.</p>
        <p>Your company size: {company_size}</p>
        <p>You heard about us from: {source}</p>
        <p>Your message: "{message}"</p>
    </div>
    """


if __name__ == '__main__':
    app.run(debug=True)


