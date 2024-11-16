import tkinter as tk
from tkinter import ttk
from sklearn.ensemble import RandomForestClassifier
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
import copy
import time
from google.cloud import bigquery