import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np
import cv2
import kagglehub


path = kagglehub.dataset_download("moltean/fruits")

print("Path to dataset files:", path)      



