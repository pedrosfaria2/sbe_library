from scapy.all import rdpcap


class PCAPReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_sbe_messages(self):
        packets = rdpcap(self.file_path)
        sbe_messages = []
        for packet in packets:
            if hasattr(packet, 'load'):
                sbe_messages.append(packet.load)
        return sbe_messages
