import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image

def image_segmentation(image_url, n_clusters, save = True):
	img = Image.open(image_url)
	img_array = np.array(img.convert("RGB"))
	#img_array = plt.imread(image_url)
	img_width = img_array.shape[0]
	img_height = img_array.shape[1]
	print(img_array.shape)
	train = img_array.reshape(img_width * img_height, img_array.shape[2])
	print(train.shape)
	kmeans = KMeans(n_clusters = n_clusters)
	kmeans.fit(train)

	cluster_img_array = []

	for cluster_index in kmeans.labels_:
		cluster_img_array.append(kmeans.cluster_centers_[cluster_index])

	new_img_array = np.array(cluster_img_array).reshape(img_width, img_height, img_array.shape[2]).astype("uint8")

	fig = plt.figure(figsize = (10,10))
	ax1 = fig.add_subplot(1, 2, 1)
	ax2 = fig.add_subplot(1, 2, 2)

	ax1.imshow(img_array)
	ax2.imshow(new_img_array)

	if save:
		plt.imsave("cluster_image.png", new_img_array)

	plt.show()

def test():
	image_segmentation("flamingo.jpg", n_clusters = 4)
	
if __name__ == "__main__":
	args = sys.argv

	if len(args) > 2:
		image_url = args[1]
		number_clusters = args[2]
		image_segmentation(image_url, int(number_clusters))
	else:
		test()
