
# the boys
import torch
import torch.nn as nn

from sklearn.model_selection import KFold

import argparse

# locals
from dataloader import BraTSDataset


parser = argparse.ArgumentParser(description='Train 2D model for TMI paper experiments.')
parser.add_argument('datadir', type=str, help='Path to directory containing BraTS data.')
parser.add_argument('batch_size', type=int, help='Size of batch to use during optimization.')

args = parser.parse_args()

dataset = BraTSDataset(args.datadir)

k_folds = 5

results = {}

# Use a fixed random state to ensure reproducibility but also that we don't impose weird
# correlations in the data by splitting them in a given order. It is very likely that the
# is in some implicit temporal order.
kfold = KFold(n_splits=k_folds, shuffle=True, random_state=0)

for fold, (train_ids, test_ids) in enumerate(kfold.split(dataset)):


    train_subsampler = torch.utils.data.SubsetRandomSampler(train_ids)
    test_subsampler = torch.utils.data.SubsetRandomSampler(test_ids)

    trainloader = torch.utils.data.DataLoader(
                        dataset,
                        batch_size=args.batch_size,
                        sampler=train_subsampler)

    testloader = torch.utils.data.DataLoader 
                        dataset,
                        batch_size=args.batch_size,
                        sampler=test_subsampler)

    for 


