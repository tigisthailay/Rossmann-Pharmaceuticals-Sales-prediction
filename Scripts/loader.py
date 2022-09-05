"""Load data from a file and returns a dataframe.
"""
import json
import sys
from git import Object
import pandas as pd
from logger import LoggerClass


class LoadData:

    def __init__(self) -> None:
        """Initilize class."""
        try:
            self.logger = LoggerClass("logger.log").get_app_logger()
            self.logger.info(
                'Successfully Instantiated load_data Class Object')
        except Exception:
            self.logger.exception(
                'Failed to Instantiate load_data Class Object')
            sys.exit(1)

    def read_json(self, json_file: str, dfExtractFunc: Object) -> pd.DataFrame:
        """Json file reader to open and read json files into a panda dataframe. """

        data_list = []
        for item in open(json_file, 'r'):
            data_list.append(json.loads(item))

        df = dfExtractFunc(data_list)
        return df

    def read_excel(self, excel_file, startRow=0) -> pd.DataFrame:
        
        df = pd.read_excel(excel_file, engine='openpyxl')
        return df

    def read_csv(self, csv_file) -> pd.DataFrame:
       
        return pd.read_csv(csv_file)
