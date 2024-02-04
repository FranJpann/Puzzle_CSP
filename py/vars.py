Alpacino = {
    "name": "Alpacino",
    "file": "E:\Workspace\Puzzle_CSP\mzn\Alpacino.mzn",
    "Columns": ["Film", "Day", "Time"],
    "Rows": ["Name", "Time", "Day"],
    "Data": {
        "Film": ["88 Minutes", "Donnie Brasco", "Scarecrow", "Scarface", "The Recruit"],
        "Name": ["Jessica", "Laurie", "Mark", "Mary", "Sally"],
        "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "Time": ["7:35", "7:40", "8:20", "8:30", "8:45"]
    },
    "Constraints":
        ["1. Of the 20-hundreds releases, neither of which was Jessica's choice, one opened the week and one "
         "closed the week.",
         "2. The latest of the 19-hundreds releases was shown at 30 minutes past the hour.",
         "3. The releases shown before 8:00 pm were on consecutive days, as were the releases shown after "
         "8:00 pm.",
         "4. One of the men and one of the women had a showing before 8:00 pm, but neither was mid-week.",
         "5. Mark, whose choice was Scarecrow, had a showing at a time of one hour and five minutes after "
         "that of Scarface.",
         "6. Neither Miss Farmer nor Miss Peters had a showing on an even-numbered day",
         "7. 88 Minutes showed at a time both 40 minutes to the hour and 40 minutes after the Thursday "
         "showing."]
}

Computers = {
    "name": "Computers",
    "file": "E:\Workspace\Puzzle_CSP\mzn\personal_computer.mzn",
    "Columns": ["Processor", "Hard Disk", "Price"],
    "Rows": ["Monitor", "Price", "Hard Disk"],
    "Data": {
        "Monitor": ["13'", "15'", "15.6'", "21.5'", "27'"],
        "Processor": ["2.0 MHz", "2.3 MHz", "2.5 MHz", "2.7 MHz", "3.1 MHz"],
        "Hard Disk": ["250 Gb", "320 Gb", "500 Gb", "750 Gb", "1024 Gb"],
        "Price": ["$ 699,00", "$ 999,00", "$ 1.149,00", "$ 1.349,00", "$ 1.649,00"]
    },
    "Constraints":
        ["1. Andrew bought the computer which was three hundred Euros less than the PC which has a processor\n"
         "that is 0.4 MHz more powerful than the one which has a 21.5' screen.",
         "2. The ve computers are: the one chosen by Andrew (which doesn't have the 27' screen),\n "
         "the one which has the 2.0-MHz processor, the computer that has a 250 GB HD, the one which has a\n "
         "price of 1,149 Euros and the computer (which doesn't have the 15' screen) that has the HD bigger\n "
         "than the one chosen by Andrew but smaller than that the one which has the 2.7 MHz processor.",
         "3. The computer with the 320 Gb HD has either the 2.0 or the 2.3 MHz processor.The processor of\n "
         "the computer which has the 15' screen is more powerful than the one in the computer that costs 999\n"
         "euros but less powerful than the processor that is included in the 1,349 Euros computer.",
         "4. The computer that has the 27' screen doesn't have the 320 Gb hard drive. The 500 GB HD is\n "
         "included in the computer that has a more powerful processor and a larger size screen than the one\n "
         "which costs 699 euros (which doesn't include the 320 Gb HD)."]
}

Pastawine = {
    "file": "E:\Workspace\Puzzle_CSP\mzn\pastawine.mzn",
    "options_array": [
        ["", "red", "blue", "green", "white", "yellow"],
        ["", "Holly", "Andrea", "Julie", "Leslie", "Victoria"],
        ["", "Davis", "Wilson", "Miller", "Lopes", "Brown"],
        ["", "farfalle", "lasagne", "penne", "spaghetti", "ravioli"],
        ["", "Italian", "French", "Chilean", "Argentine", "Australian"],
        ["", "30 years", "35 years", "40 years", "45 years", "50 years"]
    ],

    "options_left": [
        "Shirt", "Name", "Surname", "Pasta", "Wine", "Age"
    ],

    "options_top": [
        "Woman #1", "Woman #2", "Woman #3", "Woman #4", "Woman #5"
    ],

    "constraints":
        ["The woman wearing the White shirt is next to the woman who likes Lombardian wines.",
         "Ms Miller is somewhere between Ms Davis and Ms Brown, in that order.",
         "The youngest woman is at the third position.",
         "The 45-year-old woman is somewhere to the right of the woman wearing the Red shirt.",
         "The woman who likes Chilean wines also likes Farfalle.",
         "At the first position is the woman that likes Argentine wines.",
         "Andrea is exactly to the right of the 35-year-old woman.",
         "The woman wearing the Blue shirt is somewhere between Ms Davis and Holly, in that order.",
         "Victoria is next to Leslie.",
         "The woman wearing the Red shirt is somewhere to the left of the woman who likes Australian wines.",
         "Ms Wilson is next to the 30-year-old woman.",
         "Leslie is exactly to the left of the 30-year-old woman.",
         "Holly is somewhere to the right of the woman wearing the Red shirt.",
         "Ms Brown is exactly to the left of Julie.",
         "The youngest woman likes Penne.",
         "Ms Wilson is wearing the White shirt.",
         "The woman who likes Lasagne is somewhere between the woman who likes Italian wines and the woman who likes "
         "Spaghetti, in that order.",
         "At the second position is the woman wearing the Blue shirt.",
         "The 40-year-old woman likes Lasagne.",
         "Ms Lopes is at the fth position.",
         "The woman that likes Australian wines is somewhere between Victoria and the woman who likes wines from "
         "Bordeaux, in that order.",
         "The woman wearing the Yellow shirt is exactly to the left of the 35-year-old woman."
         ]
}
