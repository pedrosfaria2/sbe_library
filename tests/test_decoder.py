import unittest
from sbe.schema import SBESchema
from sbe.message import SBEMessage
from sbe.decoder import SBEDecoder


class TestSBEDecoder(unittest.TestCase):
    def test_decode(self):
        schema = SBESchema("path/to/your-schema.xml")
        message = SBEMessage(schema, "YourMessage")
        decoder = SBEDecoder()
        binary_data = b'\x00\x00\x00\x2A\x00\x00\x00\x7B'
        decoded_data = decoder.decode(message, binary_data)
        expected_data = {"field1": 42, "field2": 123}
        self.assertEqual(decoded_data, expected_data)


if __name__ == '__main__':
    unittest.main()
