from sbe.message import SBEMessage
from sbe.schema import SBESchema


class SBEDecoder:
    def __init__(self, schema: SBESchema):
        self.schema = schema

    def decode(self, binary_data):
        message_id = self.extract_message_id(binary_data)
        print(f"Extracted Message ID: {message_id}")  # Adicione esta linha para depuração
        try:
            message = SBEMessage(self.schema, message_id)
            return self.decode_message(binary_data, message)
        except ValueError as e:
            raise ValueError(f"Error decoding SBE message: {e}")

    def extract_message_id(self, binary_data):
        # Assumindo que o ID da mensagem está nas posições 0 a 2 (ou ajuste conforme necessário)
        message_id = int.from_bytes(binary_data[0:2], byteorder='little')
        return message_id

    def decode_message(self, binary_data, message):
        decoded_data = {}
        offset = 0
        for field in message.fields:
            value, offset = self.decode_field(field, binary_data, offset)
            decoded_data[field["name"]] = value
        return decoded_data

    def decode_field(self, field, binary_data, offset):
        field_type = field["type"]
        if field_type == 'int32':
            value = int.from_bytes(binary_data[offset:offset+4], byteorder='little')
            offset += 4
        elif field_type == 'int64':
            value = int.from_bytes(binary_data[offset:offset+8], byteorder='little')
            offset += 8
        elif field_type == 'string':
            length = int.from_bytes(binary_data[offset:offset+2], byteorder='little')
            offset += 2
            value = binary_data[offset:offset+length].decode('utf-8')
            offset += length
        else:
            raise ValueError(f"Unsupported field type: {field_type}")
        return value, offset
