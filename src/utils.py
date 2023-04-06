import requests
from bs4 import BeautifulSoup
from datetime import datetime
from logger import logging
import glob
import os


def get_latest_csv_file_from_github():
    """
    Fetches the latest CSV file from the specified GitHub repository.

    Parameters:
    repo_url (str): The URL of the GitHub repository directory.

    Returns:
    str: The URL of the latest CSV file, or None if no CSV files were found.

    Example:
    >>> repo_url = "https://github.com/myusername/myrepo/tree/main/data"
    >>> latest_file = get_latest_csv_file_from_github(repo_url)
    >>> print(latest_file)
    https://github.com/myusername/myrepo/raw/main/data/latest_file.csv
    """
    repo_url = "https://github.com/iamlekh/customer_spending/tree/main/data/raw"
    response = requests.get(repo_url)
    soup = BeautifulSoup(response.content, "html.parser")
    csv_links = [
        link.get("href")
        for link in soup.find_all("a")
        if link.get("href").endswith(".csv")
    ]
    if not csv_links:
        logging.info("no csv in the link")
        return None

    expected_name = datetime.now().strftime("%d%m%Y_df.csv")
    for i in csv_links:
        if expected_name in i:
            latest_link = i
    latest_file = (
        "https://raw.githubusercontent.com/iamlekh/customer_spending/main/data/raw/"
        + latest_link.split("/")[-1]
    )

    return latest_file


def get_latest_csv_file():
    """
    Fetches the latest CSV file from the specified directory.

    Parameters:
    folder_path (str): The path of the folder to search for CSV files.

    Returns:
    str: The path of the latest CSV file, or None if no CSV files were found.

    Example:
    >>> folder_path = "/path/to/folder"
    >>> latest_file = get_latest_csv_file(folder_path)
    >>> print(latest_file)
    /path/to/folder/latest_file.csv
    """
    folder_path = "data/raw/"
    csv_files = glob.glob(os.path.join(folder_path, "*_df.csv"))

    if not csv_files:
        return None
    latest_file = max(csv_files, key=os.path.getctime)
    return latest_file
