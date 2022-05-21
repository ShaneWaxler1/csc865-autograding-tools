# csc865-autograding-tools
Python tools to automate the grading and plagiarism-checking process for CSC665/865 assignments. Designed to work with iLearn's student-submission download structure, but can be modified to work with any codebase.

## Instructions For Use

### Setup Environment
The only non-python related script used here is **unar**. Download **unar** here:
https://theunarchiver.com/command-line

Ensure **unar** works via your shell by typing:

```
unar --version
```

If this doesn't work, you may need to add unar to your PATH. You won't be able to unzip rar files without this.

Then, create a conda environment using the conda file included here:

```
conda create --name <env> --file requirements.txt
```

### Grading
Pull grades from iLearn (should be a zip file with a title like "CSC066502-S22R-8591-Assignment N-\_\_\_\_.zip"). Then, drop that file in the relevant /asn<N>/submissions directory. 
  
For example, if you download the submissions for assignment 1 for two sections, you should add and unzip them into asn1/submissions. You should now have 
  
  asn1/submissions/CSC066501-S22R-8591-Assignment N-\_\_\_\_ 
  
  _and_ 
  
  asn1/submissions/CSC066502-S22R-8591-Assignment N-\_\_\_\_
  
From here, you can remove the zip files and run 
  
```
python grader.py  
```
  
Once the grader is finished, you should be able to see a file called `grades.xlsx`. 
  
Note: this contains all the grades (split into sheets for each section) including any partial credit that may be earned _if and only if_ the student did not already get points for that question. Check the verbose output on the sheet for information about which questions the students already received credit for. Most relevant error messages will be displayed if there is an error grading (e.g. "missing file \_\_\_"). If the output says a file is missing, you should look into that student's submission and ensure they didn't change any file names. There is usually at least one student who renames a file accidentally, and their code will be ignored by the grader script. Grade those manually. Rarely, students compress folders with strange formats. These should also be graded manually.

### Plagiarism Analysis
Then, for plagiarism checking, place any past submissions in the moss folder titled `past-submissions` for the relevant assignment. Drop the root folders in directly (e.g. `/moss/past-submissions/fall2019/` and `/moss/past-submissions/online_code/`). 

Then, in the relevant assignment folder, run:
  
```
python run-moss.py  
```
  
The moss script can only be ran _after_ the grader script has executed successfully. This is very important. The grader script places all current student submissions into a directory in the moss folder. If this does not exist, the moss script will not include new student submissions. 
  
The moss script should print out a link to the relevant moss analysis page. The link expires after about 1.5 weeks. There is commented code at the bottom of each `run-moss.py` file which stores the plagiarism analysis locally if you'd like. It is entirely unnecessary though.

## Important Note
This project is specifically designed to work with the directory naming conventions I have chosen. There is an extremely high probability that it will not properly function if you change any of the names of folders, files, etc. For ease of use, don't rename anything. Even the downloads from iLearn. It will confuse the grader and the moss scripts. 
  
## Further Use
If you wish to use this project for your own purposes or to write your own similar-looking program, please give credit where credit is due. Thank you.
  
If you have any questions/concerns, submit them as issues to this repository, or email me directly. I'll be happy to assist.

This project uses Moss (http://theory.stanford.edu/~aiken/moss/) with Mosspy (https://github.com/soachishti/moss.py) to assess plagiarism for student submissions.
