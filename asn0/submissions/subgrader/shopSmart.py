# shopSmart.py
# ------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders:  [('apples', 1.0), ('oranges', 3.0)] best shop is shop1
For orders:  [('apples', 3.0)] best shop is shop2
"""
from __future__ import print_function
import shop


def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    """
    "*** YOUR CODE HERE ***"
    orders1 = [('apples',1.0), ('oranges',3.0)]
    orders2 = [('apples',3.0)]
    dir1 = {'apples': 2.0, 'oranges':1.0}
    shop1 =  shop.FruitShop('shop1',dir1)
    dir2 = {'apples': 1.0, 'oranges': 5.0}
    shop2 = shop.FruitShop('shop2',dir2)
    shops = [shop1, shop2]
    count = 0
    totalCost_O1S1 = 0
    totalCost_O1S2 = 0
    totalCost_O2S1 = 0
    totalCost_O2S2 = 0

    order1_fruits = []
    order1_count = []
    for item in orders1:
        order1_fruits.append(item[0])
        order1_count.append(item[1])
        order1_fruits = []
    order2_fruits = []
    order2_count = []
    for item in orders1:
        order2_fruits.append(item[0])
        order2_count.append(item[1])
    for i in orders1:
        if i == 'apples':
            totalCost_O1S1 = totalCost_O1S1 + order1_count[count] * 2
        elif i == 'oranges':
            totalCost_O1S1 = totalCost_O1S1 + order1_count[count] * 1
        elif i == 'pears':
            totalCost_O1S1 = totalCost_O1S1 + order1_count[count] * 0
        elif i == 'limes':
            totalCost_O1S1 = totalCost_O1S1 + order1_count[count] * 0
        elif i == 'strawberries':
            totalCost_O1S1 = totalCost_O1S1 + order1_count[count] * 0
        count = count + 1
    for i in orders2:
        if i == 'apples':
            totalCost_O2S1 = totalCost_O2S1 + order1_count[count] * 2
        elif i == 'oranges':
            totalCost_O2S1 = totalCost_O2S1 + order1_count[count] * 1
        elif i == 'pears':
            totalCost_O2S1 = totalCost_O2S1 + order1_count[count] * 0
        elif i == 'limes':
            totalCost_O2S1 = totalCost_O2S1 + order1_count[count] * 0
        elif i == 'strawberries':
            totalCost_O2S1 = totalCost_O2S1 + order1_count[count] * 0
        count = count + 1
    for i in orders1:
        if i == 'apples':
            totalCost_O1S2 = totalCost_O1S2 + order1_count[count] * 1
        elif i == 'oranges':
            totalCost_O1S2 = totalCost_O1S2 + order1_count[count] * 5
        elif i == 'pears':
            totalCost_O1S2 = totalCost_O1S2 + order1_count[count] * 0
        elif i == 'limes':
            totalCost_O1S2 = totalCost_O1S2 + order1_count[count] * 0
        elif i == 'strawberries':
            totalCost_O1S2 = totalCost_O1S2 + order1_count[count] * 0
        count = count + 1
    for i in orders1:
        if i == 'apples':
            totalCost_O2S2 = totalCost_O2S2 + order1_count[count] * 1
        elif i == 'oranges':
            totalCost_O2S2 = totalCost_O2S2 + order1_count[count] * 5
        elif i == 'pears':
            totalCost_O2S2 = totalCost_O2S2 + order1_count[count] * 0
        elif i == 'limes':
            totalCost_O2S2 = totalCost_O2S2 + order1_count[count] * 0
        elif i == 'strawberries':
            totalCost_O2S2 = totalCost_O2S2 + order1_count[count] * 0
        count = count + 1
    if totalCost_O1S2 > totalCost_O1S1:
        return shop1
    else:
        return shop2

    


if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orders = [('apples', 1.0), ('oranges', 3.0)]
    dir1 = {'apples': 2.0, 'oranges': 1.0}
    shop1 = shop.FruitShop('shop1', dir1)
    dir2 = {'apples': 1.0, 'oranges': 5.0}
    shop2 = shop.FruitShop('shop2', dir2)
    shops = [shop1, shop2]
    print("For orders ", orders, ", the best shop is", shopSmart(orders, shops).getName())
    orders = [('apples', 3.0)]
    print("For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName())
