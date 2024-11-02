from django.test import TestCase
from django.contrib.auth.models import User
from .models import Course, UserCourse, Admin
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse


class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Test Course",
            description="This is a test course.",
            image=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
            video_url="http://example.com/video"
        )

    def test_course_creation(self):
        """Test that a course can be created successfully."""
        self.assertEqual(self.course.title, "Test Course")
        self.assertEqual(self.course.description, "This is a test course.")
        self.assertEqual(self.course.video_url, "http://example.com/video")
        self.assertTrue(self.course.image)

    def test_course_str(self):
        """Test the string representation of the course."""
        self.assertEqual(str(self.course), "Test Course")


class UserCourseModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.course = Course.objects.create(
            title="Test Course",
            description="This is a test course."
        )
        self.user_course = UserCourse.objects.create(
            course=self.course,
            user=self.user,
            done=False
        )

    def test_user_course_creation(self):
        """Test that a user can be enrolled in a course successfully."""
        self.assertEqual(self.user_course.user.username, "testuser")
        self.assertEqual(self.user_course.course.title, "Test Course")
        self.assertFalse(self.user_course.done)

    def test_user_course_unique_constraint(self):
        """Test that the unique constraint on user and course works."""
        with self.assertRaises(Exception):
            UserCourse.objects.create(user=self.user, course=self.course)

    def test_user_course_str(self):
        """Test the string representation of the UserCourse."""
        self.assertEqual(str(self.user_course), "testuser enrolled in Test Course")


class AdminModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='adminuser', password='12345')
        self.admin = Admin.objects.create(user=self.user)

    def test_admin_creation(self):
        """Test that an admin user can be created successfully."""
        self.assertEqual(self.admin.user.username, 'adminuser')

    def test_admin_str(self):
        """Test the string representation of the Admin."""
        self.assertEqual(str(self.admin), "adminuser")
