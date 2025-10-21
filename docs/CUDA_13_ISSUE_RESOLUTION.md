# CUDA 13.0 Issue Resolution

## Problem Statement
Users were experiencing confusion regarding "PyTorch CUDA 13.0 support" in the Helical package.

## Root Cause Analysis

### Issue Identified
1. **CUDA 13.0 does not exist** - This was the primary source of confusion
   - The latest CUDA versions are in the 12.x series (12.1, 12.4, etc.)
   - There is no CUDA 13.0 version released by NVIDIA

2. **Outdated Documentation**
   - README showed example for torch 2.3, but the project uses torch 2.6.0
   - No clear explanation of supported CUDA versions
   - mamba-ssm wheel installation instructions were outdated

3. **Lack of Troubleshooting Resources**
   - No guidance for users encountering CUDA-related issues
   - No clear documentation on how to check CUDA versions
   - Missing compatibility matrix

## Solution Implemented

### 1. Updated README.md
**Changes Made:**
- Added explicit "CUDA Compatibility" section
- Clarified that CUDA 13.0 does not exist
- Documented supported CUDA versions (12.1, 12.4)
- Updated mamba-ssm installation instructions for PyTorch 2.6.0
- Changed example wheel from `cu12torch2.3` to `cu12torch2.5` (compatible with 2.6.0)
- Added "Troubleshooting CUDA Issues" section with:
  - Explanation of CUDA version confusion
  - Commands to check CUDA version (`nvcc --version`, `nvidia-smi`)
  - Python code to verify PyTorch CUDA compatibility

### 2. Created Comprehensive CUDA Compatibility Guide
**New File:** `docs/CUDA_COMPATIBILITY.md`

This guide includes:
- Overview of supported CUDA versions
- Detailed instructions for checking CUDA versions
- PyTorch installation commands for specific CUDA versions
- mamba-ssm wheel installation guide with Python version mapping
- Troubleshooting section covering common issues:
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
- **Not supported:** CUDA 13.0 (doesn't exist), older CUDA 11.x versions

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
1. **Clarity:** Users now understand that CUDA 13.0 doesn't exist
2. **Guidance:** Clear instructions for installing with correct CUDA versions
3. **Troubleshooting:** Comprehensive guide for resolving CUDA issues
4. **Validation:** Commands to verify their setup is correct

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

### If You See "CUDA 13.0" References
1. Check your actual CUDA version: `nvcc --version`
2. You likely have CUDA 12.x (12.1, 12.4, etc.)
3. Follow the updated installation instructions in README.md
4. Refer to docs/CUDA_COMPATIBILITY.md for detailed guidance

### Installation Best Practices
1. Install base helical first: `pip install helical`
2. Verify PyTorch CUDA support works
3. If needed, install mamba-ssm using correct wheel for your setup
4. Use the compatibility guide to troubleshoot issues

## Future Considerations

### When PyTorch Updates
- Monitor PyTorch releases for new CUDA support
- Update documentation when PyTorch adds support for future CUDA versions
- Maintain the compatibility matrix in CUDA_COMPATIBILITY.md

### When mamba-ssm Updates
- Check for new wheel releases with torch 2.6 support
- Update example wheel URLs in documentation
- Test compatibility with new versions

## Conclusion

The "CUDA 13.0 issue" has been resolved by:
1. Clarifying that CUDA 13.0 does not exist
2. Documenting actual supported CUDA versions (12.1, 12.4)
3. Updating installation instructions for PyTorch 2.6.0
4. Creating comprehensive troubleshooting resources
5. Adding automated validation to prevent future documentation drift

Users can now confidently install and use Helical with the correct CUDA versions and have clear guidance when issues arise.
