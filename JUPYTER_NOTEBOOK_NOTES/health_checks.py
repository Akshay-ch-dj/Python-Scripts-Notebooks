#!/usr/bin/env python3

import os
import sys
import shutil
import psutil
import socket

stats = {}


def check_reboot():
  """Returns True if the computer has a pending reboot"""
  return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
  """Returns True if there is enough disk space, false otherwise"""
  du = shutil.disk_usage(disk)
  # calculate the % of free space
  percent_free = 100 * du.free/du.total
  # calculate in GB
  GB_free = du.free/2**30

  stats["check_root_full"] = (f"  Total disk memory(in GB): {du.total/(2**30):.2f}\n\
  Disk memory free in GB: {GB_free:.2f}\n\
  Disk memory free in %: {percent_free:.2f}")

  if GB_free < min_gb or percent_free < min_percent:
    return True
  return False

# function to check ram usage (min_ram set to 0.5 gb)
def check_memory():
  """Return True when less than 0.5gb RAM available"""
  mu = psutil.virtual_memory()
  # memory in GB
  GB_mem_free = mu.available/(2**30)
  stats["check_memory_wrap"] = (f"\n  Total RAM available(in GB): {mu.total/(2**30):.2f}\n\
  Available RAM(in GB): {GB_mem_free:.2f}")

  if GB_mem_free < 0.5:
    return True
  return False

# function to check cpu percent used
def check_cpu_constrain():
  """Returns true when cpu is more than 75% loaded"""
  cpu_use = psutil.cpu_percent(1)
  stats["check_cpu_constrain"] = f"\n  CPU Usage(in %): {cpu_use}"

  return cpu_use > 75

# check for network connectivity
def check_no_network():
  """Returns True if it fails to resolve google url,False otherwise"""
  try:
    socket.gethostbyname("www.google.com")
    return False
  except:
    return True

# wrapper for Disk check
def check_root_full():
  """Wrapper function for check_disk_full"""
  return check_disk_full(disk="/", min_gb=2, min_percent=10)


def main():
  checks = [
      (check_reboot, "pending reboot"),
      (check_root_full, "Root partition Full"),
      (check_memory, "RAM full: only 10% free"),
      (check_cpu_constrain, "CPU load above 75%"),
      (check_no_network, "No working Network"),
  ]
  everything_ok = True
  for check, msg in checks:
    if check():
      print(msg)
      everything_ok = False

  if not everything_ok:
    sys.exit(1)
  print("Everything OK.")

  if input("Press Y if need detailed stats:").lower() == "y":
    for key in stats:
      print(stats[key])
  sys.exit(0)

main()
