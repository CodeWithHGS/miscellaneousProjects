import speedtest
s = speedtest.Speedtest()
print("Upload speed = "+str(s.upload()//1000000)+" Mb/s")
print("Download speed = "+str(s.download()//1000000)+" Mb/s")
input()