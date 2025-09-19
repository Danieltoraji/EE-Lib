#function: make a pdf via latex that contains matmult quizs
#author: CBDT
#date: 24/9/9
import os
import math
import numpy as np
import time
MATMULT22CNT = 50
MATMULT33CNT = 50
MATMULT44CNT = 50

MATINV22CNT = 50
MATINV33CNT = 50
MATINV44CNT = 50

MATDET22CNT = 50
MATDET33CNT = 50
MATDET44CNT = 50
def print_matmult22(quiz, answer,num):
    #randomly generate 2x2 matrix,ints only!
    
    A = np.random.randint(-10, 10, (2, 2))
    B = np.random.randint(-10, 10, (2, 2))
    C = np.dot(A, B)
    #print A, B, C
    quiz.write("\\textbf{question%d}\n$$\nA = \\begin{bmatrix} %d & %d \\\\ %d & %d \\end{bmatrix} \\quad B = \\begin{bmatrix} %d & %d \\\\ %d & %d \\end{bmatrix} \\quad AB = ?\n$$\n" % (num,A[0, 0], A[0, 1], A[1, 0], A[1, 1], B[0, 0], B[0, 1], B[1, 0], B[1, 1]))
    answer.write("\\textbf{answer%d}\n$$\n\\begin{bmatrix} %d & %d \\\\ %d & %d \\end{bmatrix}\n$$\n" % (num,C[0, 0], C[0, 1], C[1, 0], C[1, 1]))
    return

def print_matmult33(quiz, answer,num):
    #randomly generate 3x3 matrix,ints only!
    
    A = np.random.randint(-10, 10, (3, 3))
    B = np.random.randint(-10, 10, (3, 3))
    C = np.dot(A, B)
    #print A, B, C
    quiz.write("\\textbf{question%d}\n$$\nA = \\begin{bmatrix} %d & %d & %d \\\\ %d & %d & %d \\\\ %d & %d & %d \\end{bmatrix} \\quad B = \\begin{bmatrix} %d & %d & %d \\\\ %d & %d & %d \\\\ %d & %d & %d \\end{bmatrix} \\quad AB = ?\n$$\n" % (num,A[0, 0], A[0, 1], A[0, 2], A[1, 0], A[1, 1], A[1, 2], A[2, 0], A[2, 1], A[2, 2], B[0, 0], B[0, 1], B[0, 2], B[1, 0], B[1, 1], B[1, 2], B[2, 0], B[2, 1], B[2, 2]))
    answer.write("\\textbf{answer%d}\n$$\n\\begin{bmatrix} %d & %d & %d \\\\ %d & %d & %d \\\\ %d & %d & %d \\end{bmatrix}\n$$\n" % (num,C[0, 0], C[0, 1], C[0, 2], C[1, 0], C[1, 1], C[1, 2], C[2, 0], C[2, 1], C[2, 2]))
    return

def print_matmult44(quiz, answer,num): 
    #randomly generate 4x4 matrix,ints only!
    
    A = np.random.randint(-10, 10, (4, 4))
    B = np.random.randint(-10, 10, (4, 4))
    C = np.dot(A, B)
    #print A, B, C
    quiz.write("\\textbf{question%d}\n$$\nA = \\begin{bmatrix} %d & %d & %d & %d \\\\ %d & %d & %d & %d \\\\ %d & %d & %d & %d \\\\ %d & %d & %d & %d \\end{bmatrix} \\quad B = \\begin{bmatrix} %d & %d & %d & %d \\\\ %d & %d & %d & %d \\\\ %d & %d & %d & %d \\\\ %d & %d & %d & %d \\end{bmatrix} \\quad AB = ?\n$$\n" % (num,A[0, 0], A[0, 1], A[0, 2], A[0, 3], A[1, 0], A[1, 1], A[1, 2], A[1, 3], A[2, 0], A[2, 1], A[2, 2], A[2, 3], A[3, 0], A[3, 1], A[3, 2], A[3, 3], B[0, 0], B[0, 1], B[0, 2], B[0, 3], B[1, 0], B[1, 1], B[1, 2], B[1, 3], B[2, 0], B[2, 1], B[2, 2], B[2, 3], B[3, 0], B[3, 1], B[3, 2], B[3, 3]))
    answer.write("\\textbf{answer%d}\n$$\n\\begin{bmatrix} %d & %d & %d & %d \\\\ %d & %d & %d & %d \\\\ %d & %d & %d & %d \\\\ %d & %d & %d & %d \\end{bmatrix}\n$$\n" % (num,C[0, 0], C[0, 1], C[0, 2], C[0, 3], C[1, 0], C[1, 1], C[1, 2], C[1, 3], C[2, 0], C[2, 1], C[2, 2], C[2, 3], C[3, 0], C[3, 1], C[3, 2], C[3, 3]))
    return

