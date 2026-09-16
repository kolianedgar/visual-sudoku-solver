# Modular Hybrid AI System for Solving Visual Sudoku

This repository contains the implementation of my **Bachelor's thesis**, which presents a modular artificial intelligence system for solving Sudoku puzzles directly from images.

The system combines **computer vision, deep learning, and classical algorithmic search** into a single pipeline. Rather than relying on an end-to-end model, each stage performs a specific task and passes its output to the next component, making the overall system easier to interpret, evaluate, and extend.

---

## Project Overview

The system processes a Sudoku puzzle from an input image through several stages:

```text
Input Image
     │
     ▼
Image Preprocessing
     │
     ▼
Sudoku Grid Extraction
     │
     ▼
Cell Segmentation
     │
     ▼
Digit Recognition
     │
     ▼
Sudoku Grid Reconstruction
     │
     ▼
Backtracking Solver
     │
     ▼
Solved Sudoku
     │
     ▼
Visualisation / Export
```

The main components are:

* **Image processing** — extracts the Sudoku grid from an image and prepares individual cells.
* **Digit recognition** — uses a convolutional neural network (CNN) to identify handwritten digits.
* **Sudoku solving** — applies depth-first search (DFS) with backtracking to find a valid solution.
* **Interactive solving** — provides step-by-step and partial-solution functionality.
* **Result generation** — allows solved puzzles to be exported as images.

The modular structure separates perception from reasoning, allowing individual components to be evaluated and improved independently.

---

## Objectives

The main objective of the thesis was to develop a **robust and interpretable system for solving visual Sudoku puzzles** by combining machine learning with traditional algorithmic techniques.

The project specifically investigates the integration of:

* image preprocessing and computer vision;
* neural networks for handwritten digit recognition;
* classical search algorithms for Sudoku solving; and
* interactive visualisation of the solving process.

The resulting system demonstrates how machine learning and deterministic algorithms can be combined within a single application.

---

## System Components

### 1. Image Processing

The first stage converts the input Sudoku image into a representation suitable for digit recognition.

The preprocessing pipeline includes:

* image preprocessing;
* contour detection;
* border dilation;
* Sudoku grid extraction; and
* segmentation of the grid into individual cells.

The objective of this stage is to isolate the Sudoku board and produce individual cell images that can be passed to the digit recognition model.

---

### 2. Digit Recognition

A convolutional neural network (CNN) is used to classify the digits contained within Sudoku cells.

The implemented model uses an **8-layer architecture** and is trained for handwritten digit classification.

The recognised digits are subsequently used to reconstruct the numerical Sudoku grid required by the solving algorithm.

---

### 3. Sudoku Solver

Once the Sudoku grid has been reconstructed, the puzzle is solved using **depth-first search (DFS) with backtracking**.

The solver recursively explores possible values for empty cells and backtracks whenever a choice produces an invalid configuration.

This approach was selected because it provides:

* a simple deterministic solving procedure;
* straightforward integration with the digit-recognition pipeline; and
* an interpretable sequence of decisions during solving.

The solver operates independently from the neural network, allowing the recognition and reasoning components to be evaluated separately.

---

### 4. Interactive Module

The system also includes functionality for interacting with the solving process.

Supported functionality includes:

* step-by-step solving;
* partial solution reveals; and
* exporting solved puzzles as images.

This provides a more interpretable representation of the solving process than simply returning a final Sudoku grid.

---

## Experimental Results

The system was evaluated across its major components.

### Image Processing

**Image preprocessing accuracy:**

> **98.8%**

### Digit Recognition

**Combined digit recognition accuracy:**

> **95.27%**

### Overall System

The reported overall system accuracy was:

| Configuration                     |   Accuracy |
| --------------------------------- | ---------: |
| Without difficulty classification | **95.27%** |
| With difficulty classification    | **66.97%** |

### Difficulty Classification

The difficulty classification component achieved:

> **38.67% accuracy**

The results show that the main visual Sudoku pipeline performed substantially differently depending on whether difficulty classification was included in the system.

---

## Repository Structure

