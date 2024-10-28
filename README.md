# Performance Analysis of Conv2d Layer in CNNs Using MNIST

This project provides a comprehensive performance analysis of the Conv2d-2 layer in a Convolutional Neural Network (CNN) trained on the MNIST dataset. The study evaluates both theoretical and empirical metrics, focusing on FLOPs (Floating Point Operations) and memory usage across different batch sizes on an NVIDIA V100 GPU using PyTorch.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Setup and Requirements](#setup-and-requirements)
- [Methodology](#methodology)
- [Results and Analysis](#results-and-analysis)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction
This project aims to bridge the gap between theoretical and empirical performance metrics for convolutional layers in CNNs. By analyzing the Conv2d-2 layer’s FLOPs and memory requirements, we gain insights into the effect of varying batch sizes on computation and memory usage, essential for efficient model optimization in real-world applications.

## Project Structure
```
├── code/                    # Python scripts for running experiments
├── results/                 # Output files and performance metrics
├── README.md                # Project description and instructions
├── requirements.txt         # List of dependencies
```

## Setup and Requirements

### Prerequisites
- Python 3.8 or higher
- NVIDIA Nsight Compute for GPU profiling
- PyTorch (tested on version 1.13.0)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/performance-analysis-conv2d-layer.git
   cd performance-analysis-conv2d-layer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Methodology
The analysis includes:
- **Theoretical Calculations:** Using pen-and-paper to estimate FLOPs and memory for the Conv2d-2 layer.
- **Empirical Measurements:** Profiling the Conv2d-2 layer on an NVIDIA V100 GPU, leveraging PyTorch's CUDA memory utilities and Nsight Compute.
- **Comparative Analysis:** Comparing theoretical and measured results to observe discrepancies and trends with increasing batch sizes.

## Results and Analysis
The results section presents a detailed comparison of theoretical vs. measured FLOPs and memory usage. Key observations include:
- **FLOPs Trends:** The increase in FLOPs scales linearly with batch size due to additional input processing.
- **Memory Usage:** Memory requirements grow with batch size, impacted by PyTorch's memory optimizations and GPU-specific caching.

## Conclusion
The study provides insights into performance tuning of convolutional layers in CNNs for GPU-based environments. The results highlight practical factors, such as memory handling and parallelism, which affect resource utilization beyond theoretical estimates.

## References
- NVIDIA Nsight Compute Documentation: [link](https://docs.nvidia.com/nsight-compute/)
- PyTorch Documentation: [link](https://pytorch.org/docs/stable/index.html)