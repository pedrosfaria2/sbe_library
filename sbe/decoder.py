import struct


class SBEDecoder:
    def decode(self, message, binary_data):
        data = {}
        for field in message.fields:
            offset = field["offset"]
            field_type = field["type"]
            field_name = field["name"]

            if field_type == "int32":
                value = struct.unpack_from(">i", binary_data, offset)[0]
            elif field_type == "uint32":
                value = struct.unpack_from(">I", binary_data, offset)[0]
            elif field_type == "char":
                length = field["length"]
                value = binary_data[offset:offset+length].decode("utf-8").strip()
            else:
                raise ValueError(f"Unknown field type: {field_type}")

            data[field_name] = value
        return data
