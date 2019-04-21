from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User
# from messaging.models import < Your models > 

# Tests for 'channels' route
class ChannelTestCase(TestCase):
    # Runs before every test
    def setUp(self):
        user1 = User.objects.create_user(username="Test1",
                                 email="a@uw.edu",
                                 password="testpassword1",
                                 first_name="Fname1",
                                 last_name="Lname1")
        user1.save()
        user2 = User.objects.create_user(username="Test2",
                                 email="b@uw.edu",
                                 password="testpassword2",
                                 first_name="Fname2",
                                 last_name="Lname2")
        user2.save()

    # This test is implemented for you as an example.
    def test_get_all_channels_when_only_general_exists(self):
        # Create a client to talk to the server
        c = Client()
        
        # After you call this method, the test client will have all the cookies and session data required to pass any login-based tests that may form part of a view.
        c.login(username='Test1', password='testpassword1')
        response = c.get('/messaging/channels', secure=True)

        # Check status code
        self.assertEqual(response.status_code, 200)

        # Check name of general channel
        self.assertEqual("general", response.json()[0]['name'])

        # Checking number of elements in JSON array
        self.assertEqual(1, len(response.json()))

        # Alternatively, check that getting the second element
        # raises an error:
        with self.assertRaises(IndexError):
            response.json()[1]

    # Tests that multiple channels can be returned
    # from the server.
    # def test_get_all_channels_when_multiple_exist(self):

    # Tests that channels with the same name
    # cannot exist and will not be allowed to be created.
    # def test_cannot_create_duplicate_channel(self):

    # Tests that all channel endpoints are only viewable when 
    # the client is authenticated. Expects the status code 401
    # for all unauthorized requests to the endpoint for all implemented
    # HTTP methods.
    # def test_channel_endpoints_viewable_only_when_authenticated(self):

    # Tests that users can create private channels.
    # def test_users_can_create_private_channel(self):
    

# Tests for 'channels/<int:channel_id>' route
class SpecificChannelTestCase(TestCase):
    # Runs before every test
    def setUp(self):
        user1 = User.objects.create_user(username="Test1",
                                 email="a@uw.edu",
                                 password="testpassword1",
                                 first_name="Fname1",
                                 last_name="Lname1")
        user1.save()
        user2 = User.objects.create_user(username="Test2",
                                 email="b@uw.edu",
                                 password="testpassword2",
                                 first_name="Fname2",
                                 last_name="Lname2")
        user2.save()

    # Tests that all specific channel endpoints are only viewable when 
    # the client is authenticated. Expects the status code 401
    # for all unauthorized requests to the endpoint for all implemented
    # HTTP methods.
    # def test_specific_channel_endpoints_viewable_only_when_authenticated(self):

    # Tests that the creator, and ONLY the creator,
    # of a private channel can update the name and description
    # of the channel.
    # def test_creator_can_update_private_channel(self):

    # Tests that the creator, and ONLY the creator,
    # of a private channel can delete the channel.
    # def test_creator_can_delete_private_channel(self):

    # Tests that only members of a private channel can 
    # view messages in it.
    # def test_only_members_can_view_private_channels(self):


# Tests for 'channels/<int:channel_id>/members' route
class SpecificChannelMembersTestCase(TestCase):
    # Runs before every test
    def setUp(self):
        user1 = User.objects.create_user(username="Test1",
                                 email="a@uw.edu",
                                 password="testpassword1",
                                 first_name="Fname1",
                                 last_name="Lname1")
        user1.save()
        user2 = User.objects.create_user(username="Test2",
                                 email="b@uw.edu",
                                 password="testpassword2",
                                 first_name="Fname2",
                                 last_name="Lname2")
        user2.save()

    # Tests that only the creator of a private channel can add
    # members to it.
    # def test_only_private_channel_creator_can_add_members(self):

    # Tests that only the creator of a private channel can remove
    # members from it.
    # def test_only_channel_creator_can_remove_members(self):
    

# Tests for 'messages/<int:message_id>' route
class SpecificMessageTestCase(TestCase):
    # Runs before every test
    def setUp(self):
        user1 = User.objects.create_user(username="Test1",
                                 email="a@uw.edu",
                                 password="testpassword1",
                                 first_name="Fname1",
                                 last_name="Lname1")
        user1.save()
        user2 = User.objects.create_user(username="Test2",
                                 email="b@uw.edu",
                                 password="testpassword2",
                                 first_name="Fname2",
                                 last_name="Lname2")
        user2.save()


    # Tests that the creator, and ONLY the creator, can 
    # update their own message.
    # def test_user_can_update_own_message(self):

    # Tests that the creator, and ONLY the creator, can 
    # delete their own message.
    # def test_user_can_delete_own_messages(self):