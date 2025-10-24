import os
import requests
import zipfile
from textSummarization.logging import logger
from textSummarization.config.configuration import Configuration

class DataIngestionPipeline:
    def __init__(self):
        self.config = Configuration()
        # Step 2a: Make sure folder exists
        os.makedirs(self.config.get_data_ingestion_config().root_dir, exist_ok=True)

    def main(self):
        logger.info(">>>>>> Stage Data Ingestion stage started <<<<<<")

        # Step 2b: Get config
        data_ingestion_config = self.config.get_data_ingestion_config()

        # Step 2c: Download zip
        url = data_ingestion_config.source_URL
        local_file = data_ingestion_config.local_data_file

        r = requests.get(url)
        r.raise_for_status()  # stop if download fails
        with open(local_file, "wb") as f:
            f.write(r.content)
        logger.info(f"data.zip created at: {local_file}")

        # Step 2d: Unzip
        with zipfile.ZipFile(local_file, 'r') as zip_ref:
            zip_ref.extractall(data_ingestion_config.unzip_dir)
        logger.info(f"Files extracted to: {data_ingestion_config.unzip_dir}")

        logger.info(">>>>>> Stage Data Ingestion stage completed <<<<<<\n\nx==========x")

