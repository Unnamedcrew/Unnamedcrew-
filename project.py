#NOTE
# do not change the location of the files in this process!!!
f = open("E:\demo.txt","r")
str = f.read()
print("Checking weather there are any suspicious activities are acuring")
if(str == "yes"):#to note if there are any accidents or not
     print("The relevent number has been called!!!!!")
     print("The back up will arrive soon!!!\n\n")
else:
     print("There are no mulicious activity found!!!")
str = f.close()
print("by using the infrared sencors measuring the heat of the surroundings")
print("senors of post 3 has been detected with the high num of heat than other post sencors")
f=open("E:/demo2.txt","r")
s = f.read()
if(s == "4"):
     print("Now making the camera sencors to detect the num of vechicals  ")
     print("Checking which post has more num vechicals")
     print("the post has been detected!!!!")
     print("The post num is 3!!!")
     f= open("E:/demo3.txt")
     i = f.read()
     if(i == "40"):
          print("since the post '3' has more num of vechicles than 1,2&4")
          print("changing the signal, red to the post that has green in it")
          print("now changing the signal of post 3 from red to green\n\n")
          s=f.close()
print("Checking for the traffics or more num of vechiles in other posts")
f = open ("E:/demo4.txt","r")
q= f.read()
if(q == "3"):
     print("The other post has been found!!!!!")
     print("the other post num is 2!!!")
     print("now change the green signal of post 3 to red\n")
     print("change the red signal of post 2 to green")
else:
     print("The other post has been found!!!!!")
     print("the other post num is 1!!!")
     print("now change the green signal of post 3 to red\n")
     print("change the red signal of post 1 to green\n\n")
     q = f.close()
#NOTE:
#since the people who stand in post 1&4 will be standing untill the limit of the vechiles
#we came up with the idea that if a post has red signal more than 5 min then they will be given green signal accodingly
f = open("E:\demo2.txt","r")
p = f.read()
if(p=="4"):
     print("Checking for the posts that has red signal more than 5 minutes!!!")
     print("The post 4 is said to be having more num of more num of minutes than 1 ")
     print("so the post 2 will be changed to reed from green ")
     print("now the post 4 will be changed from red to green\n\n")
     print("After the post 4 the post 1 will be changed into green since it will be more than 5 min ")
     print("this process will be running in the routine so the traffic will be managed smartl and frequently")
#NOTE:
# The project has been done with less num of days so we coudn't cope up with advanced type of language for programming
# So we decided to show the procss in the text form so there will be more print statements and sorry for that !!!!!!
#  If we had more time we could do better with it hope you like it
