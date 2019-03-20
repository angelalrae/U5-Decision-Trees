import math

def main():
    header = ["level", "lang", "tweets", "phd", "interviewed_well"]
    table = [
            ["Senior", "Java", "no", "no", "False"],
            ["Senior", "Java", "no", "yes", "False"],
            ["Mid", "Python", "no", "no", "True"],
            ["Junior", "Python", "no", "no", "True"],
            ["Junior", "R", "yes", "no", "True"],
            ["Junior", "R", "yes", "yes", "False"],
            ["Mid", "R", "yes", "yes", "True"],
            ["Senior", "Python", "no", "no", "False"],
            ["Senior", "R", "yes", "no", "True"],
            ["Junior", "Python", "yes", "no", "True"],
            ["Senior", "Python", "yes", "yes", "True"],
            ["Mid", "Python", "no", "yes", "True"],
            ["Mid", "Java", "yes", "no", "True"],
            ["Junior", "Python", "no", "yes", "False"]
        ]
    # how to represent trees in Python?
    #1. OOP
    #2. nested data structures like lists!
    # we will use nested lists
    # task: Finish the tree!
    interview_tree = \
    ["Attribute", "level",
        ["Value", "Senior",
            ["Attribute", "tweets",
                ["Value", "yes",
                    ["Leaves", ["True", 2, 5, 40]]
                ],
                ["Value", "no",
                    ["Leaves", ["False", 3, 5, 60]]
                ]
            ]
        ],
        ["Value", "Mid",
            ["Leaves", ["True", 4, 14, 28.6]]
        ],
        ["Value", "Junior", 
            ["Attribute", "phd",
                ["Value", "yes", 
                    ["Leaves", ["False", 2, 5, 40]]
                ],
                ["Value", "no", 
                    ["Leaves", ["True", 3, 5, 60]]
                ]
            ]
        ]
    ]

def tdidt(intances, att_indexes, att_domains, class_index, header=None):
    # Basic Approach (uses recursion!):

    # At each step, pick an attribute ("attribute selection")
    att_index = select_attribute(instances, att_indexes, class_index)
    # Partition data by attribute values ... this creates pairwise disjoint partitions
    # Repeat until one of the following occurs (base cases):
    # Partition has only class labels that are the same ... no clashes, make a leaf node
    # No more attributes to partition ... reached the end of a branch and there may be clashes, see options below
    # No more instances to partition ... see options below

def select_attribute(instances, att_indexes, class_index):
    # random selection for now
    # TODO: replace with entropy-based attribute selection
    # task: return a random index in att_indexes

if __name__ == "__main__":
    main()