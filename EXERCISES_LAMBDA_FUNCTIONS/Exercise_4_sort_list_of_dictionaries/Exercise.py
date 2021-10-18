
class Lam():
    def sortedList(self, models):
        return sorted(models, key = lambda x: x["color"])

brands = Lam()

models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print(f"\nOriginal list of dictionaries:\n {models}")

sorted_models = brands.sortedList(models)
print(f"\nSorting the list of dictionaries :\n {sorted_models}")