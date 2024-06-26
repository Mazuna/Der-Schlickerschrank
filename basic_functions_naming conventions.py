def introduction_1(first_name, last_name):
  print("Normal or Japanese Naming Convention ? N/j")
  naming_convention = input(str())
  if naming_convention == "j":
    print("Hello, my name is", last_name, first_name)    
  else:      
    print("Hello, my name is", first_name, last_name)
     
#introduction("Luke", "Skywalker")
#introduction("Jesse", "Quick")
#introduction("Clark", "Kent")

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
 
introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")