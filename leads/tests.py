from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Enquiry


class EnquiryApiTests(APITestCase):
    def setUp(self):
        user = get_user_model().objects.create_superuser("desk", "desk@gbte.in", "test-pass-123")
        self.token = Token.objects.create(user=user)

    def payload(self, **extra):
        data = {
            "full_name": "Riya Sharma",
            "mobile": "9876543210",
            "email": "riya@example.com",
            "state": "Uttar Pradesh",
            "city": "Noida",
            "course": "Diploma in Interior Design",
            "message": "Please call after 6",
            "source": "website",
        }
        data.update(extra)
        return data

    def test_public_can_create_but_not_list(self):
        created = self.client.post("/api/enquiries/", self.payload(), format="json")
        self.assertEqual(created.status_code, 201)
        self.assertEqual(Enquiry.objects.get().status, Enquiry.Status.NEW)
        denied = self.client.get("/api/enquiries/")
        self.assertEqual(denied.status_code, 401)

    def test_staff_can_list_and_update_status(self):
        self.client.post("/api/enquiries/", self.payload(source="brochure"), format="json")
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        listed = self.client.get("/api/enquiries/")
        self.assertEqual(listed.status_code, 200)
        enquiry_id = listed.data[0]["id"]
        patched = self.client.patch(
            f"/api/enquiries/{enquiry_id}/",
            {"status": "called", "note": "Rang once"},
            format="json",
        )
        self.assertEqual(patched.status_code, 200)
        self.assertEqual(patched.data["status"], "called")
        self.assertEqual(patched.data["note"], "Rang once")
        self.assertEqual(patched.data["source"], "brochure")

    def test_bad_mobile_is_rejected(self):
        created = self.client.post("/api/enquiries/", self.payload(mobile="12345"), format="json")
        self.assertEqual(created.status_code, 400)
        self.assertEqual(Enquiry.objects.count(), 0)
