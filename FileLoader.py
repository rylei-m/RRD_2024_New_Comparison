from RRD_2024_New_Comparison.FileComparator import FileComparator

if __name__ == "__main__":
    comparator = FileComparator(similarity_threshold=0.75)

    # Example RDF and other file paths
    file_paths = ['file1.rdf', 'file2.rdf', 'file1.docx']

    comparator.load_files(file_paths)
    comparison_results = comparator.compare_files()

    for result in comparison_results:
        if result:
            print(f"Similarity: {result['similarity']}")
            print(f"Differences:\n{result['differences']}\n")
