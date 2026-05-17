# Memory Forensics Analysis Script

import subprocess

def analyze_memory_dump(dump_file, profile="Win10x64"):
    print(f"🚀 Analyzing memory dump: {dump_file}")
    try:
        # Example Volatility commands (run in forensic environment)
        subprocess.run(["vol.py", "-f", dump_file, "--profile", profile, "pslist"], check=True)
        subprocess.run(["vol.py", "-f", dump_file, "--profile", profile, "malfind"], check=True)
        print("✅ Memory analysis completed")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    analyze_memory_dump("memory.dmp")