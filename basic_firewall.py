import socket
import struct

def create_socket():
    try:
        # Create a raw socket
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        print("Socket created successfully")
        return s
    except Exception as e:
        print(f"Error creating socket: {e}")
        return None
    
def packet_filter(packet):
    # Unpack the IP header
    ip_header = packet[0:20]
    ip_fields = struct.unpack('!BBHHHBBH4s4s', ip_header)

    #Get the source IP address
    source_ip = socket.inet_ntoa(ip_fields[8])

    #Define a block list
    block_list = [''] #add IP's to list

    if source_ip in block_list:
        print(f"Blocked packet from {source_ip}")
        return False
    else:
        print(f"Allowed packet from {source_ip}")

    def capture_packets(s):
        while True:
            # Recieve packets
            packet = s.recvfrom(65565) [0]

            # Apply packet filtering

            if packet_filter(packet):
                #add code to process allowed packets
                pass

    def main():
        s = creat_socket()
        if s:
            capture_packets(s)
    
    if __name__ == "__main__":
        main()

# implement logging
# create dynamic rules
# create GUI
# extend support to UDP and ICMP