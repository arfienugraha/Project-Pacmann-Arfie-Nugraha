# Python Project : Self Cashier
This is a program in doing self service cashier transaction in Bahasa made by Arfie Nugraha
# A. Background
Transaction is one of the step needeed in closing a purchase. The problems come when in a peak hour, sometimes it takes a long time just to input the items (item name, quantity, and price). The main goal of this program is to create a self service check out system so the queue time befor payment can be reduced.
# B. Tools
  Language :
  Python
  
  Module :
  ModuleCashier.py
  
# C. Objectives
 Make a program that has features :
 
 a. Add new items and other detailed informations like item quantity and price per item
 
 b. Update item name
 
 c. Update item quantity
 
 d. Update price per item
 
 e. Verify the order
 
 f. Display current cart
 
 g. Delete a particular item
 
 h. Delete all items
 
 i. Display and check out total price
 
# D. Flow Chart Program
![Flow Chart Tugas Besar Pacmann 4 drawio](https://user-images.githubusercontent.com/89647712/232277424-4609a118-7f80-464b-8ed1-66a985752481.png)
 
# E. Function 
There is no function located in the main program MainCashier.py while there are 10 functions in

 a. init :
 This is a function to initialize the class Transaction. In this function, it only consist of the initialitation of dictionary attributes tabel_belanja
 
 b. add_item :
This is a function to receive data item name, item quantity, and price per item from main program input, and keep it in a dictionary namely tabel_belanja.
  
 c. update_item_name : 
 This is a function to update the name of the item (dictionary key) without change the other data
 
 d. update_item_qty : 
 This is a function to update the quantity of the item (dictionary value) based on the name that has been inputted
 
 e. update_harga_item :
 This is a function to update the price per item (dictionary value) based on the name that has been inputted
 
 f. check_order : 
 This is a function to check whehter the input has been correct or still wrong
 
 g. summary :
 This is a function to display current cart to be paid
 
 h. delete_item :
 This is a function to delete an item based on an input of item_name (dictionary key), to delete the entire dictionary value (item_qty and price per item)
 
 i. reset_transaction :
 This is a function to delete all items in the dictionary tabel belanja
 
 j. total_price :
 This is a function to calculate the total price to be paid, including the discount that vary based on total amount from summary
 
 # F. How to Run the Program
 1. Download all Ppograms(MainCashier.py and ModuleCashier.py) and save in one directory (folder)
 2. Open terminal in the associated directory
 3. Run main program MainCashier.py
 
 # G. Test Case : 
 The first test case is to check the add_item function whether it can add the item name, item quantity, and price per item.  
 
 ![Test Case 1 File MainCashier](https://user-images.githubusercontent.com/89647712/232183483-54b9ede7-81e7-4de8-a3e1-9dc52695540a.PNG)

 The second test case is to check the delete_item whether it can delete one dictionary in tabel_belanja based on the input in name (dictionary key)
 
 ![Test Case 2 File MainCashier](https://user-images.githubusercontent.com/89647712/232183679-ab3a32e1-71ab-4adb-a567-e5a7aa80fd6b.PNG)
 
 The third test case is to check the reset_transaction whether it can delete all items (key and value) in the dictionary
 
 ![Test Case 3 File MainCashier](https://user-images.githubusercontent.com/89647712/232183921-a7fd5c32-9357-4d44-b459-b715e093811d.PNG)

 The fourth test case is to check the total_prce function whether it can give the discount based on the total amount and calculate the total price to be paid
 3
 ![Test Case 4 File MainCashier](https://user-images.githubusercontent.com/89647712/232183997-65feb8b1-170c-460f-813f-55a1de077ebf.PNG)

 The fifth test case is to display when main program MainCashier.py is executed

 ![Test Case 5 File Main Cashier](https://user-images.githubusercontent.com/89647712/232184230-d164efd9-d3ca-4d6e-88d0-0c05df67b97e.PNG)



 # H. Conclusion and Future Improvement
1. The program has been successfully made based on the requirement
2. The program has been passed the test case 
3. For future improvement, it will be necessary to display the data in pandas (dataframe)





