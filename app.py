from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/execute-script')
def execute_script():
    try:
        # Execute main.py script using subprocess
        result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)
        return result
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
