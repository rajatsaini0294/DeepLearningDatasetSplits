"""
execute this python script from the parent directory of the UCSD Birds dataset
Source: http://www.vision.caltech.edu/visipedia/CUB-200.html
"""
import os
from shutil import copy

DATASET_DIR = "./images/"  # parent dir (dowloaded images)
TEST_DIR = "./test"  # test directory
TRAIN_DIR = "./train"  # train directory
TEST_CLASSES = "./lists/test.txt"  # path to test split
TRAIN_CLASSES = "./lists/train.txt"  # path to train split

if not os.path.exists(DATASET_DIR):
    print("Invalid directory path ", DATASET_DIR)

if not os.path.exists(TEST_DIR):
    print(f"Test directory not found. Creating...")
    os.mkdir(TEST_DIR)

new_test_dir = TEST_DIR

if not os.path.exists(TRAIN_DIR):
    print(f"Train directory not found. Creating...")
    os.mkdir(TRAIN_DIR)

new_train_dir = TRAIN_DIR

classes = os.listdir(DATASET_DIR)

# create the dir for each class in train/test directory
for each in classes:
    _train = os.path.join(new_train_dir, each)
    _test = os.path.join(new_test_dir, each)

    if not os.path.exists(_train):
        os.makedirs(_train)

    if not os.path.exists(_test):
        os.makedirs(_test)

train_samples_path = []
test_samples_path = []

# create the paths for TRAIN SRC and DEST transfer
with open(TRAIN_CLASSES, "r") as f:
    _train_sample = f.readlines()
    _sample = [(x.strip("\n")) for x in _train_sample]
    train_samples_path_src = [os.path.join(DATASET_DIR, each) for each in _sample]
    train_samples_path_dest = [os.path.join(TRAIN_DIR, each) for each in _sample]

# create the paths for TEST SRC and DEST transfer
with open(TEST_CLASSES, "r") as f:
    _test_sample = f.readlines()
    _sample = [(x.strip("\n")) for x in _test_sample]
    test_samples_path_src = [os.path.join(DATASET_DIR, each) for each in _sample]
    test_samples_path_dest = [os.path.join(TEST_DIR, each) for each in _sample]

# copy samples into test and train samples
for i in range(0, len(train_samples_path_src)):
    copy(train_samples_path_src[i], train_samples_path_dest[i])

for i in range(0, len(test_samples_path_src)):
    copy(test_samples_path_src[i], test_samples_path_dest[i])

# check whether same sample is copied in test and train samples
print("Checking integrity...")
_train = []
_test = []

train_counter = 0
test_counter = 0
for each in os.listdir(TRAIN_DIR):
    for x in os.listdir(os.path.join(TRAIN_DIR, each)):
        _train.append(x)
        train_counter = train_counter + 1

for each in os.listdir(TEST_DIR):
    for x in os.listdir(os.path.join(TEST_DIR, each)):
        _test.append(x)
        test_counter = test_counter + 1

if not any(x in _train for x in _test):
    print("Successfully done.")
else:
    print("Error")

print("Train samples: ", train_counter)
print("Test samples: ", test_counter)
