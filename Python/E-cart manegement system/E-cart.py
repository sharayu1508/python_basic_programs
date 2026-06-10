products=[]

while True:
    print()
    print("*** Ecart *** ")
    print(" 1.View Products \n 2.Add Products \n 3.Update Product \n 4.Delete Product \n 5.Search \n 6.Generate Bill \n 7.Exit ")

    ch=int(input("Enter your choice : "))
    match ch:
        case 1:
            if(products==[]):
                print("Empty!!!\n Please add the product ")
            else:
                print("--- Product Details --- ") 
                print("ID",end=" ")
                print("Name",end=" ")
                print("Qty",end="  ")
                print("Price",end="  ")
                print()
            for list in products:
                print(list[0],end="   ")
                print(list[1],end="   ")
                print(list[2],end="    ")
                print(list[3],end="     ")
                print()
            
        case 2:
          no=int(input("How many products you want to add : "))
          print("Enter Product Details : ")
          id=len(products)
          for i in range(no):
               
               print(f"Product {i+1} : ")
               id+=1
               print("ID : ",id)
               name=input("name : ")
               quantity=int(input("quantity : "))
               price=int(input("price : "))
               print("\n")
               list=[id,name,quantity,price]
               products.append(list)
          

        case 3:
          item=input("What do you want to update (Product quantity / price) : ")
          n=input("Enter a name : ")
          found=False
          for list in products:
            if(list[1]==n):
                    found=True
                    
                    if(item=="quantity"):
                        q=int(input("Enter a quantity : "))
                        list[2]=q

                    elif(item=="price"):
                        p=int(input("Enter a price : "))
                        list[3]=p

                    print("Updated Successfully")
                    print(products)
                    break
          if not found: 
               print(" Product not found ")
          
        case 4:
            dpro=int(input("1.Delete all products \n 2.Delete one product : "))
            found=False
            if(dpro==1):
                products.clear()
                print("Deleted Successfully!!!")
            else:
                pid=int(input("Enter Id of product you want to delete : "))
                for list in products:
                  if(list[0]==pid):
                    products.remove(list)
                    found=True
                    print("Deleted Successfully")
                    print(products)

                if not found :
                    print("Product ID not found ")
          
        case 5:
          s=int(input("1.Search by ID \n 2.Search by Name : "))
          found=False
          if(s==1):
              found=True
              sid=int(input("Enter a Product id : "))
              for list in products:
                  if(list[0]==sid):
                      print("Product Found")
                      print("Product details : ",list)
                      break
              if not found:
                    print("Product not found!!!")
          found=False
          if(s==2):
              found=True
              sname=input("Enter a Product Name : ")
              for list in products:
                  if(list[1]==sname):
                      print("Product Found")
                      print("Product details : ",list)
                      break
                  
              if not found:
                      print("Product not!!!")

        case 6:
          total=0
          for list in products:
             amount=list[2]*list[3]
             total=total+amount
        
          print("--- Product Details --- ") 
          print("ID",end=" ")
          print("Name",end=" ")
          print("Qty",end="  ")
          print("Price",end="  ")
          print()

          for list in products:
                print(list[0],end="   ")
                print(list[1],end="   ")
                print(list[2],end="    ")
                print(list[3],end="     ")
                print()



          print("Total Bill without GST : ",total)
          gst=total*(0.18)
          print("GST : ",gst)
          final_amount=total+gst
          print("Total Bill including GST (18%) amount : ",final_amount)
              
        case 7:
          print(" Thank You!!!")
          break
