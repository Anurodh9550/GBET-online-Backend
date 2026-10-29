from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.throttling import ScopedRateThrottle

from .models import Enquiry
from .serializers import EnquiryCreateSerializer, EnquirySerializer


class EnquiryViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Enquiry.objects.all()
    http_method_names = ["get", "post", "patch", "head", "options"]
    throttle_scope = "enquiry"

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAdminUser()]

    def get_throttles(self):
        if self.action == "create":
            return [ScopedRateThrottle()]
        return []

    def get_serializer_class(self):
        if self.action == "create":
            return EnquiryCreateSerializer
        return EnquirySerializer
