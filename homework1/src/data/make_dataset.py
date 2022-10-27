# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
# from dotenv import find_dotenv, load_dotenv
import pandas as pd
from sklearn.model_selection import train_test_split


def read_csv_data(csv_path):
    data = pd.read_csv(csv_path)
    return data


def split_data(data, split_param):
    return train_test_split(data, split_param)
