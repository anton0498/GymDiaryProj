from django.contrib import admin
from django.http import JsonResponse
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


def health(_request):
    return JsonResponse({"status": "ok"})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me(request):
    return Response({"id": request.user.id, "username": request.user.username})



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", health),
    
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema")),

    path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("api/auth/me/", me, name="auth_me"),


]