```text
visual-sudoku-solver/
│
├── Puzzles/
│   ├── easy/
│   ├── easy_printed/
│   ├── hard/
│   ├── hard_printed/
│   ├── moderate/
│   └── moderate_printed/
│
├── Python Code/
│   ├── Combined_full.py
│   ├── Preprocessing_full.py
│   ├── Save_Solution_as_Image.py
│   ├── graphs.py
│   ├── solve_sudoku.py
│   └── utils_MNIST_Classify.py
│
├── Report Images/
│   ├── Implementation_Final/
│   └── Implementation_initial/
│
├── sudoku_digits/
│
├── Classification Results (version 1).xlsx
├── LICENSE
└── README.md
```

### Main directories

* **`Puzzles/`** — Sudoku puzzle images organised by difficulty and image type.
* **`Python Code/`** — Core implementation of preprocessing, classification, solving, visualisation, and image export.
* **`Report Images/`** — Images generated or collected during the development and evaluation of the thesis system.
* **`sudoku_digits/`** — Digit data used by the recognition component.
* **`Classification Results (version 1).xlsx`** — Experimental classification results.

---

## Setup

Clone the repository:

```bash
git clone https://github.com/kolianedgar/visual-sudoku-solver.git
cd visual-sudoku-solver
```

Install the required Python dependencies used by the project.

The exact execution procedure may depend on the local environment and the particular component being evaluated.

---

## Running the System

The main implementation is located in the **`Python Code/`** directory.

The primary components include:

```text
Preprocessing_full.py
Combined_full.py
solve_sudoku.py
Save_Solution_as_Image.py
utils_MNIST_Classify.py
```

Their roles are broadly:

* `Preprocessing_full.py` — image preprocessing and Sudoku grid extraction.
* `Combined_full.py` — combined processing and recognition pipeline.
* `solve_sudoku.py` — Sudoku solving using DFS and backtracking.
* `Save_Solution_as_Image.py` — generation/export of solved puzzle images.
* `utils_MNIST_Classify.py` — utilities related to digit classification.
* `graphs.py` — generation of evaluation graphs.

---

## Experimental Data

The repository contains Sudoku puzzle images representing different difficulty levels:

```text
Puzzles/
├── easy/
├── easy_printed/
├── moderate/
├── moderate_printed/
├── hard/
└── hard_printed/
```

The dataset contains both handwritten and printed Sudoku examples, allowing the recognition pipeline to be evaluated under different visual conditions.

---

## Evaluation

The system evaluates several distinct components rather than treating the entire pipeline as a single black-box model.

The evaluation covers:

1. **Image preprocessing**
2. **Digit recognition**
3. **Difficulty classification**
4. **Overall Sudoku solving performance**

This separation makes it possible to identify where errors are introduced within the pipeline.

For example, an incorrectly recognised digit can result in an invalid reconstructed Sudoku grid even when the underlying solving algorithm is able to solve the puzzle correctly.

---

## Challenges

Several practical challenges were encountered during development:

* limited computational resources;
* inconsistencies within the available datasets;
* challenges associated with handwritten digit recognition;
* limited initial experience with deep learning; and
* integration between neural-network-based recognition and classical Sudoku solving.

These constraints influenced both the experimental design and the final system architecture.

---

## Future Improvements

Potential extensions to the system include:

* larger and more diverse training datasets;
* synthetically generated Sudoku images;
* improved handwritten digit recognition;
* a dedicated graphical user interface;
* more advanced Sudoku solving techniques;
* constraint satisfaction problem (CSP) approaches;
* Algorithm X / Dancing Links;
* and improved difficulty classification.

These extensions could improve robustness while also providing alternative approaches for comparing neural and classical components.

---

## Reproducibility

The repository contains the implementation, puzzle data, trained model, and experimental outputs used during development of the thesis system.

The modular organisation allows individual stages of the pipeline to be inspected and evaluated independently.

The reported results can therefore be traced back to specific components of the system, including preprocessing, digit classification, and Sudoku solving.

---

## License

This project is licensed under the **MIT License**.

See [`LICENSE`](LICENSE) for the full license text.

---

## Academic Context

This project was developed as part of a **Bachelor's thesis**.

The work focuses on the integration of:

* computer vision;
* deep learning;
* image classification;
* algorithmic search; and
* interpretable AI systems.

The central design principle is **modularity**: visual perception and algorithmic reasoning are implemented as separate components that can be evaluated and improved independently.

---

## Author

* **Edgar Kolian** (github.com/kolianedgar)
