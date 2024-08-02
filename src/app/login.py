userA= "user@gmail.com"
passwordA = "1234"

email=""
password=""
loginStatus=False

def login():
    try:
        # Get the JSON request data
        request_data = request.get_json()

        # Extract email, password, and userId from the request
        email = request_data.get('email')
        password = request_data.get('password')
        user_id = request_data.get('userId')

        # Define valid credentials and expected userId
        valid_email = 'jess@example.com'
        valid_password = 'securepassword'
        expected_user_id = 'jess123'  # Example userId

        # Check the credentials and userId
        if email == valid_email and password == valid_password and user_id == expected_user_id:
            return jsonify({
                'userid': user_id,
                'email': valid_email,
                'name': 'Jess'
            })
        else:
            return jsonify({
                'loginStatus': 'failed',
                'message': 'Invalid email, password, or userId'
            }), 401  # HTTP 401 Unauthorized

    except Exception as e:
        return jsonify({
            'loginStatus': 'error',
            'message': str(e)
        }), 400  # HTTP 400 Bad Request
    