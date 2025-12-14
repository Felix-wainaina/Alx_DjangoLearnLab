from rest_framework import generics, permissions
from .models import Notification
from rest_framework.response import Response

class NotificationListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.notifications.all().order_by('-timestamp')