import os
import sys
from argparse import ArgumentParser
from PIL import Image

#----------------------------------------------------------------------------

def main():
    parser = ArgumentParser(description="Convert images to JPEG format.")
    parser.add_argument("inputDirectory", help="Directory containing images.")
    parser.add_argument("outputDirectory", help="Output directory")
    
    args = parser.parse_args()

    imageDirectory = args.inputDirectory

    if not imageDirectory.endswith('/') or not imageDirectory.endswith('\\'):
        imageDirectory += '\\'
    saveDirectory = args.outputDirectory
    if not saveDirectory.endswith('/') or not saveDirectory.endswith('\\'):
        saveDirectory += '\\'

    if not os.path.exists(saveDirectory):
        os.makedirs(saveDirectory)
    
    ext = '.jpg'

    failCounter = 0

    if os.path.exists(imageDirectory):
        for i, image in enumerate(os.listdir(imageDirectory)):
            try:
                im1 = Image.open(imageDirectory + image).convert('RGB')
                im1.save(saveDirectory + str(i) + ext)
            except:
                print("Could not process " + str(image))
                failCounter += 1
                os.remove(saveDirectory + str(i) + ext)
            
        print("Operation successful.")
        if failCounter > 0:
            print ("Could not process " + str(failCounter) + "images")
    else:
        print("Input directory not found.")
        sys.exit(1)
    

#----------------------------------------------------------------------------

if __name__ == "__main__":
    main()

#----------------------------------------------------------------------------