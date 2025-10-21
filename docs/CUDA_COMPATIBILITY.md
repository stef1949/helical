# CUDA Compatibility Guide

## Overview

This document provides detailed information about CUDA compatibility with the Helical package.

## Supported CUDA Versions

The Helical package uses **PyTorch 2.6.0**, which supports:
- **CUDA 12.1**
- **CUDA 12.4**

**Important Note**: PyTorch 2.6.0 does not support CUDA 13.0. If you have CUDA 13.0 installed, you will need to either use CUDA 12.1 or 12.4, or wait for a PyTorch version that supports CUDA 13.0. Multiple CUDA versions can coexist on the same system.

## Checking Your CUDA Version

### Using nvcc (CUDA Compiler)
```bash
nvcc --version
```

Example output:
```
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2023 NVIDIA Corporation
Built on Tue_Aug_15_22:02:13_PDT_2023
Cuda compilation tools, release 12.1, V12.1.105
```

### Using nvidia-smi
```bash
nvidia-smi
```

This shows your GPU driver version and CUDA runtime version at the top of the output.

### Using PyTorch
```python
import torch
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"CUDA version: {torch.version.cuda}")
    print(f"Number of GPUs: {torch.cuda.device_count()}")
    print(f"Current GPU: {torch.cuda.current_device()}")
    print(f"GPU Name: {torch.cuda.get_device_name(0)}")
```

## Installing PyTorch with CUDA Support

If you need to reinstall PyTorch with a specific CUDA version:

### For CUDA 12.1
```bash
pip install torch==2.6.0 --index-url https://download.pytorch.org/whl/cu121
```

### For CUDA 12.4
```bash
pip install torch==2.6.0 --index-url https://download.pytorch.org/whl/cu124
```

## Installing mamba-ssm with CUDA Support

The optional `mamba-ssm` package requires specific wheel files for CUDA compatibility.

### Available Wheel Files

For CUDA 12.x, PyTorch 2.6.0, and Python 3.11:
```bash
pip install https://github.com/state-spaces/mamba/releases/download/v2.2.4/mamba_ssm-2.2.4+cu12torch2.5cxx11abiFALSE-cp311-cp311-linux_x86_64.whl
```

**Note**: The torch2.5 wheel is compatible with PyTorch 2.6.0 due to binary compatibility.

### Python Version Mapping

- Python 3.9: `cp39`
- Python 3.10: `cp310`
- Python 3.11: `cp311`
- Python 3.12: `cp312`

### Platform-Specific Wheels

Replace `linux_x86_64` with your platform:
- Linux: `linux_x86_64`
- Windows: `win_amd64`

## Troubleshooting

### CUDA 13.0 Compatibility

**Issue**: PyTorch 2.6.0 does not support CUDA 13.0 yet.

**Solutions**:
1. **Use CUDA 12.x**: Install CUDA 12.1 or 12.4 alongside CUDA 13.0. You can have multiple CUDA versions installed and select which one to use via environment variables.

2. **Set CUDA path**: If you have multiple CUDA versions, ensure the CUDA 12.x version is in your PATH:
   ```bash
   export CUDA_HOME=/usr/local/cuda-12.4
   export PATH=$CUDA_HOME/bin:$PATH
   export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
   ```

3. **Upgrade PyTorch**: Wait for a newer PyTorch version that supports CUDA 13.0 and update the package dependencies accordingly.

4. **Check PyTorch compatibility**: Visit https://pytorch.org/get-started/locally/ for the latest information on CUDA support.

### "CUDA out of memory" errors

```python
import torch
torch.cuda.empty_cache()
```

Or reduce batch size in your model configuration.

### "CUDA driver version is insufficient"

Your GPU driver is too old. Update your NVIDIA drivers:
- Linux: Use your package manager or download from NVIDIA
- Windows: Download from [NVIDIA Driver Downloads](https://www.nvidia.com/Download/index.aspx)

### "No CUDA-capable device is detected"

1. Check if GPU is properly installed: `nvidia-smi`
2. Verify CUDA toolkit is installed: `nvcc --version`
3. Ensure PyTorch is installed with CUDA support (not CPU-only version)

### mamba-ssm Installation Fails

1. Install base helical first (installs PyTorch):
   ```bash
   pip install helical
   ```

2. Then install the specific wheel for your configuration:
   ```bash
   pip install https://github.com/state-spaces/mamba/releases/download/v2.2.4/mamba_ssm-2.2.4+cu12torch2.5cxx11abiFALSE-cp311-cp311-linux_x86_64.whl
   ```

3. Finally install causal-conv1d:
   ```bash
   pip install helical[mamba-ssm]
   ```

## System Requirements

- **GPU**: NVIDIA GPU with compute capability 6.0 or higher
- **CUDA**: Version 12.1 or 12.4
- **Driver**: NVIDIA driver 525.60.13 or newer (for CUDA 12.x)
- **RAM**: At least 8GB (16GB+ recommended for large models)
- **VRAM**: Varies by model, 8GB+ recommended

## Version Compatibility Matrix

| Helical Version | PyTorch Version | Supported CUDA Versions |
|-----------------|-----------------|-------------------------|
| 1.4.5           | 2.6.0           | 12.1, 12.4              |

## Additional Resources

- [PyTorch Installation Guide](https://pytorch.org/get-started/locally/)
- [NVIDIA CUDA Installation Guide](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)
- [Mamba State Spaces Releases](https://github.com/state-spaces/mamba/releases)

## Getting Help

If you encounter CUDA-related issues:

1. Check this compatibility guide
2. Verify your CUDA version matches supported versions
3. Check the [GitHub Issues](https://github.com/helicalAI/helical/issues)
4. Join our [Slack channel](https://dk1sxv04.eu1.hubspotlinksfree.com/Ctc/L2+113/dk1sxv04/VWtlqj8M7nFNVf1vhw52bPfMW8wLjj95ptQw7N1k24YY3m2ndW8wLKSR6lZ3ldW7fZmPx5PxJ2lW8mYJtq5xWH5BVsxw821cWpdKW8CYXdj753XHSW8b5vG-7PTQ2LW1zs6x622rZxDW6930hX7RPKh3N5-trBXyRHkwVfJ3Zs3wRQV_N5NbYL3-lm47W1HvYX63pJp9cW6QXY-x6QsWMTW8G5jZh7T4vphN4Qtr7dMCxlJW8rM1-Y42pS-PW5sfJbh4FyRMhW5mHPkD4yCl56W36YW1_4GpPrGW7-sRYG1gXy8hMXqK6Sp5p69W8YTpvd3tC80SW2PTYtr6hP0dxW863B5F4KNCYkVFSWl390bSlQW78rxWn7JbS3LW14ZJ735n7SpFVSVlQr7lm7vwVlWslf6g9JRQf8mBL3b04)
