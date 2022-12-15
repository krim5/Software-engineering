student('Mark', male, excellent).
student('John', male, satisfactorily).
student('Mary', female, good).
student('Alice', female, satisfactorily).

welldone(X, _ , _):- 
    student(X, _, excellent); student(X, _, good).
	?- write("Well done boys and girls!").