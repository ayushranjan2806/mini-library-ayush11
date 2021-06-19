class Library:
    def __init__(self,list_of_books,library_name):
        self.listofbooks=list_of_books
        self.libraryname=library_name
        self.lender_data={}
        self.deleted_books=[]
    def display_books(self):
        for index,book in enumerate(self.listofbooks):
            print(f"{index}.{book}")  
    def lend_book(self):
        print("enter your name for track record......")
        lender_name=input().upper()
        print("enter your required book ")
        requ_book=input().upper()
        if requ_book in self.listofbooks:
            print(f"you lend{requ_book}")
            self.listofbooks.remove(requ_book)
            self.lender_data.update({lender_name:requ_book}) 
        else:
            print("book is not available right now!! sorry for inconvience/!! the book is lended by") 
            for owner_name ,book_name in self.lender_data.items():
                if book_name == requ_book:
                    print(f"{book_name} was lended by {owner_name} ")
    def return_list(self):
        print("please! enter your name")
        returner_name=input().upper()
        print("enter your book name which you want to return")
        return_book_name =input().upper        
        for ret_name ,ret_book_name in self.lender_data.items() :
            if    returner_name==ret_name and    return_book_name== ret_book_name :
                print(f"thank you for submitting your tended book !vising again!!@@")
                del self.lender_data[ret_name]
                self.listofbooks.append(ret_book_name)
                break
    def add_book(self):
        print("enter your book name which you want to add ") 
        book_details=input().upper()
        self.listofbooks.append(book_details)

    def delete_books_inlist(self):
        deleting_book=input().upper()
        if deleted_book in listofbooks:
            self.listofbooks.remove( deleting_book)
            self.deleted_books.append( deleting_book)
    def display_deleted_books(self):
        for index,book in enumerate(self.deleted_books):
            print(f"{index}.{book}")  
    
def main():
    list_books=["HC VERMA","KC SINHA","SL ARORA","BASIC EE","QUANTUM","AKTU PYP","SHORT NOTES BOOKS","CHEMISTRY ","BALAJI PUBLICATION"]
    library_name="AYUSH GENTLEMAN LIBRARY"
    ayu=Library(list_books,library_name)
    print("welcome to {ayu. library_name}\n q for exit\n use d for display books \n use r for return book\n use de for deleted book\n use dd for display delete book \n l for lended book \n use a for adding books ")
    exit=False
    while(exit is not True):
        print("enter your choice and use library service")
        choice=input()

        if choice=="l":
            ayu.lend_book()
        elif choice=="d":
            ayu.display_books()
        elif choice =="dd":
            ayu.display_deleted_books()
        elif choice=="de":
            ayu.delete_books_inlist()
        elif choice =="a":
            ayu.add_book()
        elif choice=="r":
            ayu.return_list()
        elif choice =="q":
            print(f"thank you for visiting  {ayu.libraryname} .I hope you must enjoy our service ")
            exit=True
        else:
            print("you enter wrong choice please enter valid  input !!!")

if __name__ == "__main__":
    main()

    



