dict= {"kushal":2354698751,"tejo":1236547895,"chakri":8965471235,"aakash":2456987453,"raghava":8796547382}
print(dict)
print("displayed the name with number...i.e. key with value")
print(dict.keys())
print(" displayeed the keys")
dict1={"dheeraj":9849677433,"chetan":9963764920}
dict.update(dict1)
print(dict.keys())
print("displayed the updated dictionary of the friend list")
del dict["raghava"]
print(dict.keys())
print(" deleted a dictionary key ")
dict["kushal"]=5698741235
print(dict)
print("modified the current dictionary")
x=input("enter the key value to be searched:")
if x in dict:
    print("true key found")
else:
    print("false key not found")
print(sorted(dict))
print("dictionary has been sorted")
