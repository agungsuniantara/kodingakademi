# System Context: FaunaRescue - Predictive Action System

## 1. Project Identity & Context
- **Team Name:** Binary
- **Competition:** International Code Olympiad (ICO) 2026 - Semifinal Round[cite: 1]
- **Category:** Python Category[cite: 1]
- **Sub-theme:** Digital Nature Creators[cite: 1]
- **Case Study:** Overexploitation (Direct Exploitation of Species)[cite: 1]
- **Project Goal:** A desktop GUI application that educates users on endangered species by translating static conservation statuses (CR, EN, VU) from a local dataset into dynamic, mathematical population simulations. The app demonstrates how human interventions can reverse extinction trajectories.

## 2. Tech Stack & Strict Limitations
- **Language:** Python 3
- **GUI Framework:** `Tkinter` (Strictly no PyQt or other external GUI libraries)[cite: 1].
- **Data Processing & Math:** `NumPy`[cite: 1].
- **Data Visualization:** `Matplotlib` (Embedded within Tkinter using `FigureCanvasTkAgg`)[cite: 1].
- **Data Storage/Loading:** Built-in `csv` module[cite: 1].
- **ABSOLUTE RULE:** DO NOT use any other third-party libraries (e.g., pandas, scikit-learn, requests, sqlalchemy) as per competition rules[cite: 1]. DO NOT use SQLite; strictly use in-memory data structures.

## 3. Data Architecture (In-Memory Knowledge Base)
- **Source File:** `filtered_data.csv` (Contains taxonomic data and IUCN Red List categories).
- **Loading Mechanism:** Upon initialization, the app must read the CSV file using the built-in `csv` module and store the data in a Python `Dictionary` for rapid, in-memory access.
- **Search Logic (CRITICAL):** When implementing the search function for the knowledge base, the logic **MUST prioritize returning exact matches** from the local dictionary over generating fuzzy or LLM-based responses. Exact keyword matching (on `main_common_name` or `scientific_name`) is the primary retrieval method. 

## 4. Core Features & Algorithms

### A. Ecosystem Knowledge Base (Search & Discover)
- A Tkinter search bar where users input an animal's name.
- Retrieves data from the loaded dictionary using exact match logic.

### B. Extinction vs. Survival Predictor (NumPy Simulation)
- The algorithm maps the conservation `category` from the CSV to actual IUCN Red List quantitative thresholds (Version 3.1) to completely eliminate data hallucination[cite: 2, 4]:
  - **`CR` (Critically Endangered):** 
    - Initial Population = 250 (Based on IUCN Criterion C)[cite: 4].
    - Base Decay Rate = -14.86% per year (Derived from IUCN Criterion A: 80% reduction over 10 years)[cite: 4].
  - **`EN` (Endangered):** 
    - Initial Population = 2500 (Based on IUCN Criterion C)[cite: 4].
    - Base Decay Rate = -6.69% per year (Derived from IUCN Criterion A: 50% reduction over 10 years)[cite: 4].
  - **`VU` (Vulnerable):** 
    - Initial Population = 10000 (Based on IUCN Criterion C)[cite: 4].
    - Base Decay Rate = -3.49% per year (Derived from IUCN Criterion A: 30% reduction over 10 years)[cite: 4].
- Uses `NumPy` arrays to mathematically project the population decay over a 10 to 20-year timeline based on these official compound annual decline rates.

### C. Rescue Timeline Visualization (Matplotlib)
- Plots the `NumPy` arrays on a Matplotlib figure embedded in Tkinter.
- **Red Line:** Represents the default trajectory towards extinction (Baseline Scenario based on IUCN decay rates).
- **Green Line:** Represents the recovery trajectory after user interventions (Rescue Scenario).

### D. Interactive Rescue Modules (Intervention Panel)
- Tkinter checkboxes representing rescue actions (e.g., "Stop Poaching", "Fund Captive Breeding").
- Checking a box adds a positive modifier to the Base Decay Rate (e.g., +8%, +5%).
- Triggering these checkboxes recalculates the `NumPy` array and re-renders the Matplotlib graph in real-time.

## 5. Coding Guidelines for AI Agent
- **Modularity:** Separate the data loading logic (`csv` to dict), mathematical simulation logic (`numpy`), and GUI presentation (`tkinter` + `matplotlib`) into distinct classes or functions.
- **Performance:** Ensure Matplotlib figures are properly cleared (`ax.clear()`) before re-drawing to prevent memory leaks in the Tkinter mainloop.
- **Simplicity:** Favor clear, readable Python code over overly complex one-liners. Emphasize strong algorithmic logic (for NumPy) over brute-force calculations.