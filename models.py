from dataclasses import dataclass
from enum import Enum


class Status(str, Enum):
    NORMAL = "Normal"
    WARNING = "Warning"
    CRITICAL = "Critical"
    UNKNOWN = "Unknown"


@dataclass
class CPUInfo:
    cpu_percent: float
    cpu_iowait: float
    logical_cpu_count: int


@dataclass
class MemoryInfo:
    ram_percent: float
    total_ram: int
    used_ram: int
    available_ram: int
    swap_percent: float


@dataclass
class DiskInfo:
    disk_percent: float
    total_space: int
    free_space: int
    used_space: int


@dataclass
class Sensor:
    name: str
    group: str
    high: float | None
    critical: float | None
    current: float | None


@dataclass
class SystemInfo:
    cpu: CPUInfo
    memory: MemoryInfo
    disk: DiskInfo
    sensors: list[Sensor]

    