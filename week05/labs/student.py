#program to record students modules and grades
#Author: David Higgins

student = {"name" : "David",
    "modules" : [{"courseName" : "Programming",
                    "grade" : 100},
                {"courseName" : "Maths",
                    "grade" : 95}]
            }

print("Student: {}".format(student["name"]))

for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))