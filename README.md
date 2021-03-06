# QuantifyCBF

## Purpose
The `GetHighestAmplitude.py` Python script used to obtain and combine data from multiple excel files for analysis of cilia beat frequency (CBF) as described in [Allan et al. (2021)](https://temporary.link). This script obtains the first amplitude >=3 Hz and <30 Hz from `AveSpectrum*.xlsx` Excel files created by the `Cilia Beat Frequency` MatLab script and combines them into one sheet.

## Requirements 

- `Python 3.0.0+`
- `NumPy`
- `pandas`

## Installation

The easiest way to install Python 3 and required packages (numPy and pandas) is to install [Anaconda](https://docs.continuum.io/anacondaorg/). See https://docs.continuum.io/anaconda/install/ for instructions.

This allows you to run Python through `Terminal` on MacOS/Linux or `Anaconda Prompt` on Windows.

## How to use

Download the `GetHighestAmplitude.py` script and unzip the folder.

The `GetHighestAmplitude.py` script is run using `Terminal` on MacOS/Linux or `Anaconda Prompt` (or `Command Prompt` if Python not installed through Anaconda) on Windows. 

The script is performed on the folder that contains all of the `AveSpectrum*.xlsx` Excel files intended to be analysed. This script can be performed for Excel files with extensions `.xlsx` or `.xml`. 

### MacOS/Linux
In `Terminal` run:

```
python /path/to/script/GetHighestAmplitude.py /path/to/folder
```

### Windows
In `Anaconda Prompt`/`Command Prompt` run:

```
python "path\to\script\GetHighestAmplitude.py" "path\to\folder"
```

## Output

The script will output an Excel file named `HighestAmplitudeCombined.xlsx` in the same input folder. This file contains three columns `frequency`, `Amplitude` and `Source` with rows for each file analysed. 

`frequency` contains the CBF frequency <30 Hz.

`Amplitude` contains the associated CBF amplitude.

`Source` contains the respective filename.

### Example `HighestAmplitudeCombined.xlsx`

| frequency     | Amplitude     | Source                           |
| ------------- |:-------------:| --------------------------------:|
| 9.333333333   | 1.008127      | AveSpectrum_date_cond1_rep1.xlsx |
| 8.333333333   | 1.119657      | AveSpectrum_date_cond1_rep2.xlsx |
| 5.509641873   | 1.471238      | AveSpectrum_date_cond1_rep3.xlsx |
| 6.333333333   | 1.002133      | AveSpectrum_date_cond2_rep1.xlsx |
| 4.333233533   | 0.926174      | AveSpectrum_date_cond2_rep2.xlsx |
| 4.509699973   | 0.923411      | AveSpectrum_date_cond2_rep3.xlsx |
