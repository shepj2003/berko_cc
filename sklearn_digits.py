###############################################################################
## CELL 1
###############################################################################
from sklearn import datasets
# Load in the `digits` data
digits = datasets.load_digits()
# Import matplotlib
import matplotlib.pyplot as plt

# Figure size (width, height) in inches
fig = plt.figure(figsize=(6, 6))

# Adjust the subplots 
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# For each of the 64 images
for i in range(64):
    # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position
    ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
    # Display an image at the i-th position
    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
    # label the image with the target value
    ax.text(0, 7, str(digits.target[i]))

# Show the plot
plt.show()


###############################################################################
## END OF CELL 1
###############################################################################

###############################################################################
## BEGINNING OF CELL 2
###############################################################################
# Import `PCA()`
from sklearn.decomposition import PCA
# Import `train_test_split`
from sklearn.cross_validation import train_test_split
# Import `datasets` from `sklearn`
from sklearn import datasets
# Import
from sklearn.preprocessing import scale
# Import the `cluster` module
from sklearn import cluster

# Load in the `digits` data
digits = datasets.load_digits()
# Apply `scale()` to the `digits` data
data = scale(digits.data)


# Create the KMeans model
clf = cluster.KMeans(init='k-means++', n_clusters=10, random_state=42)



# Split the `digits` data into training and test sets
X_train, X_test, y_train, y_test, images_train, images_test = train_test_split(data, digits.target, digits.images, test_size=0.25, random_state=42)
# Model and fit the `digits` data to the PCA model
# Fit the training data to the model
clf.fit(X_train)
X_pca = PCA(n_components=2).fit_transform(X_train)

# Compute cluster centers and predict cluster index for each sample
clusters = clf.fit_predict(X_train)

# Create a plot with subplots in a grid of 1X2
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Adjust layout
fig.suptitle('Predicted Versus Training Labels', fontsize=14, fontweight='bold')
fig.subplots_adjust(top=0.85)

# Add scatterplots to the subplots 
ax[0].scatter(X_pca[:, 0], X_pca[:, 1], c=clusters)
ax[0].set_title('Predicted Training Labels')
ax[1].scatter(X_pca[:, 0], X_pca[:, 1], c=y_train)
ax[1].set_title('Actual Training Labels')

# Show the plots
plt.show()
###############################################################################
## END OF CELL 2
###############################################################################


###############################################################################
## BEGINNING OF CELL 3
###############################################################################
from sklearn import svm

# Create the SVC model 
svc_model = svm.SVC(gamma=0.001, C=100., kernel='linear')
# Fit the data to the SVC model
svc_model.fit(X_train, y_train)
predicted = svc_model.predict(X_test)

# Zip together the `images_test` and `predicted` values in `images_and_predictions`
images_and_predictions = list(zip(images_test, predicted))

# Figure size (width, height) in inches
fig = plt.figure(figsize=(6, 6))

# Adjust the subplots 
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.2, wspace=0.05)
# For the first 4 elements in `images_and_predictions`
for index, (image, prediction) in enumerate(images_and_predictions[:16]):
    # Initialize subplots in a grid of 1 by 4 at positions i+1
    plt.subplot(4, 4, index + 1, xticks=[], yticks=[])
    # Don't show axes
    plt.axis('off')
    # Display images in all subplots in the grid
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    # Add a title to the plot
    plt.title('Predicted: ' + str(prediction))

# Show the plot
plt.show()

###############################################################################
## END OF CELL 3
###############################################################################
