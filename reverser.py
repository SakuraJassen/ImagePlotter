import imageio
import progressbar
import draw
import time
from pygifsicle import optimize

fileName = "test2"
fileEnding = ".gif"
outFileEnding = ".gif"
originalFilePath = 'C:\\Users\\Nutzer\\Documents\\Python\\out\\{0}{1}'.format(fileName, fileEnding)
outFilePath = 'C:\\Users\\Nutzer\\Documents\\Python\\out\\{0}rev{1}'.format(fileName, outFileEnding)

startOffset = 0
endOffSet = 0

Reverse = True
OnlyOptimize = False
Metadata = {'fps': 60}

if OnlyOptimize != True:
    with imageio.get_reader(originalFilePath) as reader:
        totalFrames = reader.get_length() # A Gif doesn't save the FPS so we either have to estimate it or get a User to provide it
        #Metadata['fps'] = totalFrames / reader.get_meta_data()["duration"] * 20
        if "fps" in reader.get_meta_data():
            totalFrames = reader.count_frames()
            Metadata['fps'] = reader.get_meta_data()["fps"]
            Metadata['quality'] = 9

        print("Creating File:'{0}{1}' with {2} FPS and total Frames of {3}".format(fileName, fileEnding, Metadata['fps'], totalFrames))
        with imageio.get_writer(outFilePath, mode='I', **Metadata) as writer:
            images = []
            print("Reading...")
            for x in progressbar.progressbar(range(startOffset, totalFrames - endOffSet)):
                image = reader.get_data(x)
                images.append(image)


            print("Writing Data...")
            print("1/2...")
            for x in progressbar.progressbar(range(len(images))):
                writer.append_data(images[x])

            if(Reverse == True):
                images.reverse()
                print("2/2...")
                for x in progressbar.progressbar(range(len(images))):
                    writer.append_data(images[x])
            writer.close()

draw.optimizeGIF(outFilePath, 'C:\\Users\\Nutzer\\Documents\\Python\\out\\{0}opt{1}'.format(fileName, fileEnding))