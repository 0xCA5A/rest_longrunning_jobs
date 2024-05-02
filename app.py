from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Dummy database to store running jobs
running_jobs = {}


@app.route('/jobs', methods=['POST'])
def start_job():
    data = request.json
    job_type = data.get('job_type')
    parameters = data.get('parameters')
    
    # Generate unique job ID
    job_id = str(uuid.uuid4())
    
    # Start the job (dummy implementation)
    running_jobs[job_id] = {
        'job_type': job_type,
        'parameters': parameters,
        'status': 'running',
        'progress': 0
    }
    
    return jsonify({'job_id': job_id}), 200


@app.route('/jobs', methods=['GET'])
def get_running_jobs():
    return jsonify(list(running_jobs.values())), 200


@app.route('/jobs/<job_id>', methods=['GET'])
def get_job_status(job_id):
    if job_id not in running_jobs:
        return jsonify({'error': 'Job not found'}), 404
    
    return jsonify(running_jobs[job_id]), 200


if __name__ == '__main__':
    app.run(debug=True)
