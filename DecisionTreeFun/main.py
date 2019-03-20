

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
        ["Value", "Mid"
        ],
        ["Value", "Junior"
        ]
    ]

if __name__ == "__main__":
    main()