from Text_Classification.logger import logging # type: ignore
from Text_Classification.exception import CustomException # type: ignore
import sys
from Text_Classification.configuration.gcloud_syncer import GCloudSync # type: ignore

obj = GCloudSync()
#obj.sync_folder_from_gcloud("Text_Classification-speech2024", "dataset.zip", "download/dataset.zip")
obj.sync_folder_from_gcloud("text_classification-speech2024", "dataset.zip", "download/dataset.zip")

