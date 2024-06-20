import xml.etree.ElementTree as ET


class SBESchema:
    def __init__(self, xml_path):
        self.tree = ET.parse(xml_path)
        self.root = self.tree.getroot()
        self.messages = self.parse_messages()

    def parse_messages(self):
        messages = {}
        for message in self.root.findall(".//{http://fixprotocol.io/2016/sbe}message"):
            message_name = message.get("name")
            message_id = int(message.get("id"))
            fields = self.parse_fields(message)
            messages[message_id] = {"name": message_name, "fields": fields}
        return messages

    def parse_fields(self, message):
        fields = []
        for field in message.findall(".//{http://fixprotocol.io/2016/sbe}field"):
            field_info = {
                "name": field.get("name"),
                "type": field.get("type"),
                "offset": int(field.get("offset", 0)),
                "length": int(field.get("length", 0)),
            }
            fields.append(field_info)
        return fields

    def get_message_by_id(self, message_id):
        return self.messages.get(message_id, None)


def print_available_messages(schema):
    print("Available messages in the schema:")
    for message_id, message_info in schema.messages.items():
        print(f"ID: {message_id}, Name: {message_info['name']}")
