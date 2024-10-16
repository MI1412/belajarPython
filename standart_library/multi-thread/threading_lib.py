import threading, zipfile
# NAME
#     threading - Thread module emulating a subset of Java's threading model.
# NAME
#     zipfile - Read and write ZIP files.
class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('selesain mengzip:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()

print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')

# next buat zip tersambung database