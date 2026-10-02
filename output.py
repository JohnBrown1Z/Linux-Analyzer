from models import CPUInfo, DiskInfo, MemoryInfo, Sensor, Status


class Output:

    @staticmethod
    def _bytes_to_gb(value: int | None) -> str:
        if value is None:
            return "N/A"

        return f"{value / (1024 ** 3):.2f} GB"

    def display_cpu(self, cpu: CPUInfo, status: Status) -> None:
        print("--- CPU ---")
        print(f"CPU Usage: {cpu.cpu_percent:.1f} %")
        print(f"CPU I/O Wait: {cpu.cpu_iowait:.1f} %")
        print(f"Logical CPUs: {cpu.logical_cpu_count}")
        print(f"Status: {status.value}")
        print()

    def display_ram(self, ram: MemoryInfo, status: Status) -> None:
        print("--- RAM & SWAP ---")
        print(f"RAM Usage: {ram.ram_percent:.1f} %")
        print(f"Total RAM: {self._bytes_to_gb(ram.total_ram)}")
        print(f"Used RAM: {self._bytes_to_gb(ram.used_ram)}")
        print(f"Available RAM: {self._bytes_to_gb(ram.available_ram)}")
        print(f"SWAP Usage: {ram.swap_percent:.1f} %")
        print(f"Status: {status.value}")
        print()

    def display_disk(self, disk: DiskInfo, status: Status) -> None:
        print("--- Disk (/) ---")
        print(f"Disk Usage: {disk.disk_percent:.1f} %")
        print(f"Total Space: {self._bytes_to_gb(disk.total_space)}")
        print(f"Free Space: {self._bytes_to_gb(disk.free_space)}")
        print(f"Used Space: {self._bytes_to_gb(disk.used_space)}")
        print(f"Status: {status.value}")
        print()

    def display_sensors(
        self,
        sensors: list[Sensor],
        statuses: list[Status],
    ) -> None:
        print("--- Temperatures ---")

        if not sensors:
            print("No hardware sensors available.")
            print()
            return

        for sensor, status in zip(sensors, statuses):
            high = (
                f"{sensor.high:.1f} °C"
                if sensor.high is not None
                else "N/A"
            )

            critical = (
                f"{sensor.critical:.1f} °C"
                if sensor.critical is not None
                else "N/A"
            )

            current = (
                f"{sensor.current:.1f} °C"
                if sensor.current is not None
                else "N/A"
            )

            print(f"Sensor: {sensor.name} ({sensor.group})")
            print(
                f"Current: {current} "
                f"(High: {high}, Critical: {critical})"
            )
            print(f"Status: {status.value}")
            print()
     