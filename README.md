# Demo FASTA Analysis Project

## Purpose
This demo project was created to practice Linux file handling and basic bioinformatics analysis using Python.

## Tools Used
- Linux Terminal
- Python 3
- BioPython

## Project Structure
- data/: demo FASTA sequences
- scripts/: Python script for analysis
- output/: generated result file

## Analysis Performed
- Calculated sequence length
- Calculated GC content (%)
- Calculated AT content (%)
- Generated reverse complement of each sequence

## How to Run
cd scripts  
python3 fasta_stats.py

## Outcome
The script reads FASTA sequences and generates a tab-separated report containing:
- Sequence name
- Length
- GC content (%)
- AT content (%)
- Reverse complement

## Note
- This project uses small demo sequences for learning purposes.
- The output file can be opened in any text editor or terminal.
- AT content and GC content are rounded to two decimal places.

## Future Improvements
- Sequence validation (check for invalid bases)
- Duplicate sequence detection
- ORF (Open Reading Frame) analysis
- GC content plot using matplotlib


## Sample Output

<table>
  <tr>
    <th>Gene_Name</th>
    <th>Length</th>
    <th>GC_Content(%)</th>
    <th>AT_Content(%)</th>
    <th>Reverse_Complement</th>
  </tr>
  <tr>
    <td>Gene_A</td>
    <td>20</td>
    <td>50.00</td>
    <td>50.00</td>
    <td>CTAGCTAGCTACGTACGCAT</td>
  </tr>
  <tr>
    <td>Gene_B</td>
    <td>15</td>
    <td>46.67</td>
    <td>53.33</td>
    <td>TAGCTAGCTACGCAT</td>
  </tr>
</table>