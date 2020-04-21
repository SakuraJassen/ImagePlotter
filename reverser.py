import imageio
import progressbar

fileName = "debug"
fileEnding = ".gif"
startOffset = 0
endOffSet = 0

with imageio.get_reader('C:\\Users\\Nutzer\\Documents\\Python\\out\\{0}{1}'.format(fileName, fileEnding)) as reader:
    totalFrames = reader.get_length()
    fps = totalFrames / reader.get_meta_data()["duration"] * 10
    if "fps" in reader.get_meta_data():
        totalFrames = reader.count_frames() 
        fps = reader.get_meta_data()["fps"]

    print("Creating File:'{0}{1}' with {2} FPS and total Frames of {3}".format(fileName, fileEnding, fps, totalFrames))
    with imageio.get_writer('./out/{0}rev.mp4'.format(fileName), mode='I', fps=fps, quality=9) as writer:
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