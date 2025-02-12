# Function to reindex annotations in text files based on a standard label map.

import yaml
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def reindex_annotations(annotation_folder, data_yaml_file, standard_label_map):
    """
    Reindex annotations in text files based on a standard label map.

    This function reads annotation files from a specified folder, updates the class indices
    according to a provided standard label map, and writes the updated annotations back to the files.
    It also logs the changes made to the class indices.

    Args:
        annotation_folder (str): Path to the folder containing annotation text files.
        data_yaml_file (str): Path to the YAML file containing current label names.
        standard_label_map (dict): A dictionary mapping current label names to new indices.

    Returns:
        None
    """
    # Load current YAML to get the current labels
    with open(data_yaml_file, "r") as f:
        data = yaml.safe_load(f)

    # Extract the current mapping (label names and current index)
    current_label_map = {name: idx for idx, name in enumerate(data["names"])}
    logging.info("Current Label Mapping: %s", current_label_map)

    # Iterate through all the files in the annotation folder
    for filename in os.listdir(annotation_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(annotation_folder, filename)

            # Read all lines from the file
            with open(file_path, "r") as file:
                lines = file.readlines()

            new_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) < 5:
                    continue

                old_index = int(parts[0])
                old_label_name = data["names"][old_index]
                new_index = standard_label_map[old_label_name]

                if old_index == new_index:
                    logging.info(
                        "File: %s - Class '%s' remains the same with index %d",
                        filename,
                        old_label_name,
                        old_index,
                    )
                else:
                    logging.info(
                        "File: %s - Class '%s' changed from index %d to %d",
                        filename,
                        old_label_name,
                        old_index,
                        new_index,
                    )

                new_line = f"{new_index} {' '.join(parts[1:])}"
                new_lines.append(new_line)

            # Write the updated lines back to the file
            with open(file_path, "w") as file:
                file.write("\n".join(new_lines))

    logging.info("COMPLETED")


# Driver
standard_label_map = {
    "angryface": 0,
    "auto": 1,
    "bicycle": 2,
    "bus": 3,
    "car": 4,
    "happyface": 5,
    "motorcycle": 6,
    "neutralface": 7,
    "numberplate": 8,
    "person": 9,
    "pole": 10,
    "road": 11,
    "sadface": 12,
    "sidewalk": 13,
    "truck": 14,
    "van": 15,
    "road_cross": 16,
}

# Path of the files
list_annotation_folder = [
    "/Users/akb/Desktop/CV_GenAi/Project/visionaid/VisionAVI-Dataset/RoboflowData/kishor/train/labels"
]

list_data_yaml_file = [
    "/Users/akb/Desktop/CV_GenAi/Project/visionaid/VisionAVI-Dataset/RoboflowData/kishor/data.yaml"
]

for i in range(len(list_annotation_folder)):
    reindex_annotations(
        list_annotation_folder[i], list_data_yaml_file[i], standard_label_map
    )
