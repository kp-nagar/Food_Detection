from app import app

if __name__ == "__main__":
    print("Starting Python Flask Server For snacks Image Classification")
    app.run(host='0.0.0.0', port=5000, debug=True)