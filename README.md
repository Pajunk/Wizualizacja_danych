# Data Visualization

Project for visualization and calculations on three-dimensional data

## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [How to run app](#how-to-run-app)
* [Project status](#project-status)

## General Info

This Python script performs data visualization and analysis on a dataset loaded from `fme.txt`. It processes 3D data points, creates visual representations, and computes various statistical properties, including interpolation, approximation, surface area calculation, and numerical integration.

## Technologies
Project is created with:
* Python version: 3.11.11
* Numpy version: 1.26.4
* Matplotlib verion: 3.10.0
* Sympy version: 1.13.1
* Google Colab

## Setup
Copy code from project.py to your colab notebook file, add fme.txt to your local sesion files.

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

## How to run app
 Press button on upper left next to sript code, or press combination CTRL+ENTER then scroll down to resoults

## Project status
Completed.
