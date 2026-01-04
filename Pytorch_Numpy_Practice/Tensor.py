import torch
import time

def compare_cpu_gpu_performance():
    """
    Compare performance of matrix multiplication on CPU vs GPU
    for 1000x1000 matrices.
    """
    
    # ==============================
    # Step 1: Check if GPU is available
    # ==============================
    print("=" * 50)
    print("GPU AVAILABILITY CHECK")
    print("=" * 50)
    
    # Check if CUDA (NVIDIA GPU support) is available
    if torch.cuda.is_available():
        print("✓ GPU is available!")
        print(f"  GPU Name: {torch.cuda.get_device_name(0)}")
    else:
        print("✗ GPU is not available. Using CPU only.")
    
    # ==============================
    # Step 2: Create tensors on CPU
    # ==============================
    print("\n" + "=" * 50)
    print("CREATING TENSORS ON CPU")
    print("=" * 50)
    
    # Create two 1000x1000 matrices with random values
    # Note: All tensors are created on CPU by default
    matrix_a_cpu = torch.randn(1000, 1000)  # Random matrix A
    matrix_b_cpu = torch.randn(1000, 1000)  # Random matrix B
    
    print(f"Matrix A shape: {matrix_a_cpu.shape}")
    print(f"Matrix B shape: {matrix_b_cpu.shape}")
    print(f"Matrix A device (created on): {matrix_a_cpu.device}")
    
    # ==============================
    # Step 3: CPU Performance Test
    # ==============================
    print("\n" + "=" * 50)
    print("CPU PERFORMANCE TEST")
    print("=" * 50)
    
    # Warm-up: Run once to initialize libraries
    _ = torch.mm(matrix_a_cpu, matrix_b_cpu)
    
    # Time CPU matrix multiplication
    start_time_cpu = time.time()
    result_cpu = torch.mm(matrix_a_cpu, matrix_b_cpu)  # Matrix multiplication
    cpu_time = time.time() - start_time_cpu
    
    print(f"CPU Matrix Multiplication Time: {cpu_time:.4f} seconds")
    print(f"Result shape (CPU): {result_cpu.shape}")
    print(f"Result device (CPU): {result_cpu.device}")
    
    # ==============================
    # Step 4: GPU Performance Test (if available)
    # ==============================
    if torch.cuda.is_available():
        print("\n" + "=" * 50)
        print("GPU PERFORMANCE TEST")
        print("=" * 50)
        
        # Step 4a: Move tensors from CPU to GPU
        print("\nMoving tensors from CPU to GPU...")
        
        # Method 1: Using .to() method (recommended)
        matrix_a_gpu = matrix_a_cpu.to('cuda')
        matrix_b_gpu = matrix_b_cpu.to('cuda')
        
        # Alternative method: Using .cuda()
        # matrix_a_gpu = matrix_a_cpu.cuda()
        # matrix_b_gpu = matrix_b_cpu.cuda()
        
        print(f"Matrix A device (after move): {matrix_a_gpu.device}")
        print(f"Matrix B device (after move): {matrix_b_gpu.device}")
        
        # Important: GPU operations are asynchronous
        # We need to synchronize for accurate timing
        torch.cuda.synchronize()  # Wait for all GPU operations to complete
        
        # Step 4b: Perform matrix multiplication on GPU
        print("\nPerforming matrix multiplication on GPU...")
        
        # Warm-up GPU
        _ = torch.mm(matrix_a_gpu, matrix_b_gpu)
        torch.cuda.synchronize()
        
        # Time GPU matrix multiplication
        start_time_gpu = time.time()
        result_gpu = torch.mm(matrix_a_gpu, matrix_b_gpu)
        torch.cuda.synchronize()  # Wait for GPU to finish
        gpu_time = time.time() - start_time_gpu
        
        print(f"GPU Matrix Multiplication Time: {gpu_time:.4f} seconds")
        print(f"Result shape (GPU): {result_gpu.shape}")
        print(f"Result device (GPU): {result_gpu.device}")
        
        # Step 4c: Move result back to CPU
        print("\nMoving result from GPU back to CPU...")
        result_gpu_cpu = result_gpu.to('cpu')  # or result_gpu.cpu()
        
        print(f"Result device (after moving back): {result_gpu_cpu.device}")
        
        # ==============================
        # Step 5: Verify correctness
        # ==============================
        print("\n" + "=" * 50)
        print("VERIFICATION")
        print("=" * 50)
        
        # Check if CPU and GPU results match (allowing for small numerical differences)
        # Note: Due to floating-point precision, GPU and CPU might have tiny differences
        if torch.allclose(result_cpu, result_gpu_cpu, rtol=1e-5):
            print("✓ Results from CPU and GPU match!")
        else:
            print("⚠ Results differ slightly (normal due to floating-point precision)")
        
        # ==============================
        # Step 6: Performance Comparison
        # ==============================
        print("\n" + "=" * 50)
        print("PERFORMANCE COMPARISON")
        print("=" * 50)
        
        print(f"CPU Time: {cpu_time:.4f} seconds")
        print(f"GPU Time: {gpu_time:.4f} seconds")
        
        if gpu_time > 0:  # Avoid division by zero
            speedup = cpu_time / gpu_time
            print(f"Speedup (GPU vs CPU): {speedup:.2f}x")
            
            if speedup > 1:
                print(f"GPU is {speedup:.2f}x faster than CPU")
            else:
                print("CPU is faster (unusual for this operation)")
        
        # ==============================
        # Step 7: Memory Cleanup
        # ==============================
        print("\n" + "=" * 50)
        print("MEMORY MANAGEMENT")
        print("=" * 50)
        
        # Delete GPU tensors to free memory
        del matrix_a_gpu, matrix_b_gpu, result_gpu, result_gpu_cpu
        torch.cuda.empty_cache()  # Clear GPU memory cache
        
        print("GPU memory cleared")
    
    print("\n" + "=" * 50)
    print("TEST COMPLETE")
    print("=" * 50)

# Run the comparison
if __name__ == "__main__":
    compare_cpu_gpu_performance()











