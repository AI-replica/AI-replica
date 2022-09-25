import sys
import os

# TODO: find a better way to run custom bot from Rasa's "bot" folder
# Need to append path to the "ai_repilca" folder to be able to make imports from the modules in that folder
# ai_replica_dir_path = os.path.abspath(os.path.dirname(__file__) + "/..")
# sys.path.append(ai_replica_dir_path)

import unittest
from server.handlers.get_response import reduce_answer_content


class TestGetResponseMethods(unittest.TestCase):
    def test_test(self):
        self.assertEqual("foo", "foo")

    def test_reduce_answer_content1(self):
        res = reduce_answer_content("", {"type": "text", "content": "test content"})

        self.assertEqual(res, "test content")

    def test_reduce_answer_content2(self):
        res = reduce_answer_content(
            "acc content", {"type": "text", "content": "test content"}
        )

        self.assertEqual(res, "acc content; test content")

    def test_reduce_answer_content3(self):
        res = reduce_answer_content("", {"type": "image", "content": "test content"})

        self.assertEqual(res, "")


if __name__ == "__main__":
    unittest.main()