def print_matinv22(quiz, answer,num):
    #randomly generate 2x2 matrix,ints only!
    
    A = np.random.randint(-10, 10, (2, 2))
    if np.linalg.det(A) == 0:
        print_matinv22(quiz, answer,num)
        return
    B = np.linalg.inv(A)
    #print A, B
    quiz.write("\\textbf{question%d}\n$$\nA = \\begin{bmatrix} %d & %d \\\\ %d & %d \\end{bmatrix} \\quad A^{-1} = ?\n$$\n" % (num,A[0, 0], A[0, 1], A[1, 0], A[1, 1]))
    answer.write("\\textbf{answer%d}\n$$\n\\begin{bmatrix} %lf & %lf \\\\ %lf & %lf \\end{bmatrix}\n$$\n" % (num,B[0, 0], B[0, 1], B[1, 0], B[1, 1]))
    return

def print_matinv33(quiz, answer,num):
    #randomly generate 3x3 matrix,ints only!
    
    A = np.random.randint(-10, 10, (3, 3))
    if(np.linalg.det(A) == 0):
        print_matinv33(quiz, answer,num)
        return
    B = np.linalg.inv(A)
    
    #print A, B
    quiz.write("\\textbf{question%d}\n$$\nA = \\begin{bmatrix} %d & %d & %d \\\\ %d & %d & %d \\\\ %d & %d & %d \\end{bmatrix} \\quad A^{-1} = ?\n$$\n" % (num,A[0, 0], A[0, 1], A[0, 2], A[1, 0], A[1, 1], A[1, 2], A[2, 0], A[2, 1], A[2, 2]))
    answer.write("\\textbf{answer%d}\n$$\n\\begin{bmatrix} %lf & %lf & %lf \\\\ %lf & %lf & %lf \\\\ %lf & %lf & %lf \\end{bmatrix}\n$$\n" % (num,B[0, 0], B[0, 1], B[0, 2], B[1, 0], B[1, 1], B[1, 2], B[2, 0], B[2, 1], B[2, 2]))
    return


def print_matinv44(quiz, answer,num):
    #randomly generate 4x4 matrix,ints only!
    A = np.random.randint(-10, 10, (4, 4))
    if(np.linalg.det(A) == 0):
        print_matinv44(quiz, answer,num)
        return
    B = np.linalg.inv(A)
    
    #print A, B
    quiz.write("\\textbf{question%d}\n$$\nA = \\begin{bmatrix} %d & %d & %d & %d \\\\ %d & %d & %d & %d \\\\ %d & %d & %d & %d \\\\ %d & %d & %d & %d \\end{bmatrix} \\quad A^{-1} = ?\n$$\n" % (num,A[0, 0], A[0, 1], A[0, 2], A[0, 3], A[1, 0], A[1, 1], A[1, 2], A[1, 3], A[2, 0], A[2, 1], A[2, 2], A[2, 3], A[3, 0], A[3, 1], A[3, 2], A[3, 3]))
    answer.write("\\textbf{answer%d}\n$$\n\\begin{bmatrix} %lf & %lf & %lf & %lf \\\\ %lf & %lf & %lf & %lf \\\\ %lf & %lf & %lf & %lf \\\\ %lf & %lf & %lf & %lf \\end{bmatrix}\n$$\n" % (num,B[0, 0], B[0, 1], B[0, 2], B[0, 3], B[1, 0], B[1, 1], B[1, 2], B[1, 3], B[2, 0], B[2, 1], B[2, 2], B[2, 3], B[3, 0], B[3, 1], B[3, 2], B[3, 3]))
    return

def print_matdet22(quiz, answer,num):
    #randomly generate 2x2 matrix,ints only!
    
    A = np.random.randint(-10, 10, (2, 2))
    B = np.linalg.det(A)
    #print A, B
    quiz.write("\\textbf{question%d}\n$$\nA = \\begin{bmatrix} %d & %d \\\\ %d & %d \\end{bmatrix} \\quad |A| = ?\n$$\n" % (num,A[0, 0], A[0, 1], A[1, 0], A[1, 1]))
    answer.write("\\textbf{answer%d}\n$$\n%d\n$$\n" % (num,B))
    return

