import difflib
import os


# Function to load files
def load_file(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()


# Function to compare two files and generate a diff
def compare_two_files(file1_content, file2_content):
    diff = difflib.unified_diff(file1_content, file2_content, lineterm='', n=0)
    diff_list = list(diff)

    total_lines = len(file1_content) + len(file2_content)
    matching_lines = total_lines - len(diff_list)
    similarity = matching_lines / total_lines if total_lines > 0 else 1  # Avoid division by zero

    return diff_list, similarity


# Function to save the comparison to a file
def save_diff_to_file(diff, similarity, output_file):
    with open(output_file, 'w') as f:
        f.write("Differences:\n")
        f.writelines(diff)
        f.write("\n\nSimilarity: {:.2f}%\n".format(similarity * 100))


# Main function to orchestrate the comparison
def compare_rdf_files(file1_path, file2_path, file3_path, output_file, similarity_threshold=0.8):
    file1_content = load_file(file1_path)
    file2_content = load_file(file2_path)
    file3_content = load_file(file3_path)

    # Compare file 1 with file 2
    diff1, similarity1 = compare_two_files(file1_content, file2_content)

    # Compare file 1 with file 3
    diff2, similarity2 = compare_two_files(file1_content, file3_content)

    # Check if similarity exceeds the threshold for both comparisons
    if similarity1 >= similarity_threshold:
        save_diff_to_file(diff1, similarity1, output_file + "_1_2.txt")
    else:
        print(f"File1 and File2 are too dissimilar (similarity = {similarity1:.2f})")

    if similarity2 >= similarity_threshold:
        save_diff_to_file(diff2, similarity2, output_file + "_1_3.txt")
    else:
        print(f"File1 and File3 are too dissimilar (similarity = {similarity2:.2f})")


# Example usage
file1 = "C:/Users/rymin/NewRRD/RRD_2024_New_Comparison/Runnin/testfiles/testFiles/rtf/5500_rtf/5500_401k_IDVFIL_Footer.rtf"
file2 = "C:/Users/rymin/NewRRD/RRD_2024_New_Comparison/Runnin/testfiles/testFiles/rtf/5500_rtf/5500_401k_IDVFIL_Main.rtf"
file3 = "C:/Users/rymin/NewRRD/RRD_2024_New_Comparison/Runnin/testfiles/testFiles/rtf/A550_rtf/5500_401k_IDVFIL_Main.rtf"
output = "C:/Users/rymin/NewRRD/RRD_2024_New_Comparison/Runnin/return"
compare_rdf_files(file1, file2, file3, output, similarity_threshold=0.75)
