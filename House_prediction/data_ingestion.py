from abc import abstractmethod, ABC

import pandas as pd
import os
import zipfile
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self,file_path: str) -> pd.DataFrame : 
        pass

class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path: str) -> pd.DataFrame : 
        if not file_path.endswith("zip"):
            raise ValueError("Not a zip file")
        
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall("extracted_data")

        extracted_data = os.listdir("extracted_data")
        csv_files = [f for f in extracted_data if f.endswith(".csv")]

        if len(csv_files) == 0:
            raise ValueError("There are no CSV files in the extracted data")
        if len(csv_files)>1:
            raise ValueError("There are more than one CSV file in the zip file")
        
        csv_file_path = os.path.join("extracted_data",csv_files[0])
        df = pd.read_csv(csv_file_path)

        return df
    
class DataIngestionFactory:
    @staticmethod
    def get_data_ingestor(file_extension:str) -> DataIngestor:
        if file_extension == ".zip":
            return ZipDataIngestor()
        else:
            return ValueError("No Ingestor available for this file extension")
        
if __name__ == "__main__":
    file_path = "/Users/devanshsinha/Desktop/Devansh Macbook Pro/LLD_Prep/House_prediction/Data/archive.zip"
    file_extension = os.path.splitext(file_path)[1]

    data_ingestor = DataIngestionFactory.get_data_ingestor(file_extension)

    df = data_ingestor.ingest(file_path)
    print(df.head())


