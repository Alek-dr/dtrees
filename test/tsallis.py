import pandas as pd
from core.decision_tree import DecisionTree
from graph_visualize.dot_convertor import export2dot
from utils.help_functions import train_test_split

from core.graph import Node
from numpy import zeros

def train():
    iris = pd.read_csv('datasets/Iris.csv')
    iris.drop("Id",axis=1,inplace=True)

    train, test = train_test_split(iris)

    dt = DecisionTree()
    dt.learn(data=train, target='Species', criterion='Tsallis',q=2.1)

    # out_name = 'tennis_ts'
    # export2dot(out_name, dt.tree, writeId=True)
    #
    # dt.save(out_name+'.pkl')

def test_1():
    dt = DecisionTree()
    dt.load('tennis_2.pkl')
    # example = pd.DataFrame({'Outlook': 'Sunny','Temperature': 70, 'Humidity': None, 'Wind':'No'}, index=[0])
    example = pd.DataFrame({'Outlook': 'Rain', 'Temperature': 70, 'Humidity': 73, 'Wind': None}, index=[0])
    res = dt.tree._predict_(example, dt.tree.getNode(0))
    print(res)

def test_2():
    dt = DecisionTree()
    dt.load('tennis_2.pkl')
    node = Node(8)
    node.attr = 'No'

    weightsPerClass = zeros(2, dtype={'names': ('label', 'weight'),
                                                  'formats': ('U3', 'f8')})
    weightsPerClass['label'] = ['Yes','No']
    weightsPerClass['weight'] = [1,2]
    W = 3
    stat = {'W': W, 'WeightsPerClass': weightsPerClass}
    node.stat = stat
    dt.tree.addNode(node,4)
    dt.tree._pruneSameChild_()

if __name__=='__main__':
    train()
    # test_1()
    # test_2()