
# TOPSIS Analysis for Text Summarization Models

This repository contains the analysis of various text summarization models using the TOPSIS method.

## Overview
TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) is a multi-criteria decision-making method to rank models based on performance metrics.

## Models Evaluated
- GPT-4
- Pegasus
- BART
- T5
- DistilBART

## Criteria Used
- **ROUGE Score** (Higher is better)
- **Compression Ratio** (Lower is better)
- **Latency** (Lower is better)
- **Model Size** (Lower is better)
- **Inference Cost** (Lower is better)

## Results
| Model         | Topsis Score | Rank |
|---------------|--------------|------|
| GPT-4         | 0.752        | 1    |
| Pegasus       | 0.690        | 2    |
| BART          | 0.660        | 3    |
| T5            | 0.583        | 4    |
| DistilBART    | 0.500        | 5    |

## How to Run
1. Install Python dependencies:  
   pip install pandas numpy
2. Save your dataset as a CSV file.
3. Execute the script:  
   
   python topsis.py <input_file> <weights> <impacts> <output_file>



