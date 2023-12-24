from cmath import pi
from colored import attr, bg, fg
import os, time, random
# if ever, change christmas tree's color from pink to green---sakit sa mata
# Shades of Pink
pink1, pink2, pink3, pink4, pink5, pink6 = fg(198), fg(199), fg(162), fg(204), fg(206), fg(205) 
y, g, reset, brown, r, w =  fg(190), fg(2), '\033[0m', fg(214 ), fg(1), fg(7)
white = fg(231)
w = "\033[0;97;1m"
root = "A"
tab = "\t" 
os.system('cls') #----------------------------------------------------------------
import intro
time.sleep(1)
os.system('cls')

# A tree node
class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None
# A queue node
class Queue:
	def __init__(self):
		self.front = None
		self.rear = None
		self.size = 0
		self.array = []

def newNode(data):
	temp = Node(data)
	return temp

def createQueue(size):
	global queue
	queue = Queue()
	queue.front = queue.rear = -1
	queue.size = size
	queue.array = [None for i in range(size)]
	return queue

def isEmpty(queue):
	return queue.front == -1

def isFull(queue):
	return queue.rear == queue.size - 1

def hasOnlyOneItem(queue):
	return queue.front == queue.rear

def Enqueue(root):
	if (isFull(queue)):
		return
	
	queue.rear+=1
	queue.array[queue.rear] = root

	if (isEmpty(queue)):
		queue.front+=1

def Dequeue():
	if (isEmpty(queue)):
		return None

	temp = queue.array[queue.front]

	if(hasOnlyOneItem(queue)):
		queue.front = queue.rear = -1
	else:
		queue.front+=1

	return temp

def getFront(queue):
	return queue.array[queue.front]

def hasBothChild(temp): #------------------------------------------------------------------------------------------------------------------------------------------------
	#get all parent nodes
	if (temp) and temp.left or temp.right:
		parent_nodes.add(f"( {temp.data} )")
	# get all siblings
	if (temp and temp.left and temp.right):
		siblings.append(f"( {temp.left.data} ) and ( {temp.right.data} )")
	return (temp and temp.left and temp.right)
	
def insert(root, data, queue):
	temp = newNode(data)
	if not root:
		root = temp
	else:
		front = getFront(queue)
		if (not front.left):
			front.left = temp
		elif (not front.right):
			front.right = temp
		if (hasBothChild(front)):
			Dequeue()
	Enqueue(temp)
	return root

def levelOrder(root):
	queue = createQueue(SIZE)
	Enqueue(root)

	levels = [1] # for displaying level by level
	for i in range(getHeight(root)):
		levels.append(levels[-1]*2)
	
	nodes_per_level = []
	i = 1
	temp_nodes = []
	while (not isEmpty(queue)):
		temp = Dequeue()	
		#get all leaf nodes
		if not temp.right and not temp.left:
			leaf_nodes.append(f"( {temp.data} )")
			degree[temp.data] = 0
		
		if i in levels:
			nodes_per_level.append(f"{' '*8}".join(temp_nodes))
			temp_nodes = []
		temp_nodes.append(temp.data)

		# get degree
		if temp.right and temp.left:
			degree[temp.data] = 2
		elif (not temp.right and temp.left) or (temp.right and not temp.left):
			degree[temp.data] = 1
		#-------
		if (temp.left):
			Enqueue(temp.left)
		if (temp.right):
			Enqueue(temp.right)
		i+=1
	else:
		nodes_per_level.append(f"{' '*8}".join(temp_nodes))


def get_paths(stack, root):
    if root == None:
        return
    # append this node to the path array
    stack.append(root.data)
    if(root.left == None and root.right == None):
        paths.append(' ➡  '.join([str(i) for i in stack]))
    # otherwise try both subtrees
    get_paths(stack, root.left)
    get_paths(stack, root.right)
    stack.pop()

def getHeight(root):
	return -1 if root is None else 1 + max(getHeight(root.left),getHeight(root.right))

def maxDepth(node):
    if node is None:
        return -1 
    else :
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1


def colorText(text, lis): #for text file coloring
    for color in lis:
        text = text.replace("[[" + color + "]]", lis[color])
    return text        
        
def green_bar_colors():
    frames = []
    for name in ['green_bar1.txt', 'green_bar2.txt', 'green_bar3.txt', 'green_bar4.txt']:
        with open(name, 'r', encoding='UTF-8') as f:
            frames.append(f.readlines())
    for i in range(2):
        for frame in frames:
            ascii = ''.join(frame)
            print(colorText(ascii, {"white":"\033[1;30;0m", "green": "\033[32m"}))
            time.sleep(0.7)
            os.system('cls')

# Properties
parent_nodes = set()
child_nodes = set()
leaf_nodes = []
siblings = []
degree = {}
paths = []
SIZE = 19

