import a_PlantClass as pc

primrose = pc.Plant("Green")

sunflower = pc.Flower("Yellow",20)

print(primrose.get_color())

print(sunflower.get_color())
print(sunflower.get_petals())


print(primrose.get_petals())
#you can only work from the top down of the class file, starting with super class
#then going down to subclass
#print primrose petals will get an error because petals is associated with flower and primrose is associated with plant
