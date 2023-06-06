# inheritance vs compostion

class CPU:
    def __init__(self, core) -> None:
        self.cores = core

class RAM:
    def __init__(self, size) -> None:
        self.size = size

    def __repr__(self) -> str:
        print(f'The size is: {self.size}')

class HardDrive:
    def __init__(self, capacity) -> None:
        self.capacity = capacity

# computer has a cpu
# computer has a ram
# computer has a hard drive

class Computer:
    def __init__(self, core, size, capacity) -> None:
        self.cpu = CPU(core)
        self.size = RAM(size)
        self.hard_disk = HardDrive(capacity)

mac = Computer(8, 16, 512)
print(mac.size)