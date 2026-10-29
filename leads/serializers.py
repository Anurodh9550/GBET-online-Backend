import re

from rest_framework import serializers

from .models import Enquiry

MOBILE = re.compile(r"^[6-9]\d{9}$")


class EnquiryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = ["full_name", "mobile", "email", "state", "city", "course", "message", "source"]

    def validate_full_name(self, value):
        value = " ".join(value.split())
        if len(value) < 2:
            raise serializers.ValidationError("Enter the full name.")
        return value

    def validate_mobile(self, value):
        if not MOBILE.fullmatch(value):
            raise serializers.ValidationError("Enter a 10-digit mobile number.")
        return value

    def validate_city(self, value):
        value = value.strip()
        if len(value) < 2:
            raise serializers.ValidationError("Enter the city.")
        return value

    def validate_state(self, value):
        value = value.strip()
        if len(value) < 2:
            raise serializers.ValidationError("Enter the state.")
        return value

    def validate_course(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Choose a course.")
        return value


class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = [
            "id",
            "full_name",
            "mobile",
            "email",
            "state",
            "city",
            "course",
            "message",
            "source",
            "status",
            "note",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "full_name",
            "mobile",
            "email",
            "state",
            "city",
            "course",
            "message",
            "source",
            "created_at",
            "updated_at",
        ]
