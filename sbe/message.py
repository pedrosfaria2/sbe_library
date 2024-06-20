class SBEMessage:
    def __init__(self, schema, message_id):
        self.schema = schema
        self.message_id = message_id
        self.fields = self.get_fields_by_id(message_id)

    def get_fields_by_id(self, message_id):
        for message in self.schema.root.findall(".//{http://fixprotocol.io/2016/sbe}message"):
            if int(message.get("id")) == message_id:
                return self.schema.parse_fields(message)
        raise ValueError(f"Unknown message ID: {message_id}")
