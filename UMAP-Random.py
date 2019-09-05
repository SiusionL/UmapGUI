import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import umap
sns.set(style='white', rc={'figure.figsize':(12,8)})

np.random.seed(42)
data = np.random.rand(800, 4)

fit = umap.UMAP()
u = fit.fit_transform(data)

plt.scatter(u[:,0], u[:,1], c=data)