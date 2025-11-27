"""Get rid of the duplicates
Outline:
First, create a dictionary that consists of - id, name, class and subject integration
of students. Then, write a program to retrieve unique entries and eliminate the rest."""

"""student_data = {'id1':
                {'name': ['Sara'],
                 'class': ['V'],
                 'subject_integration': ['english, math, science']
                 },
                 'id2':
                 {'name': ['David'],
                  'class': ['V'], 
                   'subject_integration': ['english, math, science']
                   },
                   'id3':
                   {'name': ['Sara'],
                  'class': ['V'], 
                   'subject_integration': ['english, math, science']
                   },
                   'id4':
                    {'name': ['Surya'],
                  'class': ['V'], 
                   'subject_integration': ['english, math, science']
                   
                   },

}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)"""


"""Check the frequency
Outline:
Write a program to check the frequency 
of a value in a dictionary - {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}."""


"""test_dict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'else' : 2, 'for' : 2, 'Coding' : 1}

print("the original dictionary : " + str(test_dict))

k = 2

res = 0
for key in test_dict:
    if test_dict[key] == k:
        res = res + 1

print("Frequency of K is : " + str(res))"""



"""Get the country code
Outline:
Write a program to return the country code for various countries. Here’s a dictionary of different
 country codes - {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}."""

country_code = {'India' : '0091',
                    'Australia' : '0025', 
                    'Nepal' : '00977'}


print("Country code for India -")
print(country_code.get('India', 'Not Found'))

print("Country code for Japan -")
print(country_code.get('Japan', 'Not Found'))