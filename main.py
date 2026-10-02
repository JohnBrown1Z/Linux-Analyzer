from analyzer import Analyzer
from collector import Collector
from output import Output


def main() -> None:
    collector = Collector()
    analyzer = Analyzer()
    output = Output()

    system = collector.collect()

    cpu_status = analyzer.cpu_analyze(system.cpu)
    ram_status = analyzer.ram_analyze(system.memory)
    disk_status = analyzer.disk_analyze(system.disk)

    sensor_statuses = [
        analyzer.sensor_analyze(sensor)
        for sensor in system.sensors
    ]

    output.display_cpu(system.cpu, cpu_status)
    output.display_ram(system.memory, ram_status)
    output.display_disk(system.disk, disk_status)
    output.display_sensors(system.sensors, sensor_statuses)


if __name__ == "__main__":
    main()