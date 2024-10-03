from RRD_2024_New_Comparison.FileComparator import FileComparator

if __name__ == "__main__":
    comparator = FileComparator(similarity_threshold=0.75)

    # Example RDF and other file paths
    file_paths = ['/home/rylei/RRD/NewComp/RRD_2024_New_Comparison/TestDocs/testFiles/rtf/A550_rtf/5500_401k_IDVFIL_Main.rtf', '/home/rylei/RRD/NewComp/RRD_2024_New_Comparison/TestDocs/testFiles/rtf/A550_rtf/5500_403b_ERFIL_Main.rtf', '/home/rylei/RRD/NewComp/RRD_2024_New_Comparison/TestDocs/testFiles/rtf/A550_rtf/5500_403b_ERFIL_Footer.rtf']

    comparator.load_files(file_paths)
    comparison_results = comparator.compare_files()

    for result in comparison_results:
        if result:
            print(f"Similarity: {result['similarity']}")
            print(f"Differences:\n{result['differences']}\n")