if __name__ == "__main__":
	
	root = None
	queue = createQueue(SIZE)
	tab2 = "\t\t\t\t\t\t\t\t\t\t\t\t"
	f = open('space1.txt', 'r')
	content = f.read()
	print(content)
	f.close()
	print(f'''    .      *       o       .       *                                         *  o     .____________________________________________________     .      *       o       .       *       *  o     .  *   &    * $          -
                .           o       .      *       o       .       *        *     *   |                                                    |                                                   *   .         $
        .---.                       *  o     .    '       *               *           | {pink1} █▀▀ {pink2}█▀█ {pink3}█░█ {pink4}█▄░█{pink5} ▀█▀ {pink6}  ▀█▀{pink1} █▀█ {pink2}  ▀█▀{pink3} █▀█ {pink4}█▀▀{pink5} █▀▀  {white}|  - ) -       *          .                .  *            *   .
  =   _/__~0_\_     .  *            o       '                             .     .  *  | {pink1} █▄▄{pink2} █▄█ {pink3}█▄█{pink4} █░▀█{pink5} ░█░  {pink6} ░█░ {pink1}█▄█ {pink2}  ░█░{pink3} █▀▄ {pink4}██▄ {pink5}██▄  {white}|      *   .                   *   .                              *   .
 = = (_________)             .  *          .             .  *       - )-    *         |                                                    |              .---.                       *  o     .    '       *   
                 .                        *     *  o     .    '       *   .     .     |                                                    |        =   _/__~0_\_     .  *            o       '     *   .
       *               - ) -       *                                      *           |      {pink6}   Enter number of nodes from 10-20:  {white}        |       = = (_________)             .  *          .         *   . *    _
       *      -0-                   .      *       o       .       *        *     *   |____________________________________________________|                       - ) -       *          .                .  *
        .      *       o       .       *       *  o     .    '       *                                                                 .     .  *        *                     *  o     .    '       *     ''')

	nodes_num = 1
	while True:
		nodes_num = input(f'''{tab2}{pink6}{' '*12}   → {white}  ''')
		if nodes_num.isnumeric() and 10 <= int(nodes_num) <=20:
			nodes_num = int(nodes_num)
			break
	os.system("cls")
	green_bar_colors()

	for i, letter in enumerate(list("ABCDEFGHIJKLMNOPQRST")):
		if i+1 <= nodes_num:
			root=insert(root, letter, queue)
		else:
			break
		if i > 0:
			child_nodes.add(f"( {letter} )")
	
	levelOrder(root)

get_paths([], root)

def b_slash(num):
	if num <= nodes_num:
		return '\\'
	else: return pink4+'<'

def f_slash(num):
	if num <= nodes_num:
		return '/'
	else: return pink4+'>'

def pipe(num):
	if num <= nodes_num:
		return '|'
	else: return pink4+'<'

def u_score(num):
	if num <= nodes_num:
		return '_'
	else: return pink4+'>'

def node(node, num):
	if num <= nodes_num:
		return node
	else: return pink4+"<<.>>*"

