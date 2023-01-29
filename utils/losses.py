import torch


class MSECELoss(torch.nn.Module):

    def __init__(self):
        super(MSECELoss, self).__init__()

    def forward(self, pred, true):
        mse_value = torch.nn.functional.mse_loss(pred[:, :, :-1], true[:, :, :-1]) * 10000
        ce_value = torch.nn.functional.cross_entropy(pred[:, :, -1], true[:, :, -1])
        return mse_value + ce_value
