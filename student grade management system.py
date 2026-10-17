def calculate_average(marks):#create a function named calculate average
    total=sum(marks)#implement a built in function sum to add all the marks that we give & stored in the variable total
    average=total/len(marks)#total of marks divided by number of marks then we get average of marks
    return average
def get_grade(average):#defines function to recieve average to check grade
    if average >= 90:#checks the average greater than 90,80,70,60 and print suitable grades
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:#average less than 60 print grade f
        return "F"
def main():#create main function 
    marks=[]
    print("Student Grade Management System")
    print("Enter the Marks for 5 subjects between 0-100")
    for i in range(1,6):#craete a block of code for ask marks of subjects
        while True:
            try:#enter marks inside try block because it may cause any error python attempts to execute statements
                mark=float(input(f"Enter Marks for subjects {i}:"))
                if 0 <= mark <= 100:#marks between 0 and 100
                    marks.append(mark)#we can add the mark at the end through append
                    break
                else:
                    print("invalid Mark Enter a Value between 0-100")
            except ValueError:#add an error name which more possibility to raise during this program
                print("Invalid input!,please Enter a numeric value")
    average=calculate_average(marks)#call the functions for grade and average and print
    grade=get_grade(average)
    print(f"\n Student result")
    print(f"Average Marks = {average:.1f}")
    print(f"Grade = {grade}")
if __name__ =="__main__":#call main function
    main()
    
    
