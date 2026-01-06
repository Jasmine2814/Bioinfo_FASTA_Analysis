import os
from Bio import SeqIO

input_fasta = "../data/sample_sequences.fasta"
output_file = "../output/sequence_report.txt"

os.makedirs("../output", exist_ok=True)

print("Reading FASTA file...")

seen_sequences = set()

with open(output_file, "w") as out:
    out.write("Gene_Name\tLength\tGC_Content(%)\tAT_Content(%)\tReverse_Complement\tDuplicate\n")

    for record in SeqIO.parse(input_fasta, "fasta"):
        seq = record.seq.upper()
        length = len(seq)

        gc = (seq.count("G") + seq.count("C")) / length * 100
        at = (seq.count("A") + seq.count("T")) / length * 100

        rev_comp = str(seq.reverse_complement())

        if seq in seen_sequences:
            duplicate_status = "Yes"
        else:
            duplicate_status = "No"
            seen_sequences.add(seq)

        out.write(f"{record.id}\t{length}\t{gc:.2f}\t{at:.2f}\t{rev_comp}\t{duplicate_status}\n")

print("Analysis complete. Output saved.")