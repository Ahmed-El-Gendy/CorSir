from django.test import TestCase
from django.contrib.auth.models import User
from .models import Course, UserCourse, Admin


class CourseModelTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title='Test Course',
            description='This is a test course.',
        )

    def test_course_creation(self):
        """Test if a Course instance is created correctly."""
        self.assertEqual(self.course.title, 'Test Course')
        self.assertIsNotNone(self.course.created_at)
        self.assertEqual(str(self.course), 'Test Course')

    def test_course_description(self):
        """Test that the course description is stored correctly."""
        self.assertEqual(self.course.description, 'This is a test course.')


    def test_course_video_url_field(self):
        """Test that the video URL field can be blank."""
        self.assertIsNone(self.course.video_url)

    def test_course_unique_title(self):
        """Test that courses with the same title cannot be created."""
        with self.assertRaises(Exception):
            Course.objects.create(title='Test Course', description='Another description.')

    def test_course_string_representation(self):
        """Test the string representation of the Course."""
        self.assertEqual(str(self.course), 'Test Course')

    def test_course_created_at_is_auto_now_add(self):
        """Test that created_at is set automatically on creation."""
        self.assertIsNotNone(self.course.created_at)


    def test_course_has_video_url(self):
        """Test that a course can store a video URL."""
        self.course.video_url = 'http://example.com/video'
        self.course.save()
        self.assertEqual(self.course.video_url, 'http://example.com/video')


class UserCourseModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.course = Course.objects.create(title='Test Course', description='This is a test course.')
        self.user_course = UserCourse.objects.create(course=self.course, user=self.user)

    def test_user_course_creation(self):
        """Test if a UserCourse instance is created correctly."""
        self.assertEqual(self.user_course.user.username, 'testuser')
        self.assertEqual(self.user_course.course.title, 'Test Course')
        self.assertIsNotNone(self.user_course.created_at)
        self.assertFalse(self.user_course.done)

    def test_user_course_done_field_default(self):
        """Test that the done field defaults to False."""
        self.assertFalse(self.user_course.done)

    def test_user_course_string_representation(self):
        """Test the string representation of the UserCourse."""
        self.assertEqual(str(self.user_course), 'testuser enrolled in Test Course')

    def test_user_course_unique_constraint(self):
        """Test that the unique constraint for user-course combinations works."""
        with self.assertRaises(Exception):
            UserCourse.objects.create(course=self.course, user=self.user)

    def test_user_course_created_at_is_auto_now_add(self):
        """Test that created_at is set automatically on creation."""
        self.assertIsNotNone(self.user_course.created_at)

    def test_user_course_retrieve_user(self):
        """Test retrieving the user from UserCourse."""
        self.assertEqual(self.user_course.user.username, 'testuser')

    def test_user_course_retrieve_course(self):
        """Test retrieving the course from UserCourse."""
        self.assertEqual(self.user_course.course.title, 'Test Course')

    def test_user_course_done_field_change(self):
        """Test that the done field can be changed."""
        self.user_course.done = True
        self.user_course.save()
        self.assertTrue(self.user_course.done)

    def test_user_course_delete_cascade(self):
        """Test that deleting a user will affect related UserCourses."""
        user = self.user_course.user
        self.user_course.delete()
        self.assertFalse(UserCourse.objects.filter(user=user).exists())

    def test_user_course_delete_course_cascade(self):
        """Test that deleting a course will affect related UserCourses."""
        course = self.user_course.course
        self.user_course.delete()
        self.assertFalse(UserCourse.objects.filter(course=course).exists())


class AdminModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='adminuser', password='12345')
        self.admin = Admin.objects.create(user=self.user)

    def test_admin_creation(self):
        """Test if an Admin instance is created correctly."""
        self.assertEqual(self.admin.user.username, 'adminuser')
        self.assertEqual(str(self.admin), 'adminuser')

    def test_admin_user_relationship(self):
        """Test that the admin is linked to the correct user."""
        self.assertEqual(self.admin.user, self.user)

    def test_admin_string_representation(self):
        """Test the string representation of the Admin."""
        self.assertEqual(str(self.admin), 'adminuser')

    def test_admin_user_delete_cascade(self):
        """Test that deleting a user will also delete the related Admin."""
        user = self.admin.user
        self.admin.delete()
        self.assertFalse(Admin.objects.filter(user=user).exists())

    def test_admin_user_one_to_one_relationship(self):
        """Test that the admin can only be linked to one user."""
        with self.assertRaises(Exception):
            User.objects.create_user(username='adminuser2', password='12345')
            Admin.objects.create(user=self.user)

    def test_admin_creation_with_non_user(self):
        """Test that creating an Admin with a non-existent user raises an error."""
        with self.assertRaises(Exception):
            Admin.objects.create(user=None)

    def test_admin_retrieve_user(self):
        """Test retrieving the user from Admin."""
        self.assertEqual(self.admin.user.username, 'adminuser')

    def test_admin_delete_effects_on_user(self):
        """Test that deleting an admin does not delete the user."""
        user = self.admin.user
        self.admin.delete()
        self.assertTrue(User.objects.filter(username='adminuser').exists())

    def test_admin_multiple_admins_for_users(self):
        """Test that different users can have their own admin instance."""
        user2 = User.objects.create_user(username='adminuser2', password='12345')
        admin2 = Admin.objects.create(user=user2)
        self.assertNotEqual(self.admin.user, admin2.user)
