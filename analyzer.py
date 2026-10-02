from models import CPUInfo, DiskInfo, MemoryInfo, Sensor, Status


class Analyzer:

    def cpu_analyze(self, cpu: CPUInfo) -> Status:
        if cpu.cpu_percent > 90 and cpu.cpu_iowait > 15:
            return Status.CRITICAL

        if cpu.cpu_percent > 90:
            return Status.CRITICAL

        if cpu.cpu_iowait > 15:
            return Status.CRITICAL

        if cpu.cpu_percent > 70 or cpu.cpu_iowait > 5:
            return Status.WARNING

        return Status.NORMAL

    def ram_analyze(self, ram: MemoryInfo) -> Status:
        if ram.ram_percent >= 90 or ram.swap_percent >= 90:
            return Status.CRITICAL

        if ram.ram_percent >= 70 or ram.swap_percent >= 70:
            return Status.WARNING

        return Status.NORMAL

    def disk_analyze(self, disk: DiskInfo) -> Status:
        free_gb = disk.free_space / (1024 ** 3)

        if disk.disk_percent >= 90 and free_gb < 5:
            return Status.CRITICAL

        if disk.disk_percent >= 70 and free_gb < 15:
            return Status.WARNING

        return Status.NORMAL

    def sensor_analyze(self, sensor: Sensor) -> Status:
    if sensor.current is None:
        return Status.UNKNOWN

    high_threshold = sensor.high if sensor.high is not None else 85.0
    critical_threshold = (
        sensor.critical if sensor.critical is not None else 95.0
    )

    if sensor.current >= critical_threshold:
        return Status.CRITICAL

    if sensor.current >= high_threshold:
        return Status.WARNING

    return Status.NORMAL

       