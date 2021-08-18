import random
#Vector addition
def vector_add(v, w):
 return [v_i + w_i for v_i, w_i in zip(v, w)]
 
#vector subtraction
def vector_subtract(v, w):
 return [v_i - w_i for v_i, w_i in zip(v, w)] 
 
#finding median
def median(v):
 n = len(v)
 sorted_v = sorted(v)
 midpoint = n // 2
 if n % 2 == 1:
  return sorted_v[midpoint]
 else:
  lo = midpoint - 1
  hi = midpoint
  return (sorted_v[lo] + sorted_v[hi]) / 2

#probality that 2 kids in a family are all girls given atleast one is a girl
def random_kid():
 return random.choice(["boy", "girl"])
both_girls = 0
older_girl = 0
either_girl = 0
random.seed(0)
for _ in range(10000):
 younger = random_kid()
 older = random_kid()
 if older == "girl":
   older_girl += 1
 if older == "girl" and younger == "girl":
   both_girls += 1
 if older == "girl" or younger == "girl":
   either_girl += 1

print("P(both | older):", both_girls / older_girl)
print("P(both | either): ", both_girls / either_girl)

users=[
 { "id":0,"name":"Hero" },
 { "id":1,"name":"Dunn" },
 { "id":2,"name":"Sue" },
 { "id":3,"name":"Chi" },
 { "id":4,"name":"Thor" },
 { "id":5,"name":"Clive" },
 { "id":6,"name":"Hicks" },
 { "id":7,"name":"Devin" },
 { "id":8,"name":"Kate" },
 { "id":9,"name":"Klein" },
 ]
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
for user in users:
 user["friends"] = []
 
#accessing elements in tuple
for i, j in friendships:
 users[i]["friends"].append(users[j]["id"]) # add j as a friend of i
 users[j]["friends"].append(users[i]["id"]) #add i to frieds of j
 
print(users) #to see dictionary
#to find number of friends each has

def number_of_friends(user):
 return len(user["friends"])
 
#total connections
total_connections = sum(number_of_friends(user) for user in users)
print(total_connections)

#we can sort list from user with most friends to user with least friends, python 2
'''num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
sorted(num_friends_by_id,key=lambda user_id, num_friends: num_friends,reverse=True)'''

#identifying people one may know
def friends_of_friend_ids_bad(user):
 # "foaf" is short for "friend of a friend"
 return [foaf["id"] for friend in user["friends"] for foaf in friend["friends"]]

#using matlib's pyplot for visualization
#Code A
from matplotlib import pyplot as plt
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
# create a line chart, years on x-axis, gdp on y-axis
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
# add a title
plt.title("Nominal GDP")
# add a label to the y-axis
plt.ylabel("Billions of $")
plt.show()

#code B
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
# bars are by default width 0.8, so we'll add 0.1 to the left coordinates
# so that each bar is centered
xs = [i + 0.1 for i, _ in enumerate(movies)]
# plot bars with left x-coordinates [xs], heights [num_oscars]
plt.bar(xs, num_oscars)
plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")
# label x-axis with movie names at bar centers
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
plt.show()
