import os
import platform
import subprocess

def ping_host(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    try:
        output = subprocess.check_output(command, universal_newlines=True)
        print(f"{host} is reachable")
        return f"{host},reachable\n"
    except subprocess.CalledProcessError:
        print(f"{host} is unreachable")
        return f"{host},unreachable\n"

def main():
    hosts = ["8.8.8.8", "1.1.1.1", "invalid.host"]
    log_file = "ping_results.csv"

    with open(log_file, "w") as file:
        file.write("Host,Status\n")
        for host in hosts:
            result = ping_host(host)
            file.write(result)

    print(f"Results saved to {log_file}")

if __name__ == "__main__":
    main()