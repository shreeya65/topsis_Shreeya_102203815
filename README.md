# TOPSIS Implementation

## Program 1: Command Line Implementation
Command to run:
```bash
python <RollNumber>.py <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

Example:
```bash
python 102203815-topsis.py 102203815-data.csv "1,1,1,2,1" "+,+,-,+,+" 102203815-result.csv
```


### Input Requirements
- Input CSV file must have 3+ columns
- First column: Object names (M1, M2, etc.)
- 2nd column onwards: Numeric values only
- Weights: Comma-separated (e.g., "0.2,0.2,0.2,0.2,0.2")
- Impacts: Comma-separated +/- (e.g., "+,+,+,+,+")

### Error Handling
- Checks for correct parameter count
- File existence verification
- Numeric values validation
- Weights and impacts count validation
- Impact symbols must be + or -

## Program 2: PyPI Package
This implementation is available as a Python package on [`https://pypi.org/project/Topsis-Shreeya-102203815/1.0.0/`](https://pypi.org/project/Topsis-Shreeya-102203815/1.0.0/). You can easily install it via `pip`:

```bash
pip install Topsis-Shreeya-102203815==1.0.0
```
---


## Requirements
- Python
- pandas
- numpy

## Author
Name: Shreeya Kesarwani
Roll Number: 102203815****
