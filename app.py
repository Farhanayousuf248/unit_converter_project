

import streamlit as st 

def convert_units(value: float, unit_from: str, unit_to: str):
   # print("value>>>", value)
   # print("unit_from>>>", unit_from)
   # print("unit_to>>>", unit_to)

    #    Conversion Logic

     if unit_from == "kilometers" and unit_to == "meters":
         return value * 1000
     elif unit_from == "meters" and unit_to == "kilometers":
         return value * 0.001
     elif unit_from == "kilograms" and unit_to == "grams":
         return value * 1000
     elif unit_from == "grams" and unit_to == "kilograms":
         return value * 0.001
     else:
         return "Conversion is not possible!"


##     Main Function
def main():
  
   st.title("unit_converter")
   st.header("Welcome to unit_converter!")
   value =st.number_input("Enter the value you want to convert:",min_value =0.0)
   unit_from=st.text_input("Enter the unit you want to convert from (e.g. kilometers, meters,kilograms, grams):")
   unit_to=st.text_input("Enter the unit you want from conversion (e.g. kilometers, meters, kilograms, grams):")

   if st.button("convert"):
      result = convert_units(value, unit_from, unit_to)
      st.write("Converted value is:", result)

    #print("unit_converter")
   # print("Welcome to unit_converter!")
    
   # value = float(input("Enter the value you want to convert: "))
   # unit_from = input("Enter the unit you want to convert from (e.g. kilometers, meters, kilograms, grams):").strip().lower()
   # unit_to = input("Enter the unit you want from conversion (e.g. kilometers, meters, kilograms, grams):").strip().lower()

   # print("value>>>", value)
   # print("unit_to>>>", unit_to)
   # print("unit_from>>>", unit_from)
    
   # result = convert_units(value, unit_from, unit_to)
   # print("Converted value is:", result)

##    Run the program
main()

