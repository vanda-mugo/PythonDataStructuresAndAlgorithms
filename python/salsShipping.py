weight = float(input("Enter the weight in pounds: "))

ground_shipping = 0
ground_shipping_premium = 125
drone_shipping = 0
if(weight != 0 and weight  <= 2):
  ground_shipping = (1.50 * weight) + 20
  drone_shipping = (4.50 * weight)
elif(weight > 2 and weight <= 6):
  ground_shipping = (3.00 * weight) + 20
  drone_shipping = (9.00 * weight)
elif(weight > 6 and weight <=10):
  ground_shipping = (4.00 * weight) + 20
  drone_shipping = (12.00 * weight)
else:
  ground_shipping = (4.75 * weight) + 20
  drone_shipping = (14.25 * weight)




print("ground shipping:{} while drone shipping:{}  and ground_shipping_premium:{}".format(ground_shipping, drone_shipping,ground_shipping_premium) )

if(ground_shipping < drone_shipping  and ground_shipping < ground_shipping_premium):
  print("preffered shipping method is: Ground_shipping at {}".format(str(groud_shipping)))

if(ground_shipping_premium < drone_shipping  and ground_shipping_premium < ground_shipping):
  print("preffered shipping method is: Ground_shipping_premium at {}".format(str(groud_shipping_premium)))

if(drone_shipping < ground_shipping_premium  and drone_shipping < ground_shipping):
  print("preffered shipping method is: drone_shipping at {}".format(str(drone_shipping)))
  





  
