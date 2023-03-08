 #tuple is for read only
mytuple=(1,2,3)
#defining graph
mygraph={
    "A":[("B",2),("C",4),("D",5)]
}
#accessing the cost of 1st node which is 2
print(mygraph['A'][0][1])
