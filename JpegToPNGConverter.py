import sys
import os
from PIL import Image

# Check the Input Parameter
if len(sys.argv) < 2:
    print(f'Number of argument {sys.argv} is less than 2')
    exit(1)

Current_directory = os.getcwd()
# Current jpeg Image files folder
jpeg_dir = sys.argv[1]
Full_JPEG_Path = os.path.join(Current_directory, jpeg_dir)

# New PNG folder path after
png_dir = sys.argv[2]
Full_PNG_Path = os.path.join(Full_JPEG_Path, png_dir)

# Check whether jpeg and png directory exist or not
if os.path.exists(Full_JPEG_Path):
    All_files = os.listdir(Full_JPEG_Path)

    if not os.path.exists(Full_PNG_Path):
        os.mkdir(Full_PNG_Path)
        os.chmod(Full_PNG_Path, 0o777)

    for fil in All_files:
        try:
            f, e = os.path.splitext(fil)
            output_file = f + ".png"
            full_out_path = os.path.join(Full_PNG_Path, output_file)
            full_file_path = os.path.join(Full_JPEG_Path, fil)
            if os.path.exists(full_out_path):
                os.remove(full_out_path)
            if os.path.isfile(full_file_path):
                img = Image.open(full_file_path)
                convt_img=img.convert('L')
                if img.format.lower() in ['jpeg', 'jpg']:
                    convt_img.save(full_out_path, 'png')
        except FileNotFoundError as err:
            print(f'file not found pipgive correct file {err}')
else:
    print('JPEG File path is not present')
