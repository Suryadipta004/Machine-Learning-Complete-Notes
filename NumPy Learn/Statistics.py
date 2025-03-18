import numpy as np

stats = np.array([[1,2,3],[4,5,6]])
print(stats)

print(np.min(stats))
print(np.max(stats))
print(np.min(stats, axis=0))
print(np.min(stats, axis=1))
print(np.max(stats, axis=0))
print(np.max(stats, axis=1))
print(np.sum(stats))
print(np.sum(stats, axis=0))
print(np.sum(stats, axis=1))
print(np.mean(stats))
print(np.mean(stats, axis=0))
print(np.mean(stats, axis=1))
print(np.median(stats))
print(np.median(stats, axis=0))
print(np.median(stats, axis=1))
print(np.std(stats))
print(np.std(stats, axis=0))
print(np.std(stats, axis=1))
print(np.var(stats))
print(np.var(stats, axis=0))
print(np.var(stats, axis=1))
print(np.percentile(stats, 100))
print(np.percentile(stats, 100, axis=0))
print(np.percentile(stats, 100, axis=1))
