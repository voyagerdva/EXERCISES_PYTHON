class listOperation():
    def listSort(self, subj):
        return subj.sort(key = lambda x: x[1])

inst = listOperation()
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

print("\nOriginal list of tuples:")
print("---", subject_marks)

inst.listSort(subject_marks)
print("\nSorting the List of Tuples:")
print("+++", subject_marks)
