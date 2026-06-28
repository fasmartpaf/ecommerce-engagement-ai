import os
from datetime import datetime


class ResearchArtifactManager:

    def __init__(self, base_dir):

        self.base_dir = base_dir

        self.diagram_dir = os.path.join(base_dir, "diagrams")
        self.xml_dir = os.path.join(base_dir, "xmls")
        self.report_dir = os.path.join(base_dir, "reports")

        self.ensure_directories()

        self.figure_registry = []

        self.list_of_figures_file = os.path.join(
            self.report_dir,
            "list_of_figures.txt"
        )


    # -----------------------------------------------------
    # Ensure Main Directories
    # -----------------------------------------------------

    def ensure_directories(self):

        os.makedirs(self.diagram_dir, exist_ok=True)
        os.makedirs(self.xml_dir, exist_ok=True)
        os.makedirs(self.report_dir, exist_ok=True)


    # -----------------------------------------------------
    # Initialize Stage
    # -----------------------------------------------------

    def initialize_stage(self, stage_name):

        self.stage_name = stage_name

        self.stage_diagram_dir = os.path.join(self.diagram_dir, stage_name)
        self.stage_xml_dir = os.path.join(self.xml_dir, stage_name)

        os.makedirs(self.stage_diagram_dir, exist_ok=True)
        os.makedirs(self.stage_xml_dir, exist_ok=True)

        self.figure_counter = 1

        self.description_file = os.path.join(
            self.stage_diagram_dir,
            "figure_descriptions.txt"
        )

        self.placement_file = os.path.join(
            self.stage_diagram_dir,
            "thesis_placement_guide.txt"
        )

        self.analysis_notes_file = os.path.join(
            self.report_dir,
            f"{stage_name}_analysis_notes.txt"
        )

        self.write_stage_header()


    # -----------------------------------------------------
    # Stage Header
    # -----------------------------------------------------

    def write_stage_header(self):

        header = f"\nStage: {self.stage_name}\nGenerated: {datetime.now()}\n\n"

        with open(self.description_file, "w") as f:
            f.write(header)

        with open(self.placement_file, "w") as f:
            f.write(header)

        with open(self.analysis_notes_file, "w") as f:
            f.write(header)


    # -----------------------------------------------------
    # Save Figure
    # -----------------------------------------------------

    def save_figure(self, plt, name, chapter, section, purpose):

        figure_number = f"Fig_{chapter}_{self.figure_counter}"

        filename = f"{figure_number}_{name}.png"

        filepath = os.path.join(self.stage_diagram_dir, filename)

        plt.savefig(filepath)
        plt.close()

        print("Figure saved:", filepath)

        self.figure_registry.append({
            "figure": figure_number,
            "title": name,
            "chapter": chapter,
            "section": section,
            "path": filepath
        })

        self.write_description(
            figure_number,
            name,
            purpose
        )

        self.write_placement(
            figure_number,
            chapter,
            section
        )

        self.figure_counter += 1


    # -----------------------------------------------------
    # Figure Description
    # -----------------------------------------------------

    def write_description(self, fig_no, name, purpose):

        with open(self.description_file, "a") as f:

            f.write(f"{fig_no} – {name}\n")
            f.write(f"Purpose: {purpose}\n\n")


    # -----------------------------------------------------
    # Thesis Placement Guide
    # -----------------------------------------------------

    def write_placement(self, fig_no, chapter, section):

        with open(self.placement_file, "a") as f:

            f.write(f"{fig_no}\n")
            f.write(f"Chapter: {chapter}\n")
            f.write(f"Section: {section}\n")
            f.write("Placement: After the relevant discussion paragraph.\n\n")


    # -----------------------------------------------------
    # Analysis Notes
    # -----------------------------------------------------

    def write_analysis_note(self, text):

        with open(self.analysis_notes_file, "a") as f:
            f.write(text + "\n\n")


    # -----------------------------------------------------
    # Generate List of Figures
    # -----------------------------------------------------

    def generate_list_of_figures(self):

        with open(self.list_of_figures_file, "w") as f:

            f.write("LIST OF FIGURES\n\n")

            for fig in self.figure_registry:

                f.write(
                    f"{fig['figure']} – {fig['title']}\n"
                )
                f.write(
                    f"Chapter {fig['chapter']} – {fig['section']}\n"
                )
                f.write(
                    f"File: {fig['path']}\n\n"
                )

        print("List of figures generated:", self.list_of_figures_file)