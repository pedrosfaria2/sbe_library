import xml.etree.ElementTree as ET


class SBESchema:
    def __init__(self, xml_path):
        self.tree = ET.parse(xml_path)
        self.root = self.tree.getroot()
        self.messages = self.parse_messages()

    def parse_messages(self):
        messages = {}
        for message in self.root.findall('message'):
            message_name = message.get('name')
            fields = self.parse_fields(message)
            messages[message_name] = fields
        return messages

    def parse_fields(self, message):
        fields = []
        for field in message.findall(".//field"):
            field_info = {
                'name': field.get("name"),
                'type': field.get("type"),
                'offset': field.get("offset"),
                'length': field.get("length"),
            }
            fields.append(field_info)
        return fields
