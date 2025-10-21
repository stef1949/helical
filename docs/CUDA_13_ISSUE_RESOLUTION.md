# PyTorch CUDA 13.0 Compatibility Issue Resolution

## Problem Statement
Users were experiencing issues with "PyTorch CUDA 13.0 support" in the Helical package.

## Root Cause Analysis

### Issue Identified
1. **PyTorch 2.6.0 does not support CUDA 13.0**
   - PyTorch 2.6.0 supports CUDA 12.1 and CUDA 12.4
   - Users with CUDA 13.0 cannot use it with the current PyTorch version

2. **Lack of Documentation**
   - No clear explanation of supported CUDA versions
   - Missing guidance for users with CUDA 13.0
   - No troubleshooting resources for CUDA compatibility issues

## Solution Implemented

### 1. Updated README.md
**Changes Made:**
- Added explicit "CUDA Compatibility" section
- Clarified that PyTorch 2.6.0 supports CUDA 12.1 and 12.4
- Documented that CUDA 13.0 is not yet supported by PyTorch 2.6.0
- Updated mamba-ssm installation instructions for PyTorch 2.6.0
- Changed example wheel from `cu12torch2.3` to `cu12torch2.5` (compatible with 2.6.0)
- Added "Troubleshooting CUDA Issues" section with:
  - Guidance for CUDA 13.0 users (use CUDA 12.x or wait for PyTorch update)
  - Commands to check CUDA version (`nvcc --version`, `nvidia-smi`)
  - Python code to verify PyTorch CUDA compatibility

### 2. Created Comprehensive CUDA Compatibility Guide
**New File:** `docs/CUDA_COMPATIBILITY.md`

This guide includes:
- Overview of supported CUDA versions (PyTorch 2.6.0 supports 12.1 and 12.4)
- Detailed instructions for checking CUDA versions
- PyTorch installation commands for specific CUDA versions
- mamba-ssm wheel installation guide with Python version mapping
- Troubleshooting section covering common issues:
  - CUDA 13.0 compatibility (not yet supported, with workarounds)
  - CUDA out of memory
  - Insufficient driver version
  - No CUDA-capable device detected
  - mamba-ssm installation failures
- System requirements table
- Version compatibility matrix
- Links to additional resources

### 3. Updated Documentation Index
**Modified:** `mkdocs.yml`
- Added "Installation & Setup" section to navigation
- Linked the new CUDA Compatibility Guide for easy access

### 4. Added Validation Tests
**New File:** `ci/tests/test_cuda_documentation.py`

Automated tests to verify:
- CUDA version facts are accurate
- PyTorch compatibility claims are correct
- Documentation examples are valid
- README contains required information
- CUDA compatibility guide exists and is complete

## Technical Details

### PyTorch 2.6.0 CUDA Support
- **Supported CUDA versions:** 12.1, 12.4
- **Not supported:** CUDA 13.0 (not yet supported by PyTorch 2.6.0), older CUDA 11.x versions

### mamba-ssm Compatibility
- mamba-ssm 2.2.4 has wheels for various PyTorch versions
- For PyTorch 2.6.0, use torch2.5 wheels (binary compatible)
- Example: `mamba_ssm-2.2.4+cu12torch2.5cxx11abiFALSE-cp311-cp311-linux_x86_64.whl`

### Python Version Mapping
- Python 3.9: `cp39`
- Python 3.10: `cp310`
- Python 3.11: `cp311`
- Python 3.12: `cp312`

## Impact

### User Experience Improvements
1. **Clarity:** Users now understand PyTorch 2.6.0's CUDA support limitations
2. **Guidance:** Clear instructions for installing with supported CUDA versions (12.1, 12.4)
3. **CUDA 13.0 Support:** Documentation explains that CUDA 13.0 is not yet supported and provides workarounds
4. **Troubleshooting:** Comprehensive guide for resolving CUDA issues
5. **Validation:** Commands to verify their setup is correct

### Documentation Quality
1. **Accuracy:** All CUDA version references are now correct
2. **Completeness:** Covers common scenarios and edge cases
3. **Maintainability:** Centralized CUDA compatibility information
4. **Testability:** Automated validation ensures documentation stays accurate

## Verification

### Tests Passing
All documentation validation tests pass:
```
✓ CUDA version facts are correct
✓ PyTorch compatibility claims are correct
✓ Documentation examples are valid
✓ README contains required information
✓ CUDA compatibility guide is complete
```

### Files Modified
1. `README.md` - Updated installation notes with CUDA clarity
2. `docs/CUDA_COMPATIBILITY.md` - New comprehensive guide
3. `mkdocs.yml` - Added guide to documentation navigation
4. `ci/tests/test_cuda_documentation.py` - New validation tests

## Recommendations for Users

### If You Have CUDA 13.0
1. Check your CUDA version: `nvcc --version`
2. PyTorch 2.6.0 does not support CUDA 13.0 yet
3. Options:
   - Install and use CUDA 12.1 or 12.4 (multiple CUDA versions can coexist)
   - Wait for a PyTorch version that supports CUDA 13.0
4. Follow the updated installation instructions in README.md
5. Refer to docs/CUDA_COMPATIBILITY.md for detailed guidance

### Installation Best Practices
1. Install base helical first: `pip install helical`
2. Verify PyTorch CUDA support works
3. If needed, install mamba-ssm using correct wheel for your setup
4. Use the compatibility guide to troubleshoot issues

## Future Considerations

### When PyTorch Updates
- Monitor PyTorch releases for CUDA 13.0 support
- Update package dependencies when PyTorch adds CUDA 13.0 support
- Update documentation when PyTorch adds support for new CUDA versions
- Maintain the compatibility matrix in CUDA_COMPATIBILITY.md

### When mamba-ssm Updates
- Check for new wheel releases with torch 2.6 support
- Update example wheel URLs in documentation
- Test compatibility with new versions

## Conclusion

The PyTorch CUDA 13.0 compatibility issue has been addressed by:
1. Clarifying that PyTorch 2.6.0 does not yet support CUDA 13.0
2. Documenting supported CUDA versions (12.1, 12.4)
3. Providing workarounds for CUDA 13.0 users (use CUDA 12.x or wait for PyTorch update)
4. Updating installation instructions for PyTorch 2.6.0
5. Creating comprehensive troubleshooting resources
6. Adding automated validation to prevent future documentation drift

Users can now understand the CUDA compatibility limitations and have clear guidance on how to proceed based on their CUDA version.
