import matplotlib.pyplot as plt

# Data
batch_sizes = [16, 32, 64, 128, 256]
measured_flops = [340918272, 681836544, 1363673088, 2727346176, 5454692352]
theoretical_flops = [339738624, 679477248, 1358954496, 2717908992, 5435817984]
allocated_memory_measured = [2359296, 4718592, 9437184, 18874368, 37748736]
allocated_memory_theoretical = [2433280, 4792576, 9511168, 18948352, 37822720]
reserved_memory = [0, 0, 20971520, 18874368, 37748736]
        
# FLOPs vs. Batch Sizes
plt.figure(figsize=(6, 4))
plt.plot(batch_sizes, measured_flops, marker='o', linestyle='-', label='Measured FLOPs')
plt.title('FLOPs vs. Batch Sizes')
plt.xlabel('Batch Sizes')
plt.ylabel('FLOPs')
plt.grid(True)
plt.show()

# Allocated and Reserved Memory vs. Batch Sizes
plt.figure(figsize=(6, 4))
plt.plot(batch_sizes, allocated_memory_measured, marker='o', linestyle='-', label='Allocated Memory')
plt.plot(batch_sizes, reserved_memory, marker='o', linestyle='--', label='Reserved Memory')
plt.title('Memory vs. Batch Sizes')
plt.xlabel('Batch Sizes')
plt.ylabel('Memory (Bytes)')
plt.legend()
plt.grid(True)
plt.show()

# Theoretical vs Measured FLOPs Comparison
plt.figure(figsize=(6, 4))
plt.plot(batch_sizes, theoretical_flops, marker='o', linestyle='-', label='Theoretical FLOPs')
plt.plot(batch_sizes, measured_flops, marker='s', linestyle='--', label='Measured FLOPs')
plt.title('Theoretical vs. Measured FLOPs')
plt.xlabel('Batch Sizes')
plt.ylabel('FLOPs')
plt.legend()
plt.grid(True)
plt.show()

# Theoretical vs Measured Allocated Memory Comparison
plt.figure(figsize=(6, 4))
plt.plot(batch_sizes, allocated_memory_theoretical, marker='o', linestyle='-', label='Theoretical Memory')
plt.plot(batch_sizes, allocated_memory_measured, marker='s', linestyle='--', label='Measured Memory')
plt.title('Theoretical vs. Measured Memory')
plt.xlabel('Batch Sizes')
plt.ylabel('Memory (Bytes)')
plt.legend()
plt.grid(True)
plt.show()