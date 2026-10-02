import psutil

from models import CPUInfo, DiskInfo, MemoryInfo, Sensor, SystemInfo


class Collector:

    def collect(self) -> SystemInfo:
        return SystemInfo(
            cpu=self.collect_cpu(),
            memory=self.collect_memory(),
            disk=self.collect_disk(),
            sensors=self.collect_sensors(),
        )

    def collect_cpu(self) -> CPUInfo:
        cpu_times = psutil.cpu_times_percent(interval=1)

        return CPUInfo(
            cpu_percent=100.0 - cpu_times.idle,
            cpu_iowait=cpu_times.iowait,
            logical_cpu_count=psutil.cpu_count(logical=True) or 0,
        )

    def collect_memory(self) -> MemoryInfo:
        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()

        return MemoryInfo(
            ram_percent=memory.percent,
            total_ram=memory.total,
            used_ram=memory.used,
            available_ram=memory.available,
            swap_percent=swap.percent,
        )

    def collect_disk(self) -> DiskInfo:
        disk = psutil.disk_usage("/")

        return DiskInfo(
            disk_percent=disk.percent,
            total_space=disk.total,
            free_space=disk.free,
            used_space=disk.used,
        )

    def collect_sensors(self) -> list[Sensor]:
        sensors: list[Sensor] = []

        if not hasattr(psutil, "sensors_temperatures"):
            return sensors

        temperatures = psutil.sensors_temperatures()

        for group, entries in temperatures.items():
            for index, metric in enumerate(entries, start=1):
                name = metric.label or f"{group}_{index}"

                sensors.append(
                    Sensor(
                        name=name,
                        group=group,
                        high=metric.high,
                        critical=metric.critical,
                        current=metric.current,
                    )
                )

        return sensors