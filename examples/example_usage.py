import sys
import os
from sbe.schema import SBESchema, print_available_messages
from sbe.decoder import SBEDecoder
from sbe.utils import PCAPReader

# Load the schema
schema_file = r'C:\Users\Pichau\Desktop\sbe_library\examples\b3-entrypoint-messages-8.1.1.xml'
schema = SBESchema(schema_file)

# Print available messages for debugging
print_available_messages(schema)

# Initialize the decoder with the schema
decoder = SBEDecoder(schema)

# Read the PCAP
try:
    pcap_reader = PCAPReader(r'C:\Users\Pichau\Desktop\sbe_library\examples\binary-gateway-entrypoint-8.1.0.pcap')
    sbe_messages = pcap_reader.get_sbe_messages()
    print(f"Read {len(sbe_messages)} messages from PCAP.")

    # Decode the SBE messages
    for binary_data in sbe_messages[:50]:  # Limite para os primeiros 5 para teste
        print(f"Binary data: {binary_data}")  # Adicione esta linha para depuração
        try:
            decoded_data = decoder.decode(binary_data)
            print(f"Decoded SBE message: {decoded_data}")
        except Exception as decode_error:
            print(f"Error decoding SBE message: {decode_error}")

except Exception as e:
    print(f"Error reading or decoding PCAP: {e}")
