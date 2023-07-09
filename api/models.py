from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    online = models.BooleanField(default=False)
    last_seen = models.DateTimeField(null=True, blank=True)
    friends = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='user_friends')
    blocked_users = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='user_blocked_users')

class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    recipient_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)

    class Conversation(models.Model):
        participants = models.ManyToManyField('CustomUser')
        latest_message = models.ForeignKey('Message', on_delete=models.SET_NULL, null=True)