normal_c = w
leveltwo_c = w #\fg(187)
levelthree_c = w#fg(186)
levelfour_c = w#fg(221)
levelfive_c = w#fg(220)
print(f"""{y}
{tab}                                                                                                         ^
{tab}                                                                                                     __/   \__
{tab}{w}Level 0:{y}                                                                                            <   {y} Ａ {y}  >
{tab}                                                                                                     /.-..-.-.\{pink4} 
{tab}                                                                                                  >>>>.<<{brown}/\{pink4}<.<<<.<{pink4}><
{tab}                                                                                                >>>>.<<*{brown}/{pink4}<<{brown}\{pink4}*>>>>>*{pink4}><
{tab}                                                                                              >>>>.*.<<{brown}/{pink4}<<*<{brown}\{pink4}<...<*<<{pink4}><
{tab}                                                                                            >>>>.*.<<*{brown}/{pink4}<<*<.>{brown}\{pink4}*>>*>>.*>{pink4}><
{tab}                                                                                          >>>>.*.<<*.{brown}/{pink4}<<*<.>>*{brown}\{pink4}<.<*<><>.<{pink4}><
{tab}{w}Level 1:{pink4}                                                                                >>>.*<><*<{brown}__{reset}{leveltwo_c}( Ｂ ){pink4}>*.{leveltwo_c}( Ｃ ){brown}__{pink4}**>>*.{pink4}><
{tab}                                                                                      >>>.**<*{brown}/{pink4}<><*<><.>{brown}|{pink4}<<*<.>>{brown}|{pink4}<<*<.{brown}\{pink4}<<*<.>{pink4}><
{tab}                                                                                    >>>.*<<.<{brown}/{pink4}<><*<.>>>*{brown}|{pink4}<<*<.>>{brown}|{pink4}<<*<.>{brown}\{pink4}<<*<.>>{pink4}><
{tab}                                                                                  >>>.*.<<>*{brown}/{pink4}<<>*<.>>*>*{brown}|{pink4}<<*<.>>{brown}|{pink4}<<*<.>>{brown}\{pink4}<<*<.>>*{pink4}><
{tab}                                                                                >>>.*..<<>*{brown}/{pink4}<<*<.>>*<<*<{brown}|{pink4}<<*<.>>{brown}|{pink4}<<*<.>>*{brown}\{pink4}<<*<.>>*>{pink4}><
{tab}{w}Level 2:{pink4}                                                                      >>>..>.<{levelthree_c}( Ｄ ){pink4}<.<*<.<<{levelthree_c}( Ｅ ){pink4}<<*<{levelthree_c}( Ｆ ){pink4}.>>>>*{levelthree_c}( Ｇ ){pink4}>>>*>><
{tab}                                                                            >>>.<<>*{brown}/{pink4}<<*<{brown}|{pink4}<<<<*<.>>*{brown}{f_slash(10)}{pink4}<*<{brown}{pipe(11)}{pink4}<*<.>>*{brown}{pipe(12)}{pink4}<*<{brown}{b_slash(13)}{pink4}*<.>>><{brown}{pipe(14)}{pink4}*<.{brown}{b_slash(15)}{pink4}*<.>>>><
{tab}                                                                          >>.<<<*>.{brown}/{pink4}<<*<.{brown}|{pink4}<<*<.>>*>{brown}{f_slash(10)}{pink4}<*<.{brown}{pipe(11)}{pink4}<*<.>>*{brown}{pipe(12)}{pink4}<*<.{brown}{b_slash(13)}{pink4}*<.>>>{brown}{pipe(14)}{pink4}*<.>{brown}{b_slash(15)}{pink4}*<.>>><><
{tab}                                                                        >>>..<.<>*{brown}/{pink4}<<*<.>{brown}|{pink4}<<*<.>>*{brown}{f_slash(10)}{pink4}<*<.>{brown}{pipe(11)}{pink4}<*<.>>*{brown}{pipe(12)}{pink4}<*>>*{brown}{b_slash(13)}{pink4}*<.>>{brown}{pipe(14)}{pink4}*<.>>{brown}{b_slash(15)}{pink4}*<.>>><>><
{tab}                                                                      >>>...><<>>{brown}/{pink4}<<*<.>>{brown}|{pink4}<<*<.>>{brown}{f_slash(10)}{pink4}<*<.>>{brown}{pipe(11)}{pink4}<*<.>>*{brown}{pipe(12)}{pink4}<*<.>>{brown}{b_slash(13)}{pink4}*<.>{brown}{pipe(14)}{pink4}*<.>>>{brown}{b_slash(15)}{pink4}*<.>>><<>><
{tab}{w}Level 3:{pink4}                                                            >>>.*.>.{levelfour_c}( Ｈ ){pink4}>><.{levelfour_c}( Ｉ ){pink4}>>{levelfour_c}{node('( Ｊ )', 10)}{pink4}<{levelfour_c}{node('( Ｋ )', 11)}{pink4}<<<{levelfour_c}{node('( Ｌ )', 12)}{pink4}>{levelfour_c}{node('( Ｍ )', 13)}{pink4}<{levelfour_c}{node('( Ｎ )', 14)}{pink4}<{levelfour_c}{node('( Ｏ )', 15)}{pink4}>.>>>>><
{tab}                                                                  >>>...>*.{brown}{f_slash(16)}{pink4}><{brown}{pipe(17)}{pink4}<<*<.>>*>{brown}{f_slash(18)}{brown}{b_slash(19)}{pink4}<*<.>>*{brown}{pipe(20)}{pink4}*>>.<<*<<<*<<<>*>>.<<*<.>>*<<.<*<.>>*<<.<*<.>>>><
{tab}                                                                >>>..*>..{brown}{f_slash(16)}{pink4}<<><{brown}{pipe(17)}{pink4}<*<.>>*>{brown}{f_slash(18)}{pink4}**{brown}{b_slash(19)}{pink4}<*<.>>{brown}{pipe(20)}{pink4}*>>.<<*<<<*<<<>*>>.<<*<.>>*<<.<*<.>>*<<.<*<.>>><><
{tab}                                                              >>>....>*{brown}{f_slash(16)}{pink4}<<*<.>{brown}{pipe(17)}{pink4}<*<.>>*{brown}{f_slash(18)}{pink4}<<<.{brown}{b_slash(19)}{pink4}<*<.>{brown}{pipe(20)}{pink4}*>>.<<*<<<*<<<>*>>.<<*<.>>*<<.<*<.>>*<<.<*<.>>><<<>< 
{tab}                                                            >>>...>.*{brown}{f_slash(16)}{pink4}<<*<.>>*{brown}{pipe(17)}{pink4}<*<.>>{brown}{f_slash(18)}{pink4}<*<.>>{brown}{b_slash(19)}{pink4}<*<.{brown}{pipe(20)}{pink4}*>>.<<*<<<*<<<>*>>.<<*<.>>*<<.<*<.>>*<<.<*<.>>><<<>>><
{tab}{f'{w}Level 4:' if nodes_num > 15 else f"{reset}        "}{pink4}                                                  >>>.>>>{levelfive_c}{node('( Ｐ )', 16)}{pink4}>>*{levelfive_c}{node('( Ｑ )', 17)}{pink4}>{levelfive_c}{node('( Ｒ )', 18)}{pink4}<{levelfive_c}{node('( Ｓ )', 19)}{pink4}>{levelfive_c}{node('( Ｔ )', 20)}{pink4}<<<*<<<>*>*>>>**><*<<<*>>.><*<<<**<<<<*<<*>>>><*<<<><
{tab}                                                        >>>.>>>*><<.<<<*<*<<>*>>.<<*<<<*<<<>*>>.<<*<.>>*<<.<<<*<*<<>*>>.<<*<<<*<<<>*>>.>*>>>><*<<<<<>><*<<>< 
{tab}                                                      >>>.>>>>*<<>.<<<*<*<<>*>>.<<*<<<*<<<>>.<<*<.>>*<<.<<<*<*<<>*>>.<<*<<<*<<<>*>>.>*>>>><*<<<*<<<>>.*<*<<*>< 
{tab}                                                    >>>.>>>>*<<.<<><*<*<<>*>>.<<*<<<*<<<>*>>.<<*<.>>*<<.<<<*<*<<>*>>.<<*<<<*<<<>*>>.>**>>>><*<<<*<<<<<*<<>>*>>< 
{tab}                                                  >>><*<.>>*<<.<<<*><*<<>*>>.<<*<<<*<<<>*>>.<<*<.>>*<<.<*<.>>*<<.<*<.>>*<<.<<<*<*<<>*>>.<<*<<<*<<<*<<<*<<*<<><<>< {y}
{tab}                                                                                                      __\db/__
{w}{r}""")


