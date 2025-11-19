from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# --- MODIFICATION: Define DB name as a constant ---
DATABASE = 'database.db'

# --- MODIFICATION: Add the init_db() function ---
def init_db():
    """Initializes the database and creates the 'requests' table if it doesn't exist."""
    print("Attempting to initialize database...")
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # SQL command to create the table
        # 'IF NOT EXISTS' prevents an error if the table already exists.
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            product TEXT,
            message TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        conn.commit()
        conn.close()
        print(f"Database '{DATABASE}' initialized successfully.")
    except Exception as e:
        print(f"Error initializing database: {e}")


# Home route
@app.route('/')
def home():
    """View for the home page."""
    return render_template('home.html')


# Get material data API
@app.route('/api/material_data')
def material_data():
    data = {
        "material": "Steel",
        "properties": {
            "density": "7.85 g/cm^3",
            "yield_strength": "250 MPa",
            "tensile_strength": "400-550 MPa"
        }
    }
    return jsonify(data)


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

# Additional routes to match links used in templates (underscored/dashed variants)
@app.route('/mech-ai/')
def mech_ai_alt():
    return render_template('mech-ai.html')

@app.route('/fluid_flow_ai/')
def fluid_flow_ai_alt():
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

@app.route('/manufactaring_twin/')
def manufactring_twin_alt():
    return render_template('manufactaring_ai.html')


@app.route('/robopilot-ai')
def robopilot_ai():
    return render_template('robopilot_ai.html')

@app.route('/robopilot_ai/')
def robopilot_ai_alt():
    return render_template('robopilot_ai.html')


@app.route('/mat-si')
def mat_si():
    return render_template('mat_si.html')

@app.route('/mat_si/')
def mat_si_alt():
    return render_template('mat_si.html')

@app.route('/enginetune/')
def enginetune():
    return render_template('enginetune.html')

@app.route('/mesh-mind/')
def mesh_mind():
    return render_template('mesh-mind.html')

@app.route('/demo/')
def demo():
    return render_template('demo.html')


@app.route('/submit_demo', methods=['POST'])
def submit_demo():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    product = data.get('product')
    message = data.get('message')

    # --- MODIFICATION: Use DATABASE constant ---
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO requests (name, email, product, message) VALUES (?, ?, ?, ?)",
                   (name, email, product, message))
    conn.commit()
    conn.close()

    return jsonify(success=True)


@app.route('/view_requests')
def view_requests():
    # --- MODIFICATION: Use DATABASE constant ---
    conn = sqlite3.connect(DATABASE)
    # return rows as dict-like objects
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, product, message FROM requests ORDER BY id DESC")
    rows = cursor.fetchall()
    # convert to list of dicts for template safety
    requests_list = [dict(r) for r in rows]
    conn.close()
    return render_template('requests.html', requests=requests_list)


if __name__ == '__main__':
    # --- MODIFICATION: Call init_db() before running the app ---
    init_db()
    app.run(debug=True)