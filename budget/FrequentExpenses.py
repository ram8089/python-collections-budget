from . import Expense
import collections
import matplotlib.pyplot as plt

#reading the expenses
expenses = Expense.Expenses()
expenses.read_expenses( "data/spending_data.csv")

# spending by categories
spending_categories = []
for exp in expenses.list:
    spending_categories.append(exp.category)
spending_counter = collections.Counter(spending_categories)
print(spending_counter)

#top5 category spendings
top5 = spending_counter.most_common(5)
categories, count = zip(*top5)
# plotting
fig, ax = plt.subplots()
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')
plt.show()

