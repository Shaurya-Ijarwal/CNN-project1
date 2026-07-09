"""
Project Configuration File

Contains all configurable parameters used throughout the project.
"""

from pathlib import Path

# ==========================
# Project Paths
# ==========================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data" / "raw"

TRAIN_DIR = DATA_DIR / "train"
TEST_DIR = DATA_DIR / "test"

MODEL_DIR = PROJECT_ROOT / "models"

OUTPUT_DIR = PROJECT_ROOT / "outputs"

# ==========================
# Image Parameters
# ==========================

IMAGE_HEIGHT = 224
IMAGE_WIDTH = 224
IMAGE_SIZE = (IMAGE_HEIGHT, IMAGE_WIDTH)

CHANNELS = 3

# ==========================
# Dataset Parameters
# ==========================

BATCH_SIZE = 32

VALIDATION_SPLIT = 0.20

SEED = 42

# ==========================
# Training Parameters
# ==========================

EPOCHS = 20

LEARNING_RATE = 0.001

# ==========================
# Class Names
# ==========================

CLASS_NAMES = [
    "Cat",
    "Dog"
]