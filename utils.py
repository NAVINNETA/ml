import pandas as pd
from scapy.all import rdpcap

def extract_features_from_pcap(filepath):
    packets = rdpcap(filepath)
    features = []

    for pkt in packets:
        try:
            feature = {
                'packet_len': len(pkt),
                'has_TCP': 1 if pkt.haslayer('TCP') else 0,
                'has_UDP': 1 if pkt.haslayer('UDP') else 0,
                'has_ICMP': 1 if pkt.haslayer('ICMP') else 0,
                'src_port': pkt.sport if hasattr(pkt, 'sport') else 0,
                'dst_port': pkt.dport if hasattr(pkt, 'dport') else 0,
            }
            features.append(feature)
        except:
            continue

    return pd.DataFrame(features)
