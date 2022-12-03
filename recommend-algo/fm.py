import numpy as np
from scipy import sparse

class MatrixFactorization():
  def __init__(self, R, X, Y, k, steps=200, alpha=0.01, lamda=0.001, threshold=0.001):
    self.R = R
    self.m = R.shape[0]
    self.n = R.shape[1]
    self.k = k
    # initializa U and V
    self.U = np.random.rand(self.m, self.k)
    self.V = np.random.rand(self.k, self.n)
    self.alpha = alpha
    self.lamda = lamda
    self.threshold = threshold
    self.steps = 200

    # preserve user_id list and item_id list
    self.X = X
    self.Y = Y

  def shuffle_in_unison_scary(self, a, b):
    rng_state = np.random.get_state()
    np.random.shuffle(a)
    np.random.set_state(rng_state)
    np.random.shuffle(b)

  def fit(self):
    for step in range(self.steps):
      error = 0
      # shuffle the order of the entry
      self.shuffle_in_unison_scary(self.X,self.Y)

      # update U and V
      for i in self.X:
        for j in self.Y:
          r_ij = self.R[i-1,j-1]
          if r_ij > 0:
            err_ij = r_ij - np.dot(self.U[i-1,:], self.V[:,j-1])
            for q in range(self.k):
              self.U[i-1,q] += self.alpha * (err_ij * self.V[q, j-i] + self.lamda * self.U[i-1, q])
              self.V[q, j-1] += self.alpha * (err_ij * self.U[i-1, q] + self.lamda * self.V[q, j-i])

      # approximation
      R_hat = np.dot(self.U, self.V)
      # calculate estimation error for observed values
      for i in self.X:
        for j in self.Y:
          r_ij = self.R[i-1, j-1]
          r_hat_ij = R_hat[i-1, j-1]
          if r_ij > 0:
            error += pow(r_ij - r_hat_ij,2)
      # regularization
      error += (self.lamda * np.power(self.U,2).sum()) / 2
      error += (self.lamda * np.power(self.V,2).sum()) / 2

      if error < self.threshold:
        break
    return self.U, self.V


    # R = np.random.randint(6, size=(5, 8), dtype=np.int8)
R = sparse.csr_matrix(np.random.randint(6, size=(5, 8)), dtype=np.int8)
X = np.arange(1, 6) # mock for user_id
Y = np.arange(1, 9) # mock for item_id

R.toarray()


mf = MatrixFactorization(R, X, Y, k=2, steps=200)
U, V = mf.fit()
print(np.dot(U,V))