import imageio
import progressbar

fileName = "debug"
fileEnding = ".gif"
startOffset = 1
endOffSet = 10

Metadata = {'fps': 30}

with imageio.get_reader('C:\\Users\\Nutzer\\Documents\\Python\\out\\{0}{1}'.format(fileName, fileEnding)) as reader:
    totalFrames = reader.get_length() # A Gif doesn't save the FPS so we either have to estimate it or get a User to provide it
    #Metadata['fps'] = totalFrames / reader.get_meta_data()["duration"] * 20
    if "fps" in reader.get_meta_data():
        totalFrames = reader.count_frames() 
        Metadata['fps'] = reader.get_meta_data()["fps"]
        Metadata['quality'] = 9

    print("Creating File:'{0}{1}' with {2} FPS and total Frames of {3}".format(fileName, fileEnding, Metadata['fps'], totalFrames))
    with imageio.get_writer('./out/{0}rev{1}'.format(fileName, fileEnding), mode='I', **Metadata) as writer:
        images = []
        print("Reading...")
        for x in progressbar.progressbar(range(startOffset, totalFrames - endOffSet)):
            image = reader.get_data(x)
            images.append(image)


        print("Writing Data...")
        print("1/2...")
        for x in progressbar.progressbar(range(len(images))):
            writer.append_data(images[x])

        images.reverse()
        print("2/2...")
        for x in progressbar.progressbar(range(len(images))):
            writer.append_data(images[x])