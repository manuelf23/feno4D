import subprocess

def save_packets(fname, nPackets, interface):
    """[summary]

    Args:
        fname (string): File name for saving the packets (without extension).
        nPackets (integer): Number of packets to be recived.
        interface (string): Network interface for reciving the packets.

    Returns:
        [integer]: [Code 0: Packest were not saved correctly
                    Code 1: Packest were saved correctly
                    Code 2: The network interface does not exist]
    """
    process = subprocess.Popen(['tcpdump', '-c', str(nPackets * 100), '-w' , fname + '.pcap', '-i', interface],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()
    if '(No such device exists)' in str(stderr):
        return 2 # The network interface does not exist
    rPackets = int(str(stderr).split('\\n')[1].split(' ')[0])
    if rPackets == nPackets * 100:
        return 1 # Packest were saved correctly
    else:
        return 0 # Packest were not saved correctly
