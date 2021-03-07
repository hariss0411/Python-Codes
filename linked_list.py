class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

        
class Linked_list:
    def __init__(self):
        self.start=None
    def insert_start(self,new_node):
        if self.start==None:
            self.start=new_node
        else:
            (new_node.next,self.start)=(self.start,new_node)
            #temp=self.start
            #self.start=new_node
            #new_node.next=temp
    def insert_end(self,new_node):
        if self.start==None:
            self.start=new_node
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=new_node
    def insert_after(self,new_node):
        if self.start==None:
            print("List Empty")
        else:
            af_data=int(input("Enter Data after you have to insert:- "))
            temp=self.start
            while temp!=None and af_data!=temp.data:
                temp=temp.next
            if temp==None:
                print(af_data,"Not Found")
            else:
                new_node.next=temp.next
                temp.next=new_node
    def display(self):
        temp=self.start
        if temp==None:
            print("Empty")
            return
        while temp!=None:
            print(temp.data)
            temp=temp.next

            
link_list=Linked_list()
ch=1
while ch:
    ch=int(input("0 for exit\t1 for Display\t2 for insert End\t3 for insert Start\t4 for insert After:= "))
    switch={0:'break',
            1:'link_list.display()',
            2:'link_list.insert_end(Node(int(input("Enter Data:= "))))',
            3:'link_list.insert_start(Node(int(input("Enter Data:= "))))',
            4:'link_list.insert_after(Node(int(input("Enter Data:= "))))'}
    eval(switch[ch])
    '''if ch==1:
        link_list.display()
    elif ch==2:
        link_list.insert_end(Node(int(input("Enter Data:= "))))
    elif ch==3:
        link_list.insert_start(Node(int(input("Enter Data:= "))))
    elif ch==4:
        link_list.insert_after(Node(int(input("Enter Data:= "))))'''
