import h5py
import numpy as np
from pylab import imshow, show, axis

# Add path to .h5 file
h5_file = 'path_to_file'

# Reads the file
f = h5py.File(h5_file, 'r')

# Lists all groups
a_group_key = list(f.keys())[0]

# Gets data
data = np.array(f[a_group_key])

# Labels object
label = data[:,:,0]

# Shows object
imshow(label)
axis("off")
show()
