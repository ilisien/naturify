import os, zipfile, requests, shutil

# see https://www.nature.com/articles/sdata2018214
zip_url = "https://figshare.com/ndownloader/files/45057352"
zip_path = "data.zip"
extract_folder = "extracted_data"
target_folder = "climate_data"
target_filename = "koppen_geiger_0p1.tif"

def download_climate_data():
    response = requests.get(zip_url, stream=True)
    with open(zip_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)

    tif_file_path = None
    for root, dirs, files in os.walk(extract_folder):
        if "1991_2020" in root:
            for file in files:
                if file == target_filename:
                    tif_file_path = os.path.join(root, file)
                    break

    if tif_file_path:
        os.makedirs(target_folder, exist_ok=True)
        shutil.move(tif_file_path, os.path.join(target_folder, target_filename))

    shutil.rmtree(extract_folder)
    os.remove(zip_path)
