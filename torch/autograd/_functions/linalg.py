import torch

from ..function import Function


class Diag(Function):

    def __init__(self, diagonal_idx=0):
        super(Diag, self).__init__()
        self.diagonal_idx = diagonal_idx

    def forward(self, input):
        return input.diag()

    def backward(self, grad_output):
        return grad_output.diag()


class Tril(Function):

    def __init__(self, diagonal_idx=0):
        super(Tril, self).__init__()
        self.diagonal_idx = diagonal_idx

    def forward(self, input):
        return input.tril(self.diagonal_idx)

    def backward(self, grad_output):
        return grad_output.tril(self.diagonal_idx)


class Triu(Function):

    def __init__(self, diagonal_idx=0):
        super(Triu, self).__init__()
        self.diagonal_idx = diagonal_idx

    def forward(self, input):
        return input.triu(self.diagonal_idx)

    def backward(self, grad_output):
        return grad_output.triu(self.diagonal_idx)


class Trace(Function):

    def forward(self, input):
        self.isize = input.size()
        return input.new((input.trace(),))

    def backward(self, grad_output):
        isize = self.isize
        grad_input = grad_output.new(isize).zero_()
        grad_input.view(-1)[::(isize[1] + 1)] = grad_output[0]
        return grad_input
