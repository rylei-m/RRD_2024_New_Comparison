import difflib
import os


# Function to filter out irrelevant files based on name patterns
def is_relevant_file(file_name, irrelevant_patterns=["header", "footer", "logo"]):
    return not any(pattern in file_name.lower() for pattern in irrelevant_patterns)


# Function to load files
def load_file(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()


# Function to compare two files and generate a diff
def compare_files(file1_content, file2_content, threshold=0.8):
    diff = difflib.unified_diff(file1_content, file2_content, lineterm='', n=0)
    diff_list = list(diff)

    total_lines = len(file1_content) + len(file2_content)
    matching_lines = total_lines - len(diff_list)
    similarity = matching_lines / total_lines

    return diff_list, similarity


# Function to save the comparison to a file
def save_diff_to_file(diff, similarity, output_file):
    with open(output_file, 'w') as f:
        f.write("Differences:\n")
        f.writelines(diff)
        f.write("\n\nSimilarity: {:.2f}%\n".format(similarity * 100))


# Main function to orchestrate the comparison
def compare_rdf_files(file1_path, file2_path, output_file, similarity_threshold=0.8):
    if not is_relevant_file(file1_path) or not is_relevant_file(file2_path):
        print("Skipping irrelevant files.")
        return

    file1_content = load_file(file1_path)
    file2_content = load_file(file2_path)

    diff, similarity = compare_files(file1_content, file2_content, similarity_threshold)

    if similarity >= similarity_threshold:
        save_diff_to_file(diff, similarity, output_file)
    else:
        print(f"Files are too dissimilar (similarity = {similarity:.2f})")


# Example usage
file1 = "rdf_file1.rdf"
file2 = "rdf_file2.rdf"
output = "diff_output.txt"

compare_rdf_files(file1, file2, output, similarity_threshold=0.75)
