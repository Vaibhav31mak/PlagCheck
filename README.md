# PlagCheck

**PlagCheck** is a fast and lightweight code plagiarism detection tool written in modern C++.  
It supports both **C++** and **Python** files and uses a token-based comparison algorithm inspired by the SIM method.

## 🚀 Features
- Token-based similarity checking
- Supports C++ code
- Cross-platform (Windows + Linux)
- Build as standalone executable or Python module

## 🛠️ Build Instructions

### 🔹 Windows (Visual Studio)
- Open the solution in **Visual Studio 2022**
- Build the project (`.exe` or `.pyd`)

### 🔹 Linux
```bash
make normal     # Build CLI executable
make python     # Build Python module (.so)
make clean      # Clean build files
