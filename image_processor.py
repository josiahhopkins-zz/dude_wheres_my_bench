from __future__ import division
from PIL import Image
import os

class image_processor:

	def __init__(self):
		self.image_locations = []
		self.total_difference = 0
		self.threshhold = .5
		self.pixel_diff_threshhold = .1

	def get_difference(self, img1, img2):
		total_different = 0
		the_dir = os.environ["PWD"]
		img_1_array = list(Image.open(the_dir + "/" + img1).getdata())
		img_2_array = list(Image.open(the_dir + "/" + img2).getdata())
		pixel_ratio = 1
		number_of_pixels = min(len(img_1_array), len(img_2_array))

		for pixel_number in range(0, number_of_pixels, pixel_ratio):
			pixel_diff = 0
			for color in range(3):
				pixel_diff += abs(img_1_array[pixel_number][color] - img_2_array[pixel_number][color])
			if pixel_diff > 40:
				total_different += 1
		if ((total_different * pixel_ratio) / number_of_pixels) > self.pixel_diff_threshhold:
			return 1
		return 0

	def make_decision(self):
		return self.total_difference / 4 > self.threshhold 

	def add_image(self, img_location):
		self.image_locations.append(img_location)
		num_images =  len(self.image_locations)
		if num_images > 1:
			diff = self.get_difference(self.image_locations[num_images -1], self.image_locations[num_images -2])
			self.total_difference = self.total_difference + diff
