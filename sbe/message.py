class SBEMessage:
    def __init__(self, schema, message_name):
        self.schema = schema
        self.message_name = message_name
        self.fields = schema.messages[message_name]
