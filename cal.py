def meter_to_centimeter(meter):
    try: 
        centimeter = meter * 100 
        return centimeter
    except ValueError:
        print("Something went wrong!")
        
def centimeter_to_foot( centimeter):
    try:
        feet = centimeter * 30.48 
        return feet
    except ValueError:
        print("Something went wrong!")
        
def sqft_area_calc(height_meters, length_meters):
    try:
        sqft = meter_to_centimeter(height_meters) * meter_to_centimeter(length_meters) / 929.0304  # 1 square foot = 929.0304 square centimeters
        return sqft
    except ValueError:
        print("Something went wrong!")
        
def watts_to_lumen(watts):
    try:
        lumens = watts * 100
        return lumens 
    except ValueError:
        print("Something went wrong!")
        
def calculate_lumens_per_sqft(total_lumens, sqft_area):
    try:
        lumens_per_sqft = total_lumens / sqft_area
        return lumens_per_sqft
    except ZeroDivisionError:
        return "Area can't be Zero!"

#Inputs 
heigth_meters = float(input('Enter the height in meters: '))

length_meters = float(input('Enter the length in meters: '))

watts = float(input('Enter the watts '))

#Calculation
height_cm = meter_to_centimeter(heigth_meters)
length_cm = meter_to_centimeter(length_meters)
sqft_area = sqft_area_calc(heigth_meters, length_cm)
lumens = watts_to_lumen(watts)
lumens_per_sqft = calculate_lumens_per_sqft(lumens, sqft_area)

#Display results 
print(f'Height in meters: {heigth_meters}m')
print(f'Length in meters: {length_meters}m')
print(f'Area in square feet: ', format(sqft_area, '.2f'),'f²')
print(f'Watts: {watts}w')
print(f'Total lumens: {lumens}lumens')
print(f'Lumens per square foot: ',format(lumens_per_sqft, '.2f'), 'lumen/f²')
