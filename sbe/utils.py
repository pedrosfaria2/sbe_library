from scapy.all import rdpcap


class PCAPReader:
    def __init__(self, pcap_file):
        self.pcap_file = pcap_file

    def get_sbe_messages(self):
        packets = rdpcap(self.pcap_file)
        sbe_messages = []
        for packet in packets:
            if packet.haslayer('Raw'):
                sbe_messages.append(bytes(packet['Raw'].load))
        return sbe_messages
