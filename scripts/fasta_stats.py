import os
from Bio import SeqIO
import matplotlib.pyplot as plt 

# Define variables for plotting
seq_names = []
gc_list = []

input_fasta = "../data/sample_sequences.fasta"
output_file = "../output/sequence_report.txt"

os.makedirs("../output", exist_ok=True)

print("Reading FASTA file...")

seen_sequences = set()

with open(output_file, "w") as out:
    out.write("Gene_Name\tLength\tGC_Content(%)\tAT_Content(%)\tReverse_Complement\tDuplicate\n")

    for record in SeqIO.parse(input_fasta, "fasta"):
        print("Reading record:",record.id)
        seq = record.seq.upper()
        length = len(seq)

        gc = (seq.count("G") + seq.count("C")) / length * 100
        at = (seq.count("A") + seq.count("T")) / length * 100

        rev_comp = str(seq.reverse_complement())

        # Duplicate check
        if seq in seen_sequences:
            duplicate_status = "Yes"
        else:
            duplicate_status = "No"
            seen_sequences.add(seq)

        # Write to output
        out.write(f"{record.id}\t{length}\t{gc:.2f}\t{at:.2f}\t{rev_comp}\t{duplicate_status}\n")

        # For Plotting
        seq_names.append(record.id)
        gc_list.append(gc)

print("Analysis complete. Output saved.")

## ==========================
# GC Content Plot
# ===========================

plt.figure(figsize=(8,5))
plt.bar(seq_names, gc_list, color='skyblue')
plt.xlabel("Sequence Name")
plt.ylabel("GC Content (%)")
plt.title("GC Content per Sequence")
plt.ylim(0, 100)  # optional, percentage scale
plt.tight_layout()
plt.savefig("../output/gc_content_plot.png")  # save figure
plt.show()
print("GC content plot saved as 'gc_content_plot.png' in output folder.")