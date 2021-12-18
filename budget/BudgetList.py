

import budget


class BudgetList: 
 def _init_(self, budget):
  self.budget = budget
  self.sum_expenses = 0
  self.expenses = []
  self.sum_overages = 0
  self.overages = []
  def _init_(self, item):
    if self.sum_expenses + item < self.budget:
       self.expenses.append(item)
       item+ self.sum_expenses
       else:
        self.overages.append(item)
        self.sum_overages = self.sum_overages+item
        
