from flask import Flask, render_template_string, request
import random, time

app = Flask(__name__)

# Simulated model filename
trained_model_name = f"rf_model_simulated_{random.randint(1000, 9999)}.pkl"

# Global variable to hold the analysis data
analysis_data = None

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>PCAP Anomaly Dashboard</title>
    <style>
        body {
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            color: #fff;
        }
        .background {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background:Url('/static/asdf.jpeg') no-repeat center center fixed;
            background-size: cover;
            filter: blur(5px);
            z-index: -1;
        }
        .overlay {
            background-color: rgba(0, 0, 0, 0.85);
            min-height: 100vh;
            padding: 40px;
        }
        .dashboard {
            max-width: 1100px;
            margin: auto;
            background: rgba(255, 255, 255, 0.05);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 0 20px #00f2ff;
        }
        h1 {
            color: #00f2ff;
            text-align: center;
            margin-bottom: 10px;
        }
        .btn {
            display: block;
            margin: 30px auto 20px;
            padding: 15px 40px;
            font-size: 18px;
            background: #00f2ff;
            color: #000;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s;
        }
        .btn:hover {
            background: #00cfe3;
        }
        .model-info {
            text-align: center;
            margin-bottom: 20px;
            font-weight: bold;
            font-size: 18px;
            color: #99ffcc;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 30px;
        }
        th, td {
            padding: 12px 15px;
            text-align: center;
            border-bottom: 1px solid #444;
        }
        th {
            background: #00f2ff;
            color: #000;
        }
        td {
            background: rgba(255, 255, 255, 0.05);
        }
        .malicious {
            color: red;
            font-weight: bold;
        }
        .benign {
            color: #00ff00;
            font-weight: bold;
        }
    </style>
</head>
<body>
<div class="background"></div>
<div class="overlay">
    <div class="dashboard">
        <h1>📡 PCAP Anomaly Detector Dashboard</h1>

        <form method="post" action="/train" enctype="multipart/form-data">
            <button class="btn" type="submit">🔄 Train Model</button>
        </form>

        <form method="post" action="/analyze" enctype="multipart/form-data"> 
            <button class="btn" type="submit">📊 Analyze Data</button>
        </form>

        {% if training_message %}
            <div class="model-info">{{ training_message }}</div>
        {% endif %}

        {% if analysis %}
            <div class="model-info">✅ Using Model: {{ model_name }} | Showing 100 Anomalies</div>
            <table>
                <tr>
                    <th>Packet ID</th>
                    <th>Status</th>
                    <th>Confidence</th>
                </tr>
                {% for row in analysis %}
                <tr>
                    <td>{{ row[0] }}</td>
                    <td class="{{ 'malicious' if row[1] == 'Malicious' else 'benign' }}">{{ row[1] }}</td>
                    <td>{{ row[2] }}%</td>
                </tr>
                {% endfor %}
            </table>
        {% endif %}
    </div>
</div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/train', methods=['POST'])
def train():
    time.sleep(5)  # Simulate training

    global trained_model_name
    trained_model_name = f"rf_model_simulated_{random.randint(1000, 9999)}.pkl"
    training_message = f"✅ Model trained successfully! Model name: {trained_model_name}"

    return render_template_string(HTML, training_message=training_message, model_name=trained_model_name)

@app.route('/analyze', methods=['POST'])
def analyze():
    time.sleep(5)  # Simulate analysis

    global analysis_data
    data = []
    for i in range(1, 101):
        label = random.choices(['Benign', 'Malicious'], weights=(70, 30))[0]
        confidence = random.randint(80, 99) if label == 'Benign' else random.randint(90, 100)
        data.append((f"Pkt-{random.randint(100000,999999)}", label, confidence))

    random.shuffle(data)
    analysis_data = data
    return render_template_string(HTML, analysis=analysis_data, model_name=trained_model_name)

if __name__ == '__main__':
    app.run(debug=True)
