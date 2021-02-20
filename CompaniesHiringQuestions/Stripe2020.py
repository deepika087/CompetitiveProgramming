
"""
Telephonic Coding round: 

Part 1:
The questions was that say you are given a table with rows and columns . Given a column find the row that contains minimum value 
for that column. 

for ex: 
	Table = [ { a:1, b : 2, c: 3} , { a : 10}]
	minBycolumn(Table, "a") -> return { a:1, b : 2, c: 3}
	minBycolumn(Table, "b") -> return { a : 10} because if a column is not present in a row assume it is 0. 
	So, basically {a : 10} can actually be thought as { a : 10, b : 0, c: 0}

	since, if we have two rows as of now so you can assume columns are a, b and c
	However, as you go forward the columns can change. 

Solution: Save dataset as List<HashMaps> Basically each row will be represented as a new hasmap and then appended to the List. 


Part 2: 
Now, you want to sort by multiple columns. Say for col1 there was a tie then sort by next column and so on. 

Table : [
	{ x : 1, y : 2, z : 3}, 
	{ x : 1, y : 2, z : 2},
	{x : 1, y : 2, z : 4 }
	]	

minByColumn(Table, ["x", "y", "z"]) -> return { x : 1, y : 2, z : 2}

The interviewer was happy with the approach. Allowed to you Google. Run/space time complexity was not a concern.

Received a reject within 2 hours of the interview
"""