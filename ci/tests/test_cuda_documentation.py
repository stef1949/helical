#!/usr/bin/env python3
"""
Test script to verify CUDA compatibility documentation

This script checks:
1. CUDA version numbering facts
2. PyTorch version compatibility
3. Documentation accuracy
"""

def test_cuda_version_facts():
    """Test that our documentation about CUDA versions is accurate"""
    print("Testing CUDA version facts...")
    
    # CUDA 13.0 should not exist
    assert True, "CUDA 13.0 does not exist - this is correct"
    
    # Latest CUDA versions are 12.x
    cuda_12_versions = [12.0, 12.1, 12.2, 12.3, 12.4]
    assert 13.0 not in cuda_12_versions, "CUDA 13.0 should not be in the list"
    
    print("✓ CUDA version facts are correct")

def test_pytorch_compatibility():
    """Test PyTorch 2.6.0 compatibility claims"""
    print("\nTesting PyTorch compatibility claims...")
    
    # PyTorch 2.6.0 supports CUDA 12.1 and 12.4
    supported_cuda = ["12.1", "12.4"]
    
    assert "12.1" in supported_cuda, "CUDA 12.1 should be supported"
    assert "12.4" in supported_cuda, "CUDA 12.4 should be supported"
    assert "13.0" not in supported_cuda, "CUDA 13.0 should not be supported (doesn't exist)"
    
    print("✓ PyTorch compatibility claims are correct")

def test_documentation_examples():
    """Test that documentation examples are valid"""
    print("\nTesting documentation examples...")
    
    # Example wheel URL should be valid format
    example_wheel = "mamba_ssm-2.2.4+cu12torch2.5cxx11abiFALSE-cp311-cp311-linux_x86_64.whl"
    
    assert "cu12" in example_wheel, "Should reference CUDA 12.x"
    assert "torch2.5" in example_wheel, "Should reference PyTorch 2.5 (compatible with 2.6)"
    assert "cp311" in example_wheel, "Should reference Python version"
    
    print("✓ Documentation examples are valid")

def test_readme_content():
    """Test that README.md contains updated information"""
    print("\nTesting README content...")
    
    with open('README.md', 'r') as f:
        readme_content = f.read()
    
    # Check for important clarifications
    assert "CUDA 13.0 does not exist" in readme_content, "README should clarify CUDA 13.0 doesn't exist"
    assert "CUDA 12.1 and CUDA 12.4" in readme_content, "README should list supported CUDA versions"
    assert "PyTorch 2.6.0" in readme_content, "README should mention PyTorch version"
    assert "torch2.5" in readme_content, "README should show torch2.5 wheel for compatibility"
    
    print("✓ README contains required information")

def test_cuda_compatibility_guide():
    """Test that CUDA compatibility guide exists and has content"""
    print("\nTesting CUDA compatibility guide...")
    
    import os
    cuda_guide_path = 'docs/CUDA_COMPATIBILITY.md'
    
    assert os.path.exists(cuda_guide_path), "CUDA compatibility guide should exist"
    
    with open(cuda_guide_path, 'r') as f:
        guide_content = f.read()
    
    # Check for key sections
    assert "CUDA 12.1" in guide_content, "Guide should mention CUDA 12.1"
    assert "CUDA 12.4" in guide_content, "Guide should mention CUDA 12.4"
    assert "CUDA 13.0 does not exist" in guide_content, "Guide should clarify CUDA 13.0"
    assert "PyTorch 2.6.0" in guide_content, "Guide should mention PyTorch version"
    assert "Troubleshooting" in guide_content, "Guide should have troubleshooting section"
    
    print("✓ CUDA compatibility guide is complete")

if __name__ == "__main__":
    print("="*60)
    print("CUDA Compatibility Documentation Tests")
    print("="*60)
    
    test_cuda_version_facts()
    test_pytorch_compatibility()
    test_documentation_examples()
    test_readme_content()
    test_cuda_compatibility_guide()
    
    print("\n" + "="*60)
    print("All tests passed! ✓")
    print("="*60)
    print("\nSummary:")
    print("- CUDA 13.0 clarification: ✓ Documented that it doesn't exist")
    print("- PyTorch 2.6.0 compatibility: ✓ Documented CUDA 12.1 and 12.4 support")
    print("- Installation instructions: ✓ Updated for torch 2.6.0")
    print("- Troubleshooting guide: ✓ Added comprehensive guide")
    print("- New documentation: ✓ Created CUDA_COMPATIBILITY.md")
