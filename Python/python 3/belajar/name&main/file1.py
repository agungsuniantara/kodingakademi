print("berjalan adalah = {}".format(__name__))

def tampil():
    print("hello world")

if __name__=='__main__':
    tampil()
    print("name tidak diimport")
else:
    print("name diimport")