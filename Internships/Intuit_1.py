__author__ = 'deepika'

#Graduation date: Dec 2017
# Full Time SDE

"""
Logo
SAVE AND SUBMIT
7409b6af c369 43f2 ac8e 11f64001efd9
Question Prompt
Precursor steps

In a comment at the top of your solution, please include your expected graduation date, as well as whether you are applying as an intern or new grad (full time).

Introduction

Suppose you are creating an internal networking site for your company.

You have two data sets to work with. The first data set is the employees at your company, and the second is all the pairs of employees who are virtually friends so far. It does not matter which employee’s ID is in which column, the friendships are bidirectional. To get started, you need to represent each data set in its entirety in code. You may assume the raw input is provided in a reasonable format, e.g. like an API that returns a list of strings.

Furthermore, you also need to implement a function that, given the employees and friendships as parameters, returns this data in the form of an adjacency list representation. This is a mapping of each employee ID to a list of his/her friends on the site.

Example Input

var employees_input = [
  "1,Richard,Engineering",
  "2,Erlich,HR",
  "3,Monica,Business",
  "4,Dinesh,Engineering",
  "6,Carla,Engineering",
  "9,Laurie,Directors"
];

var friendships_input = [
  "1,2",
  "1,3",
  "1,6",
  "2,4"
];
Expected Output

{
  1: [2, 3, 6],
  2: [1, 4],
  3: [1],
  4: [2],
  6: [1],
  9: []
}
What’s expected

Fully compilable/executable code
Please do not modify main()
Your core implementation should be in createAdjacencyLists(), and you can add additional test cases in employeeSets(), friendshipSets(), and answers()
Clarifications

Assume all inputs are always valid (no duplicates, valid friendship IDs)
Employee IDs do not have to be sequential

"""
def create_adjacency_lists(employees, friendships):
    employeeSet = set()
    for employee in employees:

        employee = employee.split(",")
        k = int(employee[0])
        employeeSet.add(k)

    employeeSet = sorted(employeeSet)
    n = max(employeeSet)+1
    matrix = [ [None for i in range(n)] for j in range(n) ]

    for _relation in friendships: #"1, 2"
        _relation = _relation.split(",")
        a = int(_relation[0])
        b = int(_relation[1])

        matrix[a][b] = True
        matrix[b][a] = True

    mainList = []
    result = dict()
    for emp in employeeSet:
        friends = []
        for _ in employeeSet:
            if matrix[emp][_]:
                friends.append(_)
        result[emp] = friends

    mainList.append(result)
    return result

# START TEST CASES
# You can add test cases in the three functions below: employees_inputs(),
# friendships_inputs(), and expected_outputs(). Each test case input/expected output
# should correspond to the same index in the respective lists returned.
def employees_inputs():
    inputs = []

    inputs.append([
        "1,Richard,Engineering",
        "2,Erlich,HR",
        "3,Monica,Business",
        "4,Dinesh,Engineering",
        "6,Carla,Engineering",
        "9,Laurie,Directors"
    ]);

    return inputs

def friendships_inputs():
    inputs = []

    inputs.append([
        "1,2",
        "1,3",
        "1,6",
        "2,4"
    ])

    return inputs

def expected_outputs():
    expected = []

    expected.append({
        1: [2, 3, 6],
        2: [1, 4],
        3: [1],
        4: [2],
        6: [1],
        9: []
    })

    return expected
# END TEST CASES

# DO NOT MODIFY MAIN()
def main():
    employeesInputs = employees_inputs()
    friendshipsInputs = friendships_inputs()
    expectedOutputs = expected_outputs()



    for i in range(len(employeesInputs)):
        try:
            #prepare_data_set(employeesInputs[i], friendshipsInputs[i])
            result = create_adjacency_lists(employeesInputs[i], friendshipsInputs[i])
            expected = expectedOutputs[i]

            if (sorted(result.keys()) == sorted(expected.keys()) and
                all(map(lambda k: sorted(result[k]) == sorted(expected[k]), result.keys()))):
                print('Pass')
            else:
                print('Fail')
        except Exception as e:
            print('Fail')
            print(e)

if __name__ == "__main__":
    main()
