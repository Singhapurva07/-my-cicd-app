from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head><title>DevOps CI/CD Project</title></head>
    <body style="font-family: Arial; text-align: center; background: #f0f8ff; padding: 50px;">
        <h1 style="color: #2c3e50;">🚀 CI/CD Pipeline - DevOps Project</h1>
        <h2 style="color: #27ae60;">✅ Successfully Deployed on Kubernetes!</h2>
        <hr>
        <p style="font-size: 18px;"><b>Student Name:</b> Apurva Singh</p>
        <p style="font-size: 18px;"><b>Project:</b> Dockerized App Deployment using Jenkins & Kubernetes</p>
        <p style="font-size: 18px;"><b>Tools Used:</b> Jenkins | Docker | Kubernetes | AWS EC2 | GitHub</p>
        <hr>
        <h3 style="color: #2980b9;">Pipeline Stages:</h3>
        <p>✅ Code Checkout from GitHub</p>
        <p>✅ Docker Image Build</p>
        <p>✅ Push to DockerHub</p>
        <p>✅ Deploy to Kubernetes Cluster</p>
        <hr>
        <p style="color: gray;">Deployed via Jenkins CI/CD Pipeline on AWS EC2</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)