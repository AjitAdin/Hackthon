from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/wearos', methods=['POST'])  
def wearos():
    
    data = request.data.decode('utf-8')
    print(data)

    
    return jsonify({"message": "Data received", "data": data}), 200

if _name_ == '_main_':
    app.run(debug=True, host='10.100.51.249', port=5000)