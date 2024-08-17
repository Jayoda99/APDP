import os
import csv
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

#File names
USER_FILE = "user.csv"
BRANCHES_FILE = "branch.csv"
PRODUCTS_FILE = "product.csv"
SALES_FILE = "sale.csv"

###### Factory Pattern #############

#Interface for data laoders
class DataLoader:
  def loaddata(self):
    raise NotImplementedError

#Loader Implementation
class CSVLoader(DataLoader):
  def __init__(self, filename):
    self.filename = filename

  def loaddata(self):
    data = []
    if os.path.exists(self.filename):
      with open(self.filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader) #Skip header
        for row in reader:
          data.append(row)
    return data

#Creating loaders
class DataLoaderFactory:
  @staticmethod
  def make_loader(filename):
    if filename.endswith('user.csv'):
      return CSVLoader(filename)
    elif filename.endswith('branch.csv'):
      return CSVLoader(filename)
    elif filename.endswith('product.csv'):
      return CSVLoader(filename)
    elif filename.endswith('sale.csv'):
      return CSVLoader(filename)
    else:
      raise ValueError("File type not supported")

###### Commsnd Pattern #############

# Base command interface
class Command:
  def execute(self):
    raise NotImplementedError

# Add a new branch
class AddBranchCommand(Command):
  def execute(self):
    print("\n///// Add New Branch /////")
    branches = loaddata(BRANCHES_FILE)

    bran_id = input("Enter Branch ID: ")
    branch_name = input("Enter Branch Name: ")
    location = input("Enter Location: ")

    new_branch = [brain_id, branch_name, location]
    branches.append(new_branch)

    os.remove(BRANCHES_FILE)

    headers = ['Branch ID', 'Branch Name', 'Location']
    csv_datasave(BRANCHES_FILE, branches, headers = headers)
    print(f"Branch {branch_name} added successfully.")

# Concrete command to add a new sale
class AddSale(Command):
  def execute(self):
    print("\n///// Add New Sale /////")
    sales = loaddata(SALES_FILE)

    bran_id = input("Enter Branch ID: ")
    prod_id = input("Enter Product ID: ")
    amt_sold = input("Enter Amount Sold: ")

    new_sale = [bran_id, prod_id, amt_sold, datetime.now().strftime()]
