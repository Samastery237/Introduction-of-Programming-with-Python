import csv
import numpy as np
from PIL import Image

def main():
    with open("view.csv", "r") as views, open("analysis.csv", "w") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()

        for row in reader:
            row["brightness"] = round(calculate_brightness(f"{row['id']}.png"), 2)
            writer.writerow(row)
        
def calculate_brightness(filename):
    with Image.open(filename) as img: 
        brightness = np.mean(np.array(img.convert("L"))) / 255
    return brightness

main()