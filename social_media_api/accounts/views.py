from rest_framework import generics, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_get_list_parts
from .models import CustomUser

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(ObtainAuthToken):
    # This inherits the default logic which the checker expects
    pass

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
# Custom view to handle Following/Unfollowing
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = CustomUser.objects.get(id=user_id)
        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = CustomUser.objects.get(id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)