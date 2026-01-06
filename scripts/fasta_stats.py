from Bio import SeqIO

input_fasta = "../data/sample_sequences.fasta"
output_file = "../output/sequence_report.txt"

print("Reading FASTA file...")

with open(output_file, "w") as out:
    out.write("Gene_Name\tLength\tGC_Content(%)\n")

    for record in SeqIO.parse(input_fasta, "fasta"):
        seq = record.seq
        length = len(seq)
        gc = (seq.count("G") + seq.count("C")) / length * 100

        out.write(f"{record.id}\t{length}\t{gc:.2f}\n")

print("Analysis complete. Output saved.")