import unittest
from context import Message


class TestMessage(unittest.TestCase):
    def setUp(self):
        # Secret Message has Kingdom's emblem
        self.msg1, self.emblem1 = 'ROZO', 'OWL'
        self.msg_obj1 = Message(self.msg1, self.emblem1)
        self.decrypted_msg_with_emblem = 'OLWL'
        # Secret Message deosen't have Kingdom's emblem
        self.msg2, self.emblem2 = 'FAIJWJSOOFAMAU', 'PANDA'
        self.msg_obj2 = Message(self.msg2, self.emblem2)
        self.decrypted_msg_without_emblem = 'AVDERENJJAVHVP'

    def test_secret_message_has_expected_return_value(self):
        decrypted_message = self.msg_obj1.decrypt_message_with_key()
        assert decrypted_message == 'OLWL'
        self.assertIsInstance(decrypted_message, str)
        decrypted_message = self.msg_obj2.decrypt_message_with_key()
        assert decrypted_message == 'AVDERENJJAVHVP'
        self.assertIsInstance(decrypted_message, str)

    def test_secret_message_has_emblem(self):
        verification_status = self.msg_obj1.verify_message(
            self.decrypted_msg_with_emblem)
        self.assertIsInstance(verification_status, bool)
        self.assertTrue(verification_status)

    def test_secret_message_does_not_have_emblem(self):
        verification_status = self.msg_obj2.verify_message(
            self.decrypted_msg_without_emblem)
        self.assertIsInstance(verification_status, bool)
        self.assertTrue(verification_status)


if __name__ == '__main__':
    unittest.main()