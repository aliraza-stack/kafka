from producer.kafka_producer import send_message
from consumer.kafka_consumer import register_consumer, otp_validation_consumer
from database.mongodb import store_user_data, find_user_by_email
from utils.email_sender import send_email

# Kafka topics
REGISTRATION_TOPIC = 'registration'
OTP_VALIDATION_TOPIC = 'otp_validation'

# Main registration and OTP validation logic
def register_user(email):
    # Generate OTP
    otp = generate_otp()

    # Store user data in MongoDB
    user_data = {'email': email, 'otp': otp}
    store_user_data(user_data)

    # Send registration message to Kafka
    send_message(REGISTRATION_TOPIC, {'email': email, 'otp': otp})

def validate_otp(email, otp):
    # Find user in MongoDB
    user = find_user_by_email(email)

    if user and user['otp'] == otp:
        # Send OTP validation message to Kafka
        send_message(OTP_VALIDATION_TOPIC, {'email': email, 'status': 'valid'})
    else:
        send_message(OTP_VALIDATION_TOPIC, {'email': email, 'status': 'invalid'})

# Implement your OTP generation logic here
def generate_otp():
    # Generate a random OTP
    return '123456'

# Main execution
if __name__ == "__main__":
    # Example usage
    email = 'aliraxayasin@gmail.com'

    # Register a user
    register_user(email)

    # Simulate OTP validation
    received_otp = '123456'  # Replace with the actual OTP received from the user
    validate_otp(email, received_otp)

    # Consume Kafka messages (use threads or async tasks as needed)
    register_consumer()
    otp_validation_consumer()
