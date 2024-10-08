import csv

def parse_flow_logs(flow_log_file, lookup_table_file):
    lookup_table = {}
    with open(lookup_table_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            dstport = row['dstport']
            protocol = row['protocol'].lower()
            tag = row['tag']
            lookup_table[(dstport, protocol)] = tag

    tag_counts = {}
    port_protocol_counts = {}

    with open(flow_log_file, 'r') as f:
        for line in f:
            fields = line.split()
            dstport = fields[5]
            protocol = 'tcp' if fields[7] == '6' else 'udp' if fields[7] == '17' else 'icmp'
            tag = lookup_table.get((dstport, protocol), 'untagged')
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
            port_protocol_counts[(dstport, protocol)] = port_protocol_counts.get((dstport, protocol), 0) + 1

    print("Tag Counts:")
    print("Tag,Count")
    for tag, count in tag_counts.items():
        print(f"{tag},{count}")
    print("\nPort/Protocol Combination Counts:")
    print("Port,Protocol,Count")
    for (port, protocol), count in port_protocol_counts.items():
        print(f"{port},{protocol},{count}")


parse_flow_logs('flow_logs.txt', 'lookup_table.csv')