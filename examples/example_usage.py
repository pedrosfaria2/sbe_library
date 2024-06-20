from sbe.schema import SBESchema
from sbe.message import SBEMessage
from sbe.decoder import SBEDecoder
from sbe.utils import PCAPReader

# Load the schema
schema = SBESchema('path/to/your-schema.xml')
message = SBEMessage(schema, "YourMessage")

# Initialize the decoder
decoder = SBEDecoder()
binary_data = b'\x00\x00\x00\x2A\x00\x00\x00\x7B'
decoded_data = decoder.decode(message, binary_data)
print(decoded_data)

# Read the PCAP
pcap_reader = PCAPReader('path/to/your-pcap-file.pcap')
sbe_messages = pcap_reader.get_sbe_messages()

# Decode the SBE messages
for binary_data in sbe_messages:
    decoded_data = decoder.decode(message, binary_data)
    print(decoded_data)
