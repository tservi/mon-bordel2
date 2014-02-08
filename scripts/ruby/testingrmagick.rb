#!/usr/bin/env ruby1.9.1

require 'RMagick'
include Magick

cat = ImageList.new("Cheetah.jpg")
cat.display
exit
