import sys

from PIL import Image

images = []
for arg in sys.argv[1:]:# Jump the first argument
    image = Image.open(arg)
    images.append(image)

# Save image as costumes.gif, save everything apending second image, duration is 200 ms, and loop =0 means loop forever
images[0].save(
    "costumes.gif", 
    save_all=True,              # Changed the '.' to a ','
    append_images=[images[1]],  # This is now a seperate argument
    duration=200, 
    loop=0
)
