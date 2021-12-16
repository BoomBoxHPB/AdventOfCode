def main():
    filename = input("Filename: ")
    file = open(filename, mode='r')

    hex_to_str = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }

    class DataPipe:
        def __init__(self, file) -> None:
            self.file = file
            self.cur_bits = ''
            self.data = file.readline().strip()
            print(self.data)

        def get_bit(self) -> int:
            return self.get_bits(1)

        def get_bits(self, num: int) -> int:
            value = ''
            while num > 0:
                if self.cur_bits == '':
                    self.next_hex()
                value += self.cur_bits[0]
                self.cur_bits = self.cur_bits[1:]
                num -= 1
            return int(value, base=2)

        def next_hex(self) -> None:
            self.cur_bits = hex_to_str[self.data[0]]
            self.data = self.data[1:]

    class Packet:
        def __init__(self, pipe: DataPipe) -> None:
            self.version = pipe.get_bits(3)
            self.id = pipe.get_bits(3)

            self.packet_size = 6
            self.subpackets = []
            self.value = 0

            if self.id == 4: # literal
                more_data = True
                while more_data:
                    more_data = pipe.get_bit() == 1
                    new_value = pipe.get_bits(4)
                    self.value = (self.value << 4) + new_value
                    self.packet_size += 5
            else:
                length_id_type = pipe.get_bit()
                self.packet_size += 1
                if length_id_type == 0: # length of subpackets
                    subpacket_length = pipe.get_bits(15)
                    self.packet_size += 1 + 15 + subpacket_length
                    while subpacket_length > 0:
                        subpacket = Packet(pipe)
                        subpacket_length -= subpacket.packet_size
                        self.subpackets.append(subpacket)

                if length_id_type == 1: # number of subpackets
                    subpacket_count = pipe.get_bits(11)
                    self.packet_size += 1 + 11
                    for _ in range(subpacket_count):
                        subpacket = Packet(pipe)
                        self.packet_size += subpacket.packet_size
                        self.subpackets.append(subpacket)

                # Perform the operation
                if self.id == 0: # sum
                    self.value = sum([p.value for p in self.subpackets])
                elif self.id == 1: # product
                    self.value = 1
                    for p in self.subpackets:
                        self.value *= p.value
                elif self.id == 2: # minimum
                    self.value = min([p.value for p in self.subpackets])
                elif self.id == 3: # maximum
                    self.value = max([p.value for p in self.subpackets])
                elif self.id == 5: # greater than
                    if self.subpackets[0].value > self.subpackets[1].value:
                        self.value = 1
                    else:
                        self.value = 0
                elif self.id == 6: # less than
                    if self.subpackets[0].value < self.subpackets[1].value:
                        self.value = 1
                    else:
                        self.value = 0
                elif self.id == 7: # equal to
                    if self.subpackets[0].value == self.subpackets[1].value:
                        self.value = 1
                    else:
                        self.value = 0

        def __str__(self, tab_level=0) -> str:
            string = '  ' * tab_level + f'V:{self.version}, ID:{self.id}, Value:{self.value}'
            if self.subpackets:
                string += f', Subpackets:'
                for p in self.subpackets:
                    string += '\n' + p.__str__(tab_level + 1)
            return string

    data_pipe = DataPipe(file)
    packet = Packet(data_pipe)
    print(packet)

    def sum_versions(packet: Packet) -> int:
        ver = packet.version
        for p in packet.subpackets:
            ver += sum_versions(p)
        return ver

    print(sum_versions(packet))
    print(packet.value)
main()
