import torch as torch
import torch.nn as nn
import torch.nn.functional as F


class DQN(nn.Module):
    def __init__(self):
        super(DQN, self).__init__()
        self.flatten = nn.Flatten()
        self.activation = nn.ReLU()
        self.dense1 = nn.Linear(64, 256)
        self.dense2 = nn.Linear(256, 128)
        self.dense3 = nn.Linear(128, 64)
        self.output = nn.Linear(64, 1)
       
    def predict_val(self, state):
        state = self.flatten(state)
        state = self.activation(self.dense1(state))
        state = self.activation(self.dense2(state))
        state = self.activation(self.dense3(state))
        return self.output(state)

    def forward(self, board):
        values = []
        for move in board.get_possible_moves():
            board_copy = board.copy()
            board_copy.update_move(move)
            state = board_copy.get_board_state()
            value = self.predict_val(state)
            values.append(value)
        return torch.tensor(values)