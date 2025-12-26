# import psutil

# # cpu threshould check function
# def check_cpu_threshoulds():
#     cpu_threshoulds = float(input("Enter the CPU threshoulds"))
#     current_cpu = psutil.cpu_percent(interval=1)
#     print("Current CPU %: ", current_cpu)
#     if current_cpu > cpu_threshoulds:  
#         print("CPU is in risk state...") 
#     else:
#         print("CPU in Safe state...")


# check_cpu_threshoulds()

# # memory threshould check function

# def check_memory_threshoulds():
#     memory_threshoulds = float(input("Enter the  Memory threshoulds"))
#     current_memory = psutil.virtual_memory().percent
#     print("Current Memory %: ", current_memory)

#     if current_memory > memory_threshoulds:
#         print("Memory is in risk state...")
#     else:
#         print("Memory in Safe state...")

# check_memory_threshoulds()

# # disk threshould check function

# def check_disk_threshoulds():
#     disk_threshoulds = float(input("Enter the Disk threshoulds"))
#     current_disk = psutil.disk_usage('/').percent
#     print("Current Disk %: ", current_disk)
#     if current_disk > disk_threshoulds:
#         print("Disk is in risk state...")
#     else:
#         print("Disk in Safe state...")

# check_disk_threshoulds()

import psutil


def get_thresholds():
    cpu = float(input("Enter CPU threshold (%): "))
    memory = float(input("Enter Memory threshold (%): "))
    disk = float(input("Enter Disk threshold (%): "))
    return cpu, memory, disk


def check_system(cpu_t, mem_t, disk_t):
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    print("\n--- System Health Status ---")

    if cpu_usage > cpu_t:
        print(f"CPU Usage HIGH: {cpu_usage}%")
    else:
        print(f"CPU Usage OK: {cpu_usage}%")

    if memory_usage > mem_t:
        print(f"Memory Usage HIGH: {memory_usage}%")
    else:
        print(f"Memory Usage OK: {memory_usage}%")

    if disk_usage > disk_t:
        print(f"Disk Usage HIGH: {disk_usage}%")
    else:
        print(f"Disk Usage OK: {disk_usage}%")


def main():
    cpu_t, mem_t, disk_t = get_thresholds()
    check_system(cpu_t, mem_t, disk_t)


if __name__ == "__main__":
    main()

