# Pantheon Congestion Control Evaluation - Programming Assignment 3

This project evaluates various congestion control (CC) algorithms using the Pantheon framework and Mahimahi network emulation. The goal is to measure and compare throughput, latency, and packet loss under different network conditions.

## 🛠 Environment Requirements

- OS: Ubuntu 20.04 LTS (x86_64 or ARM64)
- RAM: At least 4 GB
- Disk Space: At least 10 GB
- Python: **Python 2.7** (required by Pantheon)
- Root (sudo) access

---

## ✅ Setup Instructions

### 1. System Dependencies

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential git curl python2 python2-dev \
  python-is-python2 iptables iproute2 gnuplot texlive-full \
  software-properties-common
```

> On Ubuntu 20.04, `python-is-python2` makes `python` point to Python 2.7.

---

### 2. Install pip for Python 2.7

```bash
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py
sudo python get-pip.py
```

Verify:

```bash
python --version  # Should output Python 2.7.x
pip --version     # Should use Python 2.7
```

---

### 3. Clone Pantheon Repository

```bash
git clone https://github.com/StanfordSNR/pantheon.git
cd pantheon
git submodule update --init --recursive
```

---

### 4. Install Pantheon Dependencies

```bash
sudo ./tools/install_deps.sh
```

This will:
- Install Mahimahi
- Install required Python 2.7 packages: `numpy`, `matplotlib`, `pyyaml`, `tabulate`
- Compile the `pantheon_tunnel` binary

---

### 5. Install Dependencies for Specific CC Schemes

Choose the schemes you want to evaluate (e.g., `bbr`, `cubic`, `copa`) and run:

```bash
python src/experiments/setup.py --install-deps --schemes "bbr cubic copa"
```

Alternatively, install all supported schemes:

```bash
python src/experiments/setup.py --install-deps --all
```

---

## 🧪 Running Experiments

### 1. Example: Local Test (Cubic vs BBR)

```bash
sudo python src/experiments/test.py local --schemes "cubic bbr" --runtime 60
```

### 2. Custom Test with Emulated Network Conditions

#### Low latency, high bandwidth (50Mbps, 10ms RTT):

```bash
sudo python src/experiments/test.py local \
  --schemes "bbr cubic copa" \
  --uplink-trace emulated/const48.trace \
  --downlink-trace emulated/const48.trace \
  --runtime 60
```

#### High latency, low bandwidth (1Mbps, 200ms RTT):

```bash
sudo python src/experiments/test.py local \
  --schemes "bbr cubic copa" \
  --uplink-trace emulated/1mbps_200ms.trace \
  --downlink-trace emulated/1mbps_200ms.trace \
  --runtime 60
```

---