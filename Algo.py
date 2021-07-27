import numpy as np
import cv2 as cv

number_of_questions = 16
number_of_answers = 5
d = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E'}
correct_answers = []
def extract_case(img,qst_num,answer_num):
    img_temp = img[:,36:-2]
    if (qst_num > number_of_questions or answer_num > number_of_answers):
        raise Exception("question number or answer number is invalid") 
        return 0
    else:
        return img_temp[  22*(qst_num-1) : 22*(qst_num)  ,  18*(answer_num-1) : 18*(answer_num)  ]
    
def im_show(winname,img):
    while (1):
        cv.imshow(winname,img)
        if cv.waitKey(0) & 0xFF == 27:
            cv.destroyAllWindows()
            break

def is_it_marked(img,qst_num,answer_num):
    case = extract_case(img,qst_num,answer_num)
    k=0
    for i in range(17):
        for j in range(17):
            if 100 > case[i][j]:
                k+=1
    if k > 50:
        return True
    else:
        return False
    
def answers_from_tab(img):
    answers = ["null" for i in range(number_of_questions)]
    for i in range( 1 , number_of_questions+1 ):  #questions
        for j in range( 1 , number_of_answers+1): #answers
            if ( is_it_marked(img,i,j) ):
                answers[i-1] = d[j]
                break
    return answers

def answers_from_image(img):
    
    #PREPARE THE IMAGE
    img_t = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    img_t = cv.resize(img_t,(int(1654/2),int(2339/2))) 

    #DETECT COUNTOURS
    edges = cv.Canny(img_t,0,255)
    cntrs, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    #EXTRACTING THE TABS FROM IMAGE
    i = 0
    keys = []
    tabs = []
    X = []
    Y = []
    W = []
    H = []
    for cnt in cntrs:
        x,y,w,h = cv.boundingRect(cnt)
        if 3.49 > h/w > 3.47 or 2.8 > h/w > 2.77:
            X.append(x)
            Y.append(y)
            W.append(w)
            H.append(h)
    n = len(X) #number of tabs
    same_y = 1
    for j in range(1,n):
        if Y[0] == Y[j]:
            same_y+=1 #tabs in the same horiz line
    if same_y == n:
        for k in range(n):
            f = np.argmin(X)
            keys.append([ Y[f] , Y[f]+H[f] , X[f] , X[f]+W[f] ])
            X[f] = 999 #close it
    else:   
        for k in range(n):
            keys.append([ Y[k] , Y[k]+H[k] , X[k] , X[k]+W[k] ])
        t=keys[0]
        keys[0]=keys[3]
        keys[3]=t

    for tab_ix in range(0,n):
        tabs.append(img_t[keys[tab_ix][0]:keys[tab_ix][1],keys[tab_ix][2]:keys[tab_ix][3]])
    
    #GETTING THE ANSWERS OF EACH TAB
    a = []
    for i in range(len(tabs)):
        a.append(answers_from_tab(tabs[i]))
    a = np.array(a).flatten() # +++++
    return a
        
def get_score(img,solution):
    answers = answers_from_image(img)
    n = len(answers)
    m = np.size(answers[0])
    score = 0
    for i in range(n): # number of answ
        if answers[i] != 'null':
            if answers[i] == solution[i]:
                score+=1
    return score
