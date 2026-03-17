# 🧩 Modular Hybrid AI System for Solving Visual Sudoku

This repository contains the implementation for my Bachelor’s thesis, which presents a modular AI system capable of solving Sudoku puzzles directly from images while providing interpretable results.

## 📌 Overview
The project combines computer vision, deep learning, and algorithmic problem solving into a unified pipeline that:
- Extracts Sudoku grids from images  
- Recognizes handwritten digits  
- Solves the puzzle algorithmically  
- Provides an interactive solving experience  

Unlike many end-to-end approaches, this system is modular and explainable.

## 🎯 Objective
The goal of this thesis is to design a robust and interpretable system for solving visual Sudoku puzzles by integrating:
- Image preprocessing techniques  
- Neural networks for digit recognition  
- Classical search algorithms for solving  

## 🧠 Methods

### 🔍 Image Processing
- Grid extraction using contour detection and border dilation  
- Cell segmentation into individual digits  

### 🔢 Digit Recognition
- Convolutional Neural Network (CNN)  
- 8-layer architecture  
- Trained for handwritten digit classification  

### 🧩 Sudoku Solving
- Depth-First Search (DFS) with backtracking  
- Designed for simplicity and integration  

### 🎮 Interactive Module
- Step-by-step solving options  
- Partial reveal functionality  
- Export of solved puzzles as images  

## 📊 Results

- **Image preprocessing accuracy:** 98.8%  
- **Digit recognition (combined):** 95.27%  
- **Overall system accuracy:**  
  - 95.27% (without difficulty classification)  
  - 66.97% (with classification)  
- **Difficulty classification accuracy:** 38.67%  

## 📁 Structure
├── src/ # Core implementation
├── models/ # Trained CNN models
├── data/ # Input images / datasets
├── results/ # Outputs and evaluations
└── README.md

## ⚙️ Setup
```bash
git clone https://github.com/kolianedgar/Sudoku_solver_TYP.git
cd Sudoku_solver_TYP
```

## 🚧 Challenges

- Limited computational resources
- Dataset inconsistencies
- Limited experience with deep learning and constraint programming

## 🔮 Future Improvements

- Improved and synthetic datasets
- GUI for better user interaction
- More advanced solving techniques (e.g. CSP, Algorithm X)
- Better difficulty classification

## 👤 Author

- Edgar Kolian (https://github.com/kolianedgar)

## 📄 Notes

- This project was developed as part of a Bachelor’s thesis
- Focus on modularity, interpretability, and reproducibility
