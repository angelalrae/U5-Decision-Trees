import random

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

    # dictionary of attribute index: attribute value pairs
    att_domains = {0: ["Senior", "Mid", "Junior"], 
        1: ["R", "Python", "Java"],
        2: ["yes", "no"], 
        3:["yes", "no"]}
    # att_indexes is a list of attributes to use for building the tree
    att_indexes = list(range(len(header) - 1))
    class_index = len(header) - 1
    tree = tdidt(table, att_indexes, att_domains, class_index, header)

def tdidt(instances, att_indexes, att_domains, class_index, header=None):
    # Basic Approach (uses recursion!):

    # At each step, pick an attribute ("attribute selection")
    att_index = select_attribute(instances, att_indexes, class_index)
    # can't choose the same attribute twice in a branch!!
    att_indexes.remove(att_index) # remember: Python is pass
    # by object reference!! 
    print("Splitting on:", att_index, header[att_index])

    # Partition data by attribute values ... this creates pairwise disjoint partitions
    partition = partition_instances(instances, att_index, att_domains[att_index])
    print(partition)
    # Repeat until one of the following occurs (base cases):
    # Partition has only class labels that are the same ... no clashes, make a leaf node
    # No more attributes to partition ... reached the end of a branch and there may be clashes, see options below
    # No more instances to partition ... see options below

    return None

def partition_instances(instances, att_index, att_domain):
    # this is a group by att_domain, not by att_values in instances
    partition = {}
    for att_value in att_domain:
        subinstances = []
        for instance in instances:
            # check if this instance has att_value at att_index
            if instance[att_index] == att_value:
                subinstances.append(instance)
        partition[att_value] = subinstances
    return partition

def select_attribute(instances, att_indexes, class_index):
    # random selection for now
    # TODO: replace with entropy-based attribute selection
    # task: return a random index in att_indexes
    rand_index = random.randrange(0, len(att_indexes))
    return att_indexes[rand_index]

if __name__ == "__main__":
    main()