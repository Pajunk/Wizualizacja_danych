# Data Visualization

## Overview

This Python script performs data visualization and analysis on a dataset loaded from `fme.txt`. It processes 3D data points, creates visual representations, and computes various statistical properties, including interpolation, approximation, surface area calculation, and numerical integration.

## Features

- **Data Processing:** Reads `fme.txt` and extracts `x`, `y`, and `z` coordinates.
- **2D & 3D Visualization:** Generates contour plots and 3D surface plots using `matplotlib`.
- **Statistical Analysis:**
  - Mean and median calculations.
  - Standard deviation computation.
- **Interpolation and Approximation:**
  - Lagrange interpolation.
  - Least squares approximation.
- **Surface Area Calculation:** Computes the total surface area based on 3D data.
- **Numerical Integration:** Calculates integrals using the trapezoidal method.
- **Partial Derivatives:** Computes and visualizes first-order derivatives.
- **Monotonicity Analysis:** Determines intervals where the function is increasing or decreasing.

## Dependencies

Ensure you have the following Python libraries installed:

```bash
pip install numpy matplotlib sympy scipy
