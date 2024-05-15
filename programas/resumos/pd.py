import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2],
  'days': [420,380,390]
}

#myvar = pd.DataFrame(mydataset)
#myvar = pd.Series(mydataset, index = ['cars','days'])

print(myvar)



a = [1, 7, 4]

myvar = pd.Series(a)


myvar = pd.Series(a,index=['x','y','z'])

#print(myvar['y'])
