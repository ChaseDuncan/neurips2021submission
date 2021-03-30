import torch
import numpy as np
import os
from torch.utils.data import Dataset, DataLoader

class BraTSDataset(Dataset):
    def __init__(self, data_dir):
        '''
        Args:
            data_dir (string): Path to directory containing BraTS patient datasets. 
        '''
        assert os.path.isdir(data_dir), f'{data_dir} is not a directory.'
        self.patient_data = os.listdir(data_dir) 
        
        print(self.patient_data)

    def __len__(self):
        '''
        Length of dataset is the number of examples which has been predefined during
        preprocessing to be axis 0.
        '''
        return len(self.patient_data)
    

    def __getitem__(self, idx):
        '''
        Args:
            idx (int): The index of the example to be retrieved.

        TODO: transformations. at minimum the example needs to be normalized by MR mode.
        '''
        return self.data[idx]