def print_matdet33(quiz, answer,num):
    #randomly generate 3x3 matrix,ints only!
    
    A = np.random.randint(-10, 10, (3, 3))
    B = np.linalg.det(A)
    #print A, B
    quiz.write("\\textbf{question%d}\n$$\nA = \\begin{bmatrix} %d & %d & %d \\\\ %d & %d & %d \\\\ %d & %d & %d \\end{bmatrix} \\quad |A| = ?\n$$\n" % (num,A[0, 0], A[0, 1], A[0, 2], A[1, 0], A[1, 1], A[1, 2], A[2, 0], A[2, 1], A[2, 2]))
    answer.write("\\textbf{answer%d}\n$$\n%d\n$$\n" % (num,B))
    return

def print_matdet44(quiz, answer,num):
    #randomly generate 4x4 matrix,ints only!
    
    A = np.random.randint(-10, 10, (4, 4))
    B = np.linalg.det(A)
    #print A, B
    quiz.write("\\textbf{question%d}\n$$\nA = \\begin{bmatrix} %d & %d & %d & %d \\\\ %d & %d & %d & %d \\\\ %d & %d & %d & %d \\\\ %d & %d & %d & %d \\end{bmatrix} \\quad |A| = ?\n$$\n" % (num,A[0, 0], A[0, 1], A[0, 2], A[0, 3], A[1, 0], A[1, 1], A[1, 2], A[1, 3], A[2, 0], A[2, 1], A[2, 2], A[2, 3], A[3, 0], A[3, 1], A[3, 2], A[3, 3]))
    answer.write("\\textbf{answer%d}\n$$\n%d\n$$\n" % (num,B))
    return

def main():
    #open files
    quiz = open("matprac.tex", "w")
    answer = open("matprac_answer.tex", "w")
    #make
    #latex!
    quiz.write("\\documentclass{article}\n")
    quiz.write("\\usepackage{amsmath}\n")
    quiz.write("\\begin{document}\n")
    quiz.write("\\title{Matrix Practice}\n")
    quiz.write("\\author{CBDT}\n")
    quiz.write("\\maketitle\n")
    #toc
    quiz.write("\\tableofcontents\n")
    quiz.write("\\section{Matrix Multiplication}\n")
    answer.write("\\documentclass{article}\n")
    answer.write("\\usepackage{amsmath}\n")
    answer.write("\\begin{document}\n")
    answer.write("\\title{Matrix Practice Answer}\n")
    answer.write("\\author{CBDT}\n")
    answer.write("\\maketitle\n")
    #toc
    answer.write("\\tableofcontents\n")
    answer.write("\\section{Matrix Multiplication}\n")
    
    for i in range(MATMULT22CNT):
        print_matmult22(quiz, answer,i+1)
    for i in range(MATMULT33CNT):
        print_matmult33(quiz, answer,i+MATMULT22CNT+1)
    for i in range(MATMULT44CNT):
        print_matmult44(quiz, answer,i+MATMULT22CNT+MATMULT33CNT+1)
    quiz.write("\\section{Matrix Inverse}\n")
    answer.write("\\section{Matrix Inverse}\n")
    for i in range(MATINV22CNT):
        print_matinv22(quiz, answer,i+1)
    for i in range(MATINV33CNT):
        print_matinv33(quiz, answer,i+MATINV22CNT+1)
    for i in range(MATINV44CNT):
        print_matinv44(quiz, answer,i+MATINV22CNT+MATINV33CNT+1)
    quiz.write("\\section{Matrix Determinant}\n")
    answer.write("\\section{Matrix Determinant}\n")
    for i in range(MATDET22CNT):
        print_matdet22(quiz, answer,i+1)
    for i in range(MATDET33CNT):
        print_matdet33(quiz, answer,i+MATDET22CNT+1)
    for i in range(MATDET44CNT):
        print_matdet44(quiz, answer,i+MATDET22CNT+MATDET33CNT+1)
    quiz.write("\\end{document}\n")
    answer.write("\\end{document}\n")
    #close files
    quiz.close()
    answer.close()
    #compile
    os.system("pdflatex matprac.tex")
    os.system("pdflatex matprac_answer.tex")
    #compile again for toc
    os.system("pdflatex matprac.tex")
    os.system("pdflatex matprac_answer.tex")
    
    #remove useless files(.aux,.fdb_latexmk,...)
    t = time.time()%114514
    os.makedirs("口算题卡%d"%(t))
    os.rename("matprac.pdf","口算题卡%d/练习题%d.pdf"%(t,t))
    os.rename("matprac_answer.pdf","口算题卡%d/答案%d.pdf"%(t,t))
    
    os.remove("matprac.tex")
    os.remove("matprac_answer.tex")
    os.remove("matprac.aux")
    os.remove("matprac.log")
    os.remove("matprac.toc")
    os.remove("matprac_answer.aux")
    os.remove("matprac_answer.log")
    os.remove("matprac_answer.toc")
    return
if __name__ == "__main__":
    main()
    