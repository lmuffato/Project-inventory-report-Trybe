import xml.etree.ElementTree as ET
import csv 

class Inventory:

  # list_of_dicts = []

  def __init__(self, path):
    self.path = path

  def __contains__(self, path):
    if substring in self.path and substring

    def import_data(self, csv_path: str) -> list:
      with open(csv_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]
      return data

      # if (in)
    
