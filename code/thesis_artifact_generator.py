import os
import xml.etree.ElementTree as ET
from datetime import datetime


BASE_DIR = r"d:\ecom_data"

DIAGRAM_DIR = os.path.join(BASE_DIR, "diagrams")
XML_DIR = os.path.join(BASE_DIR, "xmls")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(REPORT_DIR, exist_ok=True)


class ThesisArtifactGenerator:

    def __init__(self):

        self.figures = []

    # -------------------------------------------------------
    # Scan Figures
    # -------------------------------------------------------

    def scan_figures(self):

        print("\nScanning figures...\n")

        for root, dirs, files in os.walk(DIAGRAM_DIR):

            for file in files:

                if file.endswith(".png"):

                    full_path = os.path.join(root, file)

                    fig_name = file.replace(".png", "")

                    parts = fig_name.split("_")

                    chapter = parts[1] if len(parts) > 1 else "?"

                    title = " ".join(parts[2:]) if len(parts) > 2 else fig_name

                    self.figures.append({
                        "file": file,
                        "title": title,
                        "chapter": chapter,
                        "path": full_path
                    })

        print("Figures detected:", len(self.figures))

    # -------------------------------------------------------
    # List of Figures
    # -------------------------------------------------------

    def generate_list_of_figures(self):

        file = os.path.join(REPORT_DIR, "list_of_figures.txt")

        with open(file, "w") as f:

            f.write("LIST OF FIGURES\n\n")

            for i, fig in enumerate(self.figures, 1):

                f.write(
                    f"Figure {fig['chapter']}.{i} – {fig['title']}\n"
                )

        print("Generated:", file)

    # -------------------------------------------------------
    # Figure Captions
    # -------------------------------------------------------

    def generate_captions(self):

        file = os.path.join(REPORT_DIR, "figure_captions.txt")

        with open(file, "w") as f:

            f.write("FIGURE CAPTIONS\n\n")

            for i, fig in enumerate(self.figures, 1):

                caption = (
                    f"Figure {fig['chapter']}.{i}: "
                    f"{fig['title']} showing relevant patterns "
                    f"in customer behaviour data."
                )

                f.write(caption + "\n\n")

        print("Generated:", file)

    # -------------------------------------------------------
    # Thesis Placement Guide
    # -------------------------------------------------------

    def generate_placement_guide(self):

        file = os.path.join(REPORT_DIR, "thesis_placement_guide.txt")

        with open(file, "w") as f:

            f.write("THESIS FIGURE PLACEMENT GUIDE\n\n")

            for i, fig in enumerate(self.figures, 1):

                f.write(
                    f"Figure {fig['chapter']}.{i}\n"
                    f"Suggested Chapter: {fig['chapter']}\n"
                    f"File: {fig['path']}\n\n"
                )

        print("Generated:", file)

    # -------------------------------------------------------
    # XML Analysis
    # -------------------------------------------------------

    def analyze_xml(self):

        summary = {}

        for root, dirs, files in os.walk(XML_DIR):

            for file in files:

                if file.endswith(".xml"):

                    path = os.path.join(root, file)

                    try:

                        tree = ET.parse(path)

                        root_node = tree.getroot()

                        summary[file] = len(root_node)

                    except:

                        summary[file] = "Error"

        file = os.path.join(REPORT_DIR, "xml_summary.txt")

        with open(file, "w") as f:

            f.write("XML DATA SUMMARY\n\n")

            for k, v in summary.items():

                f.write(f"{k}: {v} entries\n")

        print("Generated:", file)

    # -------------------------------------------------------
    # Research Summary
    # -------------------------------------------------------

    def research_summary(self):

        file = os.path.join(REPORT_DIR, "research_summary.txt")

        with open(file, "w") as f:

            f.write("RESEARCH SUMMARY\n\n")

            f.write(
                "This research analyses customer engagement patterns "
                "in e-commerce platforms using statistical analysis, "
                "machine learning models, and customer segmentation.\n\n"
            )

            f.write(
                "Key objectives:\n"
                "- Understand purchasing behaviour\n"
                "- Predict customer engagement\n"
                "- Discover hidden customer segments\n"
                "- Identify engagement drivers\n\n"
            )

            f.write(
                "Outputs include statistical figures, ML experiment "
                "results, segmentation analysis, and explainable AI insights."
            )

        print("Generated:", file)

    # -------------------------------------------------------
    # Master Report
    # -------------------------------------------------------

    def master_report(self):

        file = os.path.join(REPORT_DIR, "thesis_artifact_report.txt")

        with open(file, "w") as f:

            f.write("THESIS ARTIFACT REPORT\n")
            f.write("=====================\n\n")

            f.write(f"Generated: {datetime.now()}\n\n")

            f.write(f"Total Figures: {len(self.figures)}\n")

            f.write(f"Diagram Folder: {DIAGRAM_DIR}\n")
            f.write(f"XML Folder: {XML_DIR}\n\n")

            f.write(
                "Artifacts Generated:\n"
                "- List of Figures\n"
                "- Figure Captions\n"
                "- Thesis Placement Guide\n"
                "- XML Research Summary\n"
                "- Research Summary\n"
            )

        print("Generated:", file)

    # -------------------------------------------------------

    def run(self):

        self.scan_figures()

        self.generate_list_of_figures()

        self.generate_captions()

        self.generate_placement_guide()

        self.analyze_xml()

        self.research_summary()

        self.master_report()


# -------------------------------------------------------------

if __name__ == "__main__":

    generator = ThesisArtifactGenerator()

    generator.run()