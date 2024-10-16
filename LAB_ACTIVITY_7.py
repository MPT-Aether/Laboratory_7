"""
Write a Write a Python program that will calculate the student's 
final grade and display the grade points and its description based on 
this table:

Grade Points       Percentage Equivalent       General Description
   1.00                  99-100%                    Excellent
   1.25                  96-98%                    Outstanding
   1.50                  93-95%                      Superior
   1.75                  90-92%                     Very Good
   2.00                  87-89%                       Good
   2.25                  84-86%                   Satisfactory
   2.50                  81-83%                Fairly Satisfactory
   2.75                  78-80%                       Fair
   3.00                  75-77%                      Passed
   5.0                   Below 75%                   Failed


Bases of Grades

The following factors shall be considered in the computation in grades:

Preliminary Period Grade     = 33.33%
Midterm Period Grade         = 33.33%
Final Period Grade           = 33.33%
Final Grade                  = sum of all the period grades

"""

# Input of Student's Identification and Grade Data for Prelim, Midterm, and Final

student_name = (input("Please input the student's name: "))
student_section = (input("Please input the section's section: "))
preliminary_period_grade = round(float(input("Enter his/her Preliminary Period Grade: ")), 2)
midterm_period_grade = round(float(input("Enter his/her Midterm Period Grade: ")), 2)
final_period_grade = round(float(input("Enter his/her Final Period Grade: ")), 2)

# Analytical Calculation of Final Grade

# Final Grade Analysis Calculation 
base_final_period_grade = float(0.3333 * preliminary_period_grade + 0.3333 * midterm_period_grade + 0.333 * final_period_grade)

final_grade = round(base_final_period_grade)

# Display of Student's Results and Performance Statistics
if final_grade >= 99 and final_grade <= 100:
    print(" \nName: {} \nSection: {} \nFinal Grade: {} \nGPA: 1.00 \nDear Parents, {} from {} has a Grade Point of 1.00 and he or she has an Excellent and Recommended Performance!" .format(student_name, student_section, final_grade, student_name, student_section))

elif final_grade >= 96 and final_grade <= 98:
    print(" \nName: {} \nSection: {} \nFinal Grade: {} \nGPA: 1.25 \nDear Parents, {} from {} has a grade point of 1.25 and he or she has an Outstanding and Recommended Performance!" .format(student_name, student_section, final_grade, student_name, student_section))
    
elif final_grade >= 93 and final_grade <= 95:
    print(" \nName: {} \nSection: {} \nFinal Grade: {} \nGPA: 1.50 \nDear Parents, {} from {} has a grade point of 1.50 and he or she has a Superior and Recommended Performance!" .format(student_name, student_section, final_grade, student_name, student_section))

elif final_grade >= 90 and final_grade <= 92:
    print(" \nName: {} \nSection: {} \nFinal Grade: {} \nGPA: 1.75 \nDear Parents, {} from {} has a grade point of 1.75 and he or she has a Very Good and Recommended Performance!" .format(student_name, student_section, final_grade, student_name, student_section))

elif final_grade >= 87 and final_grade <= 89:
    print(" \nName: {} \nSection: {} \nFinal Grade: {} \nGPA: 2.00 \nDear Parents, {} from {} has a grade point of 2.00 and he or she has a Good and Commended Performance!" .format(student_name, student_section, final_grade, student_name, student_section))

elif final_grade >= 84 and final_grade <= 86:
    print(" \nName: {} \nSection: {} \nFinal Grade: {} \nGPA: 2.25 \nDear Parents, {} from {} has a grade point of 2.25 and he or she has a Satisfactory and Commended Performance!" .format(student_name, student_section, final_grade, student_name, student_section))

elif final_grade >= 81 and final_grade <= 83:
    print(" \nName: {} \nSection: {} \nFinal Grade: {} \nGPA: 2.50 \nDear Parents, {} from {} has a grade point of 2.50 and he or she has a Fairly Satisfactory Performance." .format(student_name, student_section, final_grade, student_name, student_section))

elif final_grade >= 78 and final_grade <= 80:
    print(" \nName: {} \nSection: {} \nFinal Grade: {} \nGPA: 2.75 \nDear Parents, {} from {} has a grade point of 2.75 and he or she has a Fair Performance." .format(student_name, student_section, final_grade, student_name, student_section))

elif final_grade >= 75 and final_grade <= 77:
    print(" \nName: {} \nSection: {} \nFinal Grade: {} \nGPA: 3.00 \nDear Parents, {} from {} has a grade point of 3.00 and he or she has Passed ^w^." .format(student_name, student_section, final_grade, student_name, student_section))
    
elif final_grade >= 40 and final_grade <= 74:
    print(" \nName: {} \nSection: {} \nFinal Grade: {} \nGPA: 5.0 \nDear Parents, your son/daughter, {} from {} has Failed with a grade point of 5.0 and is recommended to be held back for another session as an irregular:<" .format(student_name, student_section, final_grade, student_name, student_section))
    
input()