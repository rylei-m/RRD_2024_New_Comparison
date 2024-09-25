import os
import docx
import fitz  # PyMuPDF for PDFs
import re
from difflib import SequenceMatcher
from rdflib import Graph


class FileComparator:
    def __init__(self, similarity_threshold=0.8, keywords=None):
        self.similarity_threshold = similarity_threshold
        self.keywords = keywords or []
        self.file_contents = []

    def load_files(self, file_paths):
        for path in file_paths:
            if path.endswith('.txt'):
                self.file_contents.append(self._load_txt(path))
            elif path.endswith('.docx'):
                self.file_contents.append(self._load_docx(path))
            elif path.endswith('.pdf'):
                self.file_contents.append(self._load_pdf(path))
            elif path.endswith('.rdf'):
                self.file_contents.append(self._load_rdf(path))
            # Add more formats as needed

    def _load_txt(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()

    def _load_docx(self, path):
        doc = docx.Document(path)
        return "\n".join([para.text for para in doc.paragraphs])

    def _load_pdf(self, path):
        doc = fitz.open(path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text

    def _load_rdf(self, path):
        g = Graph()
        g.parse(path, format="xml")
        rdf_content = ""
        for subj, pred, obj in g:
            rdf_content += f"{subj} {pred} {obj}\n"
        return rdf_content

    def compare_files(self):
        comparisons = []
        for i in range(len(self.file_contents)):
            for j in range(i + 1, len(self.file_contents)):
                result = self._compare(self.file_contents[i], self.file_contents[j])
                comparisons.append(result)
        return comparisons

    def _compare(self, text1, text2):
        similarity = self._calculate_similarity(text1, text2)
        if similarity >= self.similarity_threshold:
            highlighted_diff = self._highlight_differences(text1, text2)
            return {
                "similarity": similarity,
                "differences": highlighted_diff
            }
        return None

    def _calculate_similarity(self, text1, text2):
        return SequenceMatcher(None, text1, text2).ratio()

    def _highlight_differences(self, text1, text2):
        # This will return a diff highlighting the differences
        return "\n".join(re.findall(r'(?=\b(\w+)\b)', text1 + "\n" + text2))

    def keyword_analysis(self):
        keyword_matches = {}
        for content in self.file_contents:
            for keyword in self.keywords:
                if keyword.lower() in content.lower():
                    keyword_matches[keyword] = content
        return keyword_matches
