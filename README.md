# Demo FASTA Analysis Project

## Purpose
This demo project was created to practice Linux file handling and basic bioinformatics analysis using Python.

## Tools Used
- Linux Terminal
- Python 3
- BioPython
- Matplotlib (for GC content plot)

## Project Structure
- data/: demo FASTA sequences
- scripts/: Python script for analysis
- output/: generated result file

## Analysis Performed
- Calculated sequence length
- Calculated GC content (%)
- Calculated AT content (%)
- Generated reverse complement of each sequence
- Duplicate sequence detection
- GC content plot using matplotlib

## How to Run
```bash
cd scripts  
python3 fasta_stats.py

## Outcome
The script reads FASTA sequences and generates a tab-separated report containing:
- Sequence name
- Length
- GC content (%)
- AT content (%)
- Reverse complement
- Duplicate sequence detection
- GC content plot is generated in output/gc_content_plot.png.
## Note
- This project uses small demo sequences for learning purposes.
- The output file can be opened in any text editor or terminal.
- AT content and GC content are rounded to two decimal places.

## Future Improvements
- Sequence validation (check for invalid bases)
- ORF (Open Reading Frame) analysis
- Additional plots(e.g., AT content plot)


## Sample Output

The script generates a tab-separated report ('sequence_report.txt') and a GC content plot ('gc_content_plot.png) in the 'output/' folder.
See 'sample_output.txt' for an example of the generated report.
The GC content plot visualize the GC percentage of each sequence.

<table>
  <tr>
    <th>Gene_Name</th>
    <th>Length</th>
    <th>GC_Content(%)</th>
    <th>AT_Content(%)</th>
    <th>Reverse_Complement</th>
    <th>Duplicate</th>
  </tr>
  <tr>
    <td>Gene_A</td>
    <td>20</td>
    <td>50.00</td>
    <td>50.00</td>
    <td>CTAGCTAGCTACGTACGCAT</td>
    <td>No</td>
  </tr>
  <tr>
    <td>Gene_B</td>
    <td>15</td>
    <td>46.67</td>
    <td>53.33</td>
    <td>TAGCTAGCTACGCAT</td>
    <td>No</td>
  </tr>
  <tr>
    <td>Gene_C</td>
    <td>24</td>
    <td>50.00</td>
    <td>50.00</td>
    <td>CTAGCTAGCTAGCTACGTACGCAT</td>
    <td>No</td>
  </tr>
</table>

See 'sample_output.txt' for an example of the generated report.