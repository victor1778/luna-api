from django.test import TestCase
from channels import TestClient
from .models import CustomUser, Message
import json

class ChatConsumerTest(TestCase):
    def test_chat_message(self):
        # Create two users
        vrfvega = CustomUser.objects.create_user(username='vrfvega')
        testuser = CustomUser.objects.create_user(username='testuser')

        # Connect to the WebSocket
        client = TestClient(
            '/ws/chat/vrfvega/testuser',
            user=vrfvega
        )

        # Send a message
        client.send_text('{"message": "Hello, testuser!"}')

        # Receive the message
        response = client.receive()
        data = json.loads(response)

        # Assert that the message was received
        self.assertEqual(data['message'], 'Hello, testuser!')
        self.assertEqual(data['sender_username'], 'vrfvega')
        self.assertEqual(data['recipient_username'], 'testuser')

        # Assert that the message was saved to the database
        message = Message.objects.get(sender_id=vrfvega.id, recipient_id=testuser.id)
        self.assertEqual(message.content, 'Hello, testuser!')