tab = tab*10+f" "*18
print(f"{tab}{' '*10}ＲＯＯＴ: ", w+root.data)
print(f"{tab}{r}{' '*8}ＥＤＧＥＳ: {w}", nodes_num-1, r)
print(f"\n{tab}  ＰＡＲＥＮＴ ＮＯＤＥＳ ({len(parent_nodes)}):{w}",end="")
for i, nodee in enumerate(sorted(parent_nodes)):
	if i%4==0:
		print("\n"+tab+nodee, end=",   ")
	else:
		print(nodee, end=",   ")
print(f"\n\n{r}{tab}   ＣＨＩＬＤ ＮＯＤＥＳ ({len(child_nodes)}):{w}", end="")
for i, nodee in enumerate(sorted(child_nodes)):
	if i%4==0:
		print("\n"+tab+nodee, end=",   ")
	else:
		print(nodee, end=",   ")
print(f"\n\n{r}{tab}{' '*7}ＳＩＢＬＩＮＧＳ ({len(siblings)}):{w}", end="")
for i, nodee in enumerate(siblings):
	if i%2==0:
		print("\n"+tab+nodee, end=",  ")
	else:
		print(nodee, end=",   ")
print(f"\n\n{r}{tab}     ＬＥＡＦ ＮＯＤＥＳ ({len(leaf_nodes)}):{w}", end="")
for i, nodee in enumerate(leaf_nodes):
	if i%4==0:
		print("\n"+tab+nodee, end=",   ")
	else:
		print(nodee, end=",   ")
print(f"\n\n{r}{tab}{' '*9}ＤＥＧＲＥＥ ({len(degree)}):{w}", end="")
for i, key_value in enumerate(degree.items()):
	if i%3==0:
		print(f"\n{tab}( {key_value[0]} ) = {key_value[1]}", end=f",   "  )
	else:
		print(f"( {key_value[0]} ) = {key_value[1]}", end=",   "  )
print(f"\n\n{r}{tab}{' '*10}ＰＡＴＨＳ({len(paths)}):{w}\n{tab}{' '*7}"+ f'\n{f"{tab}"}       '.join(paths))
print(f"\n{r}{tab}ＨＥＩＧＨＴ ＯＦ ＴＨＲＥＥ: {w}", getHeight(root))
print(f"{r}{tab}ＤＥＰＴＨ ＯＦ ＴＨＲＥＥ: {w}", maxDepth(root))
