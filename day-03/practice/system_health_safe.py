import psutil


def get_thresholds():
    """
    Get CPU, Memory, Disk threshold values from user safely
    """
    try:
        cpu = float(input("Enter CPU threshold (%): "))
        memory = float(input("Enter Memory threshold (%): "))
        disk = float(input("Enter Disk threshold (%): "))
        return cpu, memory, disk

    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return None


def check_system(cpu_t, mem_t, disk_t):
    """
    Fetch system metrics and compare with thresholds
    """
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        print("\nSystem Health Status")

        if cpu_usage > cpu_t:
            print("CPU Usage HIGH:", cpu_usage, "%")
        else:
            print("CPU Usage OK:", cpu_usage, "%")

        if memory_usage > mem_t:
            print("Memory Usage HIGH:", memory_usage, "%")
        else:
            print("Memory Usage OK:", memory_usage, "%")

        if disk_usage > disk_t:
            print("Disk Usage HIGH:", disk_usage, "%")
        else:
            print("Disk Usage OK:", disk_usage, "%")

    except Exception as error:
        print("Error while checking system health")
        print("Reason:", error)


def main():
    thresholds = get_thresholds()

    if thresholds is None:
        return

    cpu_t, mem_t, disk_t = thresholds
    check_system(cpu_t, mem_t, disk_t)


if __name__ == "__main__":
    main()